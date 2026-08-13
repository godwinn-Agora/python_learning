# Les dictionnaires.

"""Qu'est-ce qu'une clé?"""
# Une clé est un identifiant unique utilisé pour accéder à une valeur dans un dictionnaire.

"""Qu'est-ce qu'une valeur?"""
# Une valeur est l'objet associé à une clé dans un dictionnaire.

"""Créer un dictionnaire :"""
dico = {}

"""Lire un dictionnaire :"""
print(dico)

"""modifier un dictionnaire :"""
dico["clé"] = "valeur"
print(dico)

"""Ajouter un élément à un dictionnaire :"""
dico["nouvelle_clé"] = "nouvelle_valeur"
print(dico)

"""Supprimer un élément d'un dictionnaire :"""
del dico["clé"]
print(dico)

"""parcourir un dictionnaire :"""
for clé, valeur in dico.items():
    print(f"{clé}: {valeur}")

"""Taille d'un dictionnaire :"""
print(len(dico))  # Affiche le nombre d'éléments dans le dictionnaire

"""keys() :"""
print(dico.keys())  # Affiche toutes les clés du dictionnaire

"""values() :"""
print(dico.values())  # Affiche toutes les valeurs du dictionnaire

"""items() :"""
print(dico.items())  # Affiche toutes les paires clé-valeur du dictionnaire

"""get() :"""
print(dico.get("clé"))  # Affiche la valeur associée à la clé "clé", ou None si la clé n'existe pas