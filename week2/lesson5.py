# Les listes.
"""créer une liste :"""
ma_liste = [1, 2, 3, 4, 5]
print(ma_liste)

"""Accéder à un élément de la liste :"""
print(ma_liste[0])  # Affiche le premier élément de la liste
print(ma_liste[2])  # Affiche le troisième élément de la liste

"""index:"""
print(ma_liste[-1])  # Affiche le dernier élément de la liste
print(ma_liste[-2])  # Affiche l'avant-dernier élément de la liste

"""Modifier un élément de la liste :"""
ma_liste[0] = 10
print(ma_liste)  # Affiche la liste avec le premier élément modifié

"""Ajouter un élément à la liste :"""
ma_liste.append(6)
print(ma_liste)  # Affiche la liste avec le nouvel élément

"""Supprimer un élément de la liste :"""
ma_liste.remove(3)
print(ma_liste)  # Affiche la liste sans l'élément supprimé

"""Taille de la liste :"""
print(len(ma_liste))  # Affiche le nombre d'éléments dans la liste

"""pop() :"""
ma_liste.pop()  # Supprime le dernier élément de la liste
print(ma_liste)  # Affiche la liste sans le dernier élément

"""clear() :"""
ma_liste.clear()  # Supprime tous les éléments de la liste
print(ma_liste)  # Affiche la liste vide

"""Parcourir une liste :"""
for element in ma_liste:
    print(element)  # Affiche chaque élément de la liste