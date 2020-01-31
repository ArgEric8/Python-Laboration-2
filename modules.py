import json

dataDict = {'fnamn': None, 'enamn': None, 'email': None}
people = []


def ReadOriginalFile(filename):
    lineList = []
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

def AddPerson(filename):
    with open(filename, "r", encoding="utf-8") as jsonFile:
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

def DeletePerson(filename):
    with open(filename, "r", encoding="utf-8") as jsonFile:
        people = json.load(jsonFile)
        personToDelete = input("Ange förnamn: ")
        if personToDelete == "alla":
            people = []
        else:
            people = [person for person in people if person['fnamn'] != personToDelete]
    return people

def SaveAsJson(filename, data):
    with open (filename, "w", encoding="utf-8") as jsonFile:
        json.dump(data, jsonFile, ensure_ascii=False)
        if len(data) > 0:
            print("- Sparat!")
        else:
            print("- Du har inget att spara")

def UserInputInt():
    while True:
        try:
            x = int(input("Ange en siffra: ")) 
            break
        except:
            print("Error, inte giltig siffra, försök igen")
    return x