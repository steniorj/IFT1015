## Nom, Prénom ; Date
# Da Silva Faria, Stennio; 2024/02/14

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
# le paramètre formal de la fonction est annee, correspondant à l'année analysé
# son type est int

# Q3: Quel est le type du résultat?
# format texte (string)

# Q4: Quel est le meilleur nom pour la fonction?
# calculation_easter_date

# Q5: Quels sont des exemples d'utilisation:
# Ex1: calculation_easter_date(2024) - calcule la date du dimanche de Pâques de l'année courrante
# Ex2: calculation_easter_date(325) - calcule la date du dimanche de Pâques de l'année du concile de Nicée

## Calcul, commentaires détaillés nécessaires seulement

def calculation_easter_date(annee):

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
    assert calculation_easter_date(2013) == '31-03-2013' and funcao_fdp(2014) == '20-04-2014'

test_calculation_easter_date()

# Après avoir terminé votre code, renommez votre fichier en fonction de la
# nature de calcul effectué dans votre programme.