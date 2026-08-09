# Apprendre à faire des choix

"""Exercice 1

Demande l'âge d'une personne.

Affiche un message différent selon l'âge."""

âge = int(input("Quel est ton âge ? "))

if âge < 18:
    print("Tu es mineur.")
else:
    print("Tu es majeur.")

"""Exercice 2

Demande une note.

Affiche une appréciation selon le résultat."""

note = float(int(input("Quelle est ta note ? ")))

if note >= 10:
    print("Tu as réussi !")
elif note >= 15:
    print("Tu es excellent.")
else:  
    print("Tu as échoué.")

"""Exercice 3

Crée un programme qui vérifie si un nombre est :

positif ;
négatif ;
nul."""

nombre = int(input("Donne-moi un nombre : "))

if nombre == 0:
    print("Le nombre est nul.")
elif nombre > 0:
    print("Le nombre est positif.")
else:
    print("Le nombre est négatif.")

"""Exercice 4 

Crée un programme qui demande un mot de passe à l'utilisateur et vérifie s'il est correct."""

password = input("Entre un mot de passe : ")
check_password = input("Confirme le mot de passe : ")

if password == check_password:
    print("Le mot de passe est correct.")
else:
    print("Les mots de passe ne correspondent pas.")
