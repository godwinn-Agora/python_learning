#Faire communiquer ton programme avec l'utilisateur

prénom = input("Quel est ton prénom ? ")
print("Bonjour", prénom, "!")

a = int(input("Donne-moi un nombre : "))
b = int(input("Donne-moi un autre nombre : "))
c = a + b
print("La somme de", a, "et", b, "est :", c)

naissance = int(input("En quelle année es-tu né ? "))
année_actuelle = 2026
âge = année_actuelle - naissance
print("Tu as", âge, "ans.")

prenom = input("Quel est ton prénom ? ")
age = int(input("Quel est ton âge ? "))
pays = input("Dans quel pays vis-tu ? ")
intérêts = input("Quels sont tes intérêts ? ")

print(f"Bonjour {prenom}, tu as {age} ans, tu vis en {pays} et tes intérêts sont : {intérêts}.")
