import modules



while True:
    print("1. Läs in originalfil")
    print("2. Visa json-datat")
    print("3. Lägg till person")
    print("4. Ta bort person")
    print("5. Spara fil")
    print("6. Avsluta")
    userChoice = modules.UserInputInt()
    
    if userChoice == 1:
        data = modules.ReadOriginalFile("personer.csv")
    elif userChoice == 2:
        modules.ReadJson("lista personer.json")
    elif userChoice == 3:
        data = modules.AddPerson()
    elif userChoice == 4:
        data = modules.DeletePerson()
    elif userChoice == 5:
        modules.SaveAsJson("lista personer.json", data)
    else:
        break