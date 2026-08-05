
print("Bienvenue !")

menu = ["Calculatrice", "Vérifier un nombre", "Table de multiplication", "Quitter"]
for index, option in enumerate(menu):
    print(f"{index + 1}. {option}")

choice = int(input("Choisis une option : "))
if choice == 1:
    print("CALCULATRICE")
    operations = ["Addition", "Soustraction", "Multiplication", "Division", "Quitter"]
    for index, operation in enumerate(operations):
        print(f"{index + 1}. {operation}")
    operation_choice = int(input("Choisis une opération : "))
    if operation_choice in [1, 2, 3, 4]:
        a = float(input("Donne-moi un nombre : "))
        b = float(input("Donne-moi un autre nombre : "))
    if operation_choice == 1:
        c = a + b
        print(f"{a} + {b} = {float(c)}")
    elif operation_choice == 2:
        c = a - b
        print(f"{a} - {b} = {float(c)}")
    elif operation_choice == 3:
        c = a * b
        print(f"{a} * {b} = {float(c)}")
    elif operation_choice == 4:
        c = a / b
        print(f"{a} / {b} = {float(c)}")
    elif operation_choice == 5:
        print("AU REVOIR !")
    else:
        print("Option invalide. Veuillez choisir une option valide.")

elif choice == 2:
    print("VÉRIFIER UN NOMBRE")
    verif = ["Vérifier si un nombre est pair ou impair", "Quitter"]
    for index, option in enumerate(verif):
        print(f"{index + 1}. {option}")
    choice = int(input("Choisis une option : "))
    if choice == 1:
        number = int(input("Donne-moi un nombre : "))
        if number % 2 == 0:
            print(f"{number} est pair.")
        else:
            print(f"{number} est impair.")
    elif choice == 2:
        print("AU REVOIR !")
    else:
        print("Option invalide. Veuillez choisir une option valide.")

elif choice == 3:
    print("TABLE DE MULTIPLICATION")
    table = ["Afficher la table de multiplication d'un nombre", "Quitter"]
    for index, option in enumerate(table):
        print(f"{index + 1}. {option}")
    choice = int(input("Choisis une option : "))
    if choice == 1:
        number = int(input("Donne-moi un nombre : "))
        for i in range(0, 13):
            result = number * i
            print(f"{number} x {i} = {result}")
    elif choice == 2:
        print("AU REVOIR !")
    else:
        print("Option invalide. Veuillez choisir une option valide.")

elif choice == 4:
    print("AU REVOIR !")

else:
    print("Option invalide. Veuillez choisir une option valide.")