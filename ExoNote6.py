"""
Date: 2024/avr/08
Nom, Prénom: Da Silva Faria, Stennio
Matricule: 20270109
"""

import random
import functools

#Q1
def tabZero(n):
    #Réçoit un entier n et retourne un tableau de zéros de taille égal a n.

    tab = [0]*n
    return tab

def randomTab(n):
    # Réçoit un entier n et retourne un entier entre 1 et 10 (inclusif à gauche et à droite).

    return (int((random.random()*10))+1) + n

def tableauRandom(n):
    # Réçoit un entier n et retourne un tableau de nombres aléatoires entre 1 et 10 (inclusif à gauche et à droite)
    # de taille égal a n.

    tab = tabZero(n)
    return list(map(randomTab, tab))

#Q2
def lettreFiltre(tab):
    # Prends un tableau de textes comme paramètre
    # et retourne un tableau avec les éléments textes contenant uniquement des lettres.

    return list(filter(lambda l: l.isalpha(), tab))

#Q3
def tableauPairs(tab):
    # Prend un tableau d'entiers comme paramètre et retourne un tableau contenant tous les éléments pairs du tableau initial.
    return list(filter(lambda p: p%2 ==0, tab))

#Q4
def sommePuissances(tab):
    # Prend un paramètre, un tableau d'entiers et calcule la somme d'expressions 2**tab[i].
    # La fonction lambda p genère une liste de puissances,  functools.reduce retourne la somme des éléments de la liste.

    return functools.reduce(lambda x,y: x+y, list(map(lambda p: 2**p, tab)))

#Q5
def testerFonctions():
    ## Partie 1: Tests unitaires pour la fonction 2:
    #1a: tableau contenant uniquement des lettres
    assert lettreFiltre(['a', 'b', 'abc']) == ['a', 'b', 'abc']

    #1b: tableau contenant uniquement des charactères non-alphabétiques
    assert lettreFiltre(['1', '', '123', '-']) == []

    #1c: tableau contenant des charactères alphabetiques et non-alphabétiques:
    assert lettreFiltre(['a', 'abc', '1', '+', '@']) == ['a', 'abc']

    ## Partie 2: Tests unitaires pour la fonction 3:
    #2a: tableau contenant uniquement des pairs:
    assert tableauPairs([2,64,128]) == [2,64,128]

    #2b: tableau contenant uniquement non-pairs:
    assert tableauPairs([3,65,129]) == []

    #2c tableau contenant des pairs et des non-pairs:
    assert tableauPairs([2,3,64,65,128,129]) == [2,64,128]

    ## Partie 3: Tests unitaires pour la fonction 4:
    #3a: tableau contenant des entiers positifs:
    assert sommePuissances([2,3,4]) == 28

    #3b: tableau contenant des entiers négatifs:
    assert sommePuissances([-2,-3,-4]) == 0.4375

    #3c: tableau contenant des entiers positifs et négatifs:
    assert sommePuissances([-2, 3, 4]) == 24.25

testerFonctions()

## Impression des 3 résultats démandés:
#1 - Un tableau retourné par la fonction de la question 1:
print(tableauRandom(5))

#2 - Un tableau retourné par fonction de la question 3 avec un argument tableau retourné par fonction de la question 1:
print(tableauPairs(tableauRandom(5)))

#3 - La somme retournée par fonction de la question 4, calculée pour un tableau retourné par la fonction de la question 3,
# laquelle dans son tour, doit utiliser le tableau retourné par la fonction de la question 1:

print(sommePuissances(tableauPairs(tableauRandom(5))))