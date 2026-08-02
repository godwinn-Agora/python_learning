# Faire répéter une action : Les boucles (for, while, break, continue, range, enumerate, zip, etc.)

"""1. Boucle for : elle permet de répéter une action un nombre défini de fois. Elle est souvent utilisée pour parcourir des séquences (listes, chaînes de caractères, etc.)."""
"""Exemple : Afficher les nombres de 1 à 5."""
for i in range(1, 6):
    print(i)
"""2. Boucle while : elle permet de répéter une action tant qu'une condition est vraie. Elle est souvent utilisée lorsque le nombre d'itérations n'est pas connu à l'avance."""
"""Exemple : Afficher les nombres de 1 à 5."""
i = 1
while i <= 5:
    print(i)
"""3. Break : il permet de sortir d'une boucle avant qu'elle ne se termine normalement. Il est souvent utilisé pour arrêter une boucle lorsqu'une condition spécifique est remplie."""
for i in range(1, 11):
    if i == 6:
        break
    print(i)
"""4. Continue : il permet de passer à l'itération suivante d'une boucle sans exécuter le reste du code de cette itération. Il est souvent utilisé pour ignorer certaines valeurs dans une séquence."""
for i in range(1, 11):
    if i == 6:
        continue
    print(i)
"""5. Range : il permet de générer une séquence de nombres. Il est souvent utilisé avec les boucles for pour parcourir une séquence de nombres."""
for i in range(1, 11):
    print(i)
"""6. Enumerate : il permet de parcourir une séquence tout en gardant une trace de l'index de chaque élément. Il est souvent utilisé pour parcourir des listes et des chaînes de caractères."""
fruits = ["pomme", "banane", "cerise"]
for index, fruit in enumerate(fruits):
    print(f"Index : {index}, Fruit : {fruit}")
"""7. Zip : il permet de combiner plusieurs séquences en une seule séquence de tuples. Il est souvent utilisé pour parcourir plusieurs listes en parallèle."""
noms = ["Alice", "Bob", "Charlie"]
âges = [25, 30, 35]
for nom, âge in zip(noms, âges):
    print(f"Nom : {nom}, Âge : {âge}")
    