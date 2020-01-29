import json

dataDict = {'fnamn': None, 'enamn': None, 'email': None}
lineList = []
people = []


def ReadOriginalFile(filename):
    with open (filename, "r", encoding="utf-8") as currentFile:
            for line in currentFile:
                lineList = line.rstrip("\n").split(";")
                n = 0
                for key in dataDict:
                    dataDict[key] = lineList[n]
                    n += 1
                    if n == 2: # skippa tredje elementet
                        n = 3
                people.append(dataDict.copy())
    for person in people:
        print(person)
    return people

def ReadJson(filename):
    try:
        with open (filename, "r", encoding="utf-8") as jsonFile:
            people = json.load(jsonFile)
            for person in people:
                print(person)
    except json.decoder.JSONDecodeError:
        print("Din fil är tom")

def AddPerson():
    with open("lista personer.json", "r", encoding="utf-8") as jsonFile:
        try:
            people = json.load(jsonFile)
        except json.decoder.JSONDecodeError:
            print("Din fil är tom")
            people = []
        dataDict["fnamn"] = input("Ange förnamn: ")
        dataDict["enamn"] = input("Ange efternamn: ")
        dataDict["email"] = input("Ange email: ")
        people.append(dataDict)
    return people

def DeletePerson():
    with open("lista personer.json", "r", encoding="utf-8") as jsonFile:
        people = json.load(jsonFile)
        personToDelete = input("Ange förnamn: ")
        people = [person for person in people if person['fnamn'] != personToDelete]
    return people

def SaveAsJson(filename, data):
    while True:
        with open (filename, "w", encoding="utf-8") as jsonFile:
            if len(data) > 0:
                json.dump(data, jsonFile, ensure_ascii=False)
                print("Sparat!")
                break
            else:
                print("Du har inget att spara")
                break

def UserInputInt():
    while True:
        try:
            x = int(input("Ange en siffra: "))
            print("\n")
            break
        except:
            print("Error, inte giltig siffra, försök igen")
    return x

