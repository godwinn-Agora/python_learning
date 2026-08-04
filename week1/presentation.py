

while True:
    menu = ["Dire Bonjour", "Afficher mon nom", "Afficher mon âge", "Quitter"]
    for index, option in enumerate(menu):
        print(f"{index + 1}. {option}")

    choice = int(input("Choisis une option : "))
    if choice == 1:
        print("Bonjour !")
    elif choice == 2:
        nom = input("Quel est ton nom ? ")
        print(f"Ton nom est : {nom}")
    elif choice == 3:
        age = input("Quel est ton âge ? ")
        print(f"Ton âge est : {age} ans")
    elif choice == 4:
        print("Au revoir !")
        break
    else:
        print("Option invalide. Veuillez choisir une option valide.")