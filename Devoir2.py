## Da Silva Faria, Stennio ; 2024/01/30

## Programme pour calculer les solutions des polynômes du deuxième degré qui peuvent avoir 2, 1 ou
# ne pas avoir des solutions réelles.

## Déclaration des variables globales, constantes
# Donnée que:
# 1 - tels polynomes sont décrits par l'équations générale ax**2 + bx + c = 0 ;
# 2 - La formule utilisée pour calculer les solutions sera: x = ( -b +-((b**2 - 4*a*c) ** (1/2) ) / (2*a) ;

# Les variables seront nommés:
# a: l'indice a du terme ax**2
# b: l'indice b du terme bx
# c: terme c
# x_Sqrt_Positif: garde le calcul en considerant la solution positive de la racine carrée de l'équation
# x_Sqrt_Negatif: garde le calcul en considerant la solution négative de la racine carrée de l'équation
# racine_Carree:  la valeur qui sera utilisée pour calculer la racine carrée
# probleme: affectation des variables a, b, c, selon la question posée

## Calcul, commentaires détaillés nécessaires seulement
probleme = 1
while probleme < 4:
    if probleme == 1:
        a = 2
        b = 5
        c = 2
    elif probleme == 2:
        a = 1
        b = 2
        c = 1
    elif probleme == 3:
        a = 2
        b = 2
        c = 2

    racine_Carree = (b ** 2 - 4 * a * c)

    # Output si le polynome n'a pas des racines réelles

    if racine_Carree < 0:
        print("Il n'y a pas des solutions réelles pour le polynome", str(a) + "x**2 +", str(b) + "x +", c)
        probleme += 1

    # Output si le polynome a des racines réelles

    else:

        x_Sqrt_Positif = (-b + (racine_Carree ** (1 / 2))) / (2 * a)
        x_Sqrt_Negatif = (-b - (racine_Carree ** (1 / 2))) / (2 * a)

        if x_Sqrt_Positif == x_Sqrt_Negatif:  # Output pour une solution réelle.
            print('Pour le polynome', str(a) + 'x**2 +', str(b) + 'x +', c, 'la seule solution est', x_Sqrt_Positif)
            probleme += 1

        else:  # Output pout deux solutions réelles
            print('Pour le polynome', str(a) + 'x**2 +', str(b) + 'x +', c, 'les solutions sont', x_Sqrt_Positif, 'et',
                  x_Sqrt_Negatif)
            probleme += 1
