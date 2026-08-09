print("BIENVENUE DANS LE GESTIONNAIRE DE TÂCHES !")

tasks = []

while True:
    print("\nMenu :")
    print("1. Ajouter une tâche")
    print("2. Supprimer une tâche")
    print("3. Afficher les tâches")
    print("4. Quitter")

    choix = input("Choisissez une option (1-4) : ")

    if choix == '1':
        tache = input("Entrez la tâche à ajouter : ")
        tasks.append(tache)
        print(f"Tâche '{tache}' ajoutée.")
    elif choix == '2':
        tache = input("Entrez la tâche à supprimer : ")
        if tache in tasks:
            tasks.remove(tache)
            print(f"Tâche '{tache}' supprimée.")
        else:
            print(f"Tâche '{tache}' non trouvée.")
    elif choix == '3':
        print("Liste des tâches :")
        for task in tasks:
            print(f"- {task}")
    elif choix == '4':
        print("Au revoir !")
        break
    else:
        print("Option invalide, veuillez réessayer.")

