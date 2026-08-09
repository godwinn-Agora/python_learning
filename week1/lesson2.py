#Faire communiquer ton programme avec l'utilisateur

"""Exercice 1 Demande : « Quel est ton prénom ? » Puis affiche une phrase personnalisée."""

prénom = input("Quel est ton prénom ? ")
print("Bonjour", prénom, "!")

"""Exercice 2 Demande deux nombres et affiche leur somme. Attention : Comprends pourquoi input() renvoie une chaîne de caractères."""

a = int(input("Donne-moi un nombre : "))
b = int(input("Donne-moi un autre nombre : "))
c = a + b
print("La somme de", a, "et", b, "est :", c)

"""Exercice 3 Demande l'année de naissance de l'utilisateur et calcule son âge."""

naissance = int(input("En quelle année es-tu né ? "))
année_actuelle = 2026
âge = année_actuelle - naissance
print("Tu as", âge, "ans.")

"""Exercice 4 Demande à l'utilisateur plusieurs informations et affiche-les dans un message personnalisé."""

prenom = input("Quel est ton prénom ? ")
age = int(input("Quel est ton âge ? "))
pays = input("Dans quel pays vis-tu ? ")
intérêts = input("Quels sont tes intérêts ? ")

print(f"Bonjour {prenom}, tu as {age} ans, tu vis en {pays} et tes intérêts sont : {intérêts}.")
