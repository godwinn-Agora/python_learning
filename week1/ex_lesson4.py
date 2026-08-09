"""Exercice 1

Afficher les nombres de 1 à 10."""

for i in range(1, 11):
    print(i)

"""Exercice 2

Afficher les nombres pairs de 1 à 100."""

for i in range(1, 101):
    if  i % 2 == 0:
        print(i)

"""Exercice 3

Demander un nombre et afficher sa table de multiplication."""

nombre = int(input("Donne-moi un nombre : "))
for i in range(0, 13):
    resultat = nombre * i
    print(f"{nombre} x {i} = {resultat}")

"""Exercice 4

Créer un programme qui demande plusieurs réponses à l'utilisateur."""

answer = ["A", "B", "C", "D"]
for index, reponse in enumerate(answer):
    print(f"Réponse {index + 1} : {reponse}")

choix = input("Quelle réponse choisis-tu ? : ")
if choix in answer:
    print(f"Tu as choisi : {choix}")

"""Exercice 5 — Défi

Créer un programme qui continue de fonctionner tant que l'utilisateur ne choisit pas :

« Quitter »."""

for i in range(1, 101):
    print(i)

    if i % 10 == 0:
        while True:
            boutons = ["Rester", "Quitter"]
            for index, bouton in enumerate(boutons):
                print(f" {index + 1}. {bouton}")

            action = int(input("Quelle action veux-tu effectuer ?"))

            if action == 1:
                break
            elif action == 2:
                print("OFF") 
                stop = True
                break
            else:
                print("Action invalide. Veuillez choisir 1 ou 2.")

        if 'stop' in locals() and stop:
            break
