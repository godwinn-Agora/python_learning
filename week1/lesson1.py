# Découvrir les bases de Python
"""Exercice 1

Crée des variables contenant :

ton prénom ;
ton âge ;
ton pays ;
ton objectif professionnel.

Affiche-les."""

prenom = "Ouriel"
age = 17
pays = "Chine" 
objectif_professionnel = "Devenir développeur Python et experrt en IA/ML."

print("Prénom :", prenom)
print("Âge :", age)
print("Pays :", pays)
print("Objectif professionnel :", objectif_professionnel)

"""Exercice 2

Crée deux variables numériques et réalise :

addition ;
soustraction ;
multiplication ;
division."""

a = 10
b = 5
c = a + b
d = a - b
e = a * b
f = a / b

print("Addition :", c)
print("Soustraction :", d)
print("Multiplication :", e)
print("Division :", f)

"""Exercice 3

Crée un programme qui calcule l'âge d'une personne dans 5 ans."""

prenom = input("Quel est ton prénom ? ")
age = int(input("Quel est ton âge ? "))

print(f"Bonjour {prenom}, dans 5 ans tu auras {age + 5} ans.")

"""Exercice 4 — Réflexion

Essaie de répondre sans chercher :

Quelle est la différence entre une variable et une valeur ?

Pourquoi "17" et 17 ne représentent-ils pas exactement la même chose ?"""

"""Le premier 17 est une valeur de type chaîne de caractères (string), tandis que le second 17 est une valeur de type entier (integer). 
Une variable est un nom qui fait référence à une valeur stockée en mémoire, tandis qu'une valeur est la donnée elle-même."""


