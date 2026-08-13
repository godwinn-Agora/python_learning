"""Exercice 1

Crée une liste contenant 5 de tes activités préférées"""

activities = [ 'programming', 'reading', 'exercising', 'cooking', 'traveling' ]
print(activities[0])
print(activities[-1])
print(activities[1:4])
print(activities)

"""Exercice 2

Ajoute une activité avec append()."""

activities.append('painting')
print(activities)
"""Exercice 3

Supprime une activité avec remove()."""

activities.remove('reading')
print(activities)

"""Exercice 4

Parcourir la liste avec une boucle for et afficher chaque activité."""

for activity in activities:
    print(activity)

"""Exercice 5

Demande à l'utilisateur d'entrer 3 tâches à faire. Ajoute ces tâches à une liste et affiche la liste."""

task1 = input("Enter your first task: ")
task2 = input("Enter your second task: ")
task3 = input("Enter your third task: ")
tasks = [task1, task2, task3]
print("Your tasks are:")
for task in tasks:
    print(task)
