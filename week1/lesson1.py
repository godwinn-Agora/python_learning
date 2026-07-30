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

prenom = input("Quel est ton prénom ? ")
age = int(input("Quel est ton âge ? "))

print(f"Bonjour {prenom}, dans 5 ans tu auras {age + 5} ans.")
