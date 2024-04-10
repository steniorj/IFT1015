"""
[x] gerar entre 15 e 20 posicoes randomicas com valor entre 0 e 99
[x] os valores nao podem estar em posições adjacentes

"""
import random
import math
def genererSous():
    # Retourne une liste de 15 à 20 éléments contenant un nombre entre 0 et 99, correspondant
    # aux positions où les sous seront plaés dans le tableau

    quantiteDeSous = int(15 + random.random() * 6) # Entre 15 et 20 cases auront un sous
    positionsDesSous = []
    nombreAleatoire = int(random.random()*1000//10) # Position où le sus sera mis

    for i in range(quantiteDeSous):

        # Éviter le même nombre plus d'une fois dans la liste et pièces en cases voisines
        while nombreAleatoire in positionsDesSous or \
                (nombreAleatoire-11) in positionsDesSous or \
                (nombreAleatoire-10) in positionsDesSous or \
                (nombreAleatoire-9) in positionsDesSous or \
                (nombreAleatoire-1) in positionsDesSous or \
                (nombreAleatoire+1) in positionsDesSous or \
                (nombreAleatoire+9) in positionsDesSous or \
                (nombreAleatoire+10) in positionsDesSous or \
                (nombreAleatoire+11) in positionsDesSous:
            nombreAleatoire = random.randint(0,99)

        positionsDesSous.append(nombreAleatoire)

    return positionsDesSous

print(len(genererSous()))

