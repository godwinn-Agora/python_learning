# Devine le nombre !
import random

print("Bienvenue dans le jeu du devine le nombre !")
levels = ["Facile (0-20)", "Moyen (0-50)", "Difficile (0-100)"]
for index, level in enumerate(levels):
    print(f"{index + 1}. {level}")
    
level = int(input("Choisis un niveau : "))
if level == 1:
    a = random.randint(0, 20)
elif level == 2:
    a = random.randint(0, 50)
else:
    a = random.randint(0, 100)

b = int(input("Devine le nombre aléatoire : "))

while True:
    if b == a:
        print("Félicitations ! Tu as deviné le nombre.")

        retry = ["Rejouer", "Quitter"]
        for index, option in enumerate(retry):
            print(f"{index + 1}. {option}")

        option = int(input("Choisis une option : "))
        if option == 1:
            if level == 1:
                a = random.randint(0, 20)
            elif level == 2:
                a = random.randint(0, 50)
            else:
                a = random.randint(0, 100)
        else:
            print("Merci d'avoir joué !")
            break

    elif a - 5 <= b <= a + 5:
        print("Le nombre que tu as choisi est très proche.")
    elif a + 5 < b <= a + 20:
        print("Le nombre que tu as choisi est supérieur.")
    elif a - 20 <= b < a - 5:
        print("Le nombre que tu as choisi est inférieur.")
    elif a + 20 < b <= 100:
        print("Le nombre que tu as choisi est trop grand.")
    elif 0 <= b < a - 20:
        print("Le nombre que tu as choisi est trop petit.")
    elif level == 1 and (b < 0 or b > 20):
        print("Le nombre que tu as choisi est invalide.")
    elif level == 2 and (b < 0 or b > 50):
        print("Le nombre que tu as choisi est invalide.")
    elif level == 3 and (b < 0 or b > 100):
        print("Le nombre que tu as choisi est invalide.")

    b = int(input("Devine le nombre aléatoire : "))
