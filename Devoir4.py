## Nom, Prénom ; Date
# Da Silva Faria, Stennio; 2024/fev/14

## Commentaire général
# Programme pour calculer la date du dimanche de Pâques pour une année donné
# en la retournant comme texte sous forme JJ-MM-YYYY en utilisant l'algorithme de calcul
# du Jour de Pâques défini par le concile de Nicée en 325 après J.-C.

## Réponses aux 5 question de conception d'une foncion:
# Q1: Quelle est la tâche de la fonction:
# La fonction calcule la date du dimanche de Pâques pour une année donné
# en la retournant comme texte sous forme JJ-MM-YYYY en utilisant l'algorithme de calcul
# du Jour de Pâques défini par le concile de Nicée en 325 après J.-C.

# Q2: Quels sont les paramètres de la fonction et quels sont leurs types?
# Le paramètre formal de la fonction est annee, correspondant à l'année analysé. Son type est int

# Q3: Quel est le type du résultat?
# Format chaîne de caractères (string)

# Q4: Quel est le meilleur nom pour la fonction?
# calculation_easter_date

# Q5: Quels sont des exemples d'utilisation:
# Ex1: calculation_easter_date(2024) - calcule la date du dimanche de Pâques de l'année courrante
# output attendu: "31-03-2024"

# Ex2: calculation_easter_date(1789) - calcule la date du dimanche de Pâques de l'année de la prise de la Bastille
# output attendu: "08-04-1789"


## Calcul, commentaires détaillés nécessaires seulement

def calculation_easter_date(annee):
    temp1_g = annee % 19 # Calcul du "Nombre d'Or" (Golden Number), un cycle métonique de 19 ans
                         # représentant les phases de la lune.
    temp2_c= annee // 100 # Obtention du siècle de l'année.
    temp3_d = temp2_c - temp2_c // 4 # Calcul d'un ajustement basé sur le siècle pour tenir compte des années bissextiles.
    temp4_e = (8 * temp2_c + 13) // 25 # Calcul d'un ajustement lié au siècle.
    temp5_i = (19 * temp1_g + 15) % 30 # Calcul d'un élément lié au Nombre d'Or.
    temp6_h = (temp3_d - temp4_e + 19 * temp1_g + 15) % 30 # Calcul d'un autre élément lié au siècle.
    temp7_k = temp6_h // 28 # Calcul d'un facteur lié au calcul du mois.
    temp8_p = 29 // (temp6_h + 1) # Calcul d'un ajustement pour le mois.
    temp9_q = (21 - temp1_g) // 11 # Calcul d'un autre facteur lié au calcul du mois.
    temp5_i = temp6_h - temp7_k * (1 - temp7_k * temp8_p * temp9_q) # Réutilisation de la variable I pour un calcul additionnel lié au mois.
    temp10_j = (annee + annee // 4 + temp5_i + 2 - temp3_d) % 7 # Calcul du jour de la semaine de la date de Pâques.
    temp11_r = 28 + temp5_i - temp10_j # Calcul du jour du mois pour Pâques.

    if temp11_r > 31 and temp11_r < 41: # formatation des jours d'avril avec un seul charactère
        return "0" + str(temp11_r - 31) + '-04-' + str(annee)

    elif temp11_r >= 41: # formatation pour pâques en avril avec jours en deux chiffres
        return str(temp11_r - 31) + '-04-' + str(annee)

    else: # formatation pour pâques en mars
        return str(temp11_r) + '-03-' + str(annee)

## tests unitaires:
def test_calculation_easter_date():
    #1 cas général:
    assert calculation_easter_date(2024) == '31-03-2024'

    #2 la date la plus tôt possible : le 22 mars
    assert calculation_easter_date(1818) == '22-03-1818'

    #3 la date la plus tard possible : le 25 avril
    assert calculation_easter_date(1943) == '25-04-1943'

    #4 vérification si la correction pour les années bissextiles est correcte:
    assert calculation_easter_date(1900) == '15-04-1900'

    #5 vérifier si le nombre d'Or a été correctement calculé pour un cycle ménotique de 19 ans
    assert calculation_easter_date(2013) == '31-03-2013' and calculation_easter_date(2014) == '20-04-2014'

test_calculation_easter_date()
