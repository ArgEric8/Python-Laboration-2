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

def SaveAsJson(filename, data):
    try:
        with open (filename, "w", encoding="utf-8") as jsonFile:
            json.dump(data, jsonFile, indent=2, ensure_ascii=False)
    except:
        print("Något gick fel")

def ReadJson(filename):
    with open (filename, "r", encoding="utf-8") as jsonFile:
        for line in jsonFile:
            print(line)

def AddPerson():
    with open("lista personer.json", "r", encoding="utf-8") as jsonFile:
        people = json.load(jsonFile)
        dataDict["fnamn"] = input("Ange förnamn: ")
        dataDict["enamn"] = input("Ange efternamn: ")
        dataDict["email"] = input("Ange email: ")
        people.append(dataDict)
    return people

def DeletePerson():
    person = json.loads(open ("lista personer.json", "r"))
    for person in people:
        if ["fnamn"] == input("Ange förnamn för att ta bort: "):
            person.remove["fnamn", "enamn", "email"]
        break
    return people

def UserInputInt():
    while True:
        try:
            x = int(input("Ange en siffra: "))
            break
        except:
            print("Error, inte giltig siffra, försök igen")
    return x

