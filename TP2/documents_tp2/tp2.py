# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.

"""

[x] fazer generersous() rodar sem bugar - só pode usar random.random()
[x] colocar os sous na lista da grille
[x] criar contador de moedas no código e mostrar na página
[x] criar contador de erros
[x] mostrar contador de erros na pagina
[x] criar contador de moedas descobertas
[x] criar checagem de vitoria

caso jogada numa casa com moeda:
[x] ajustar função clic para mostrar a moeda somente se a casa na grille contiver uma moeda
[x] modificar contador de moedas achadas
[x] checar condicoes de vitoria

caso jogada numa casa sem moeda:
[x] ajustar fç clic para diminuir numero de jogadas
[x] checar derrota
    em caso de derrota:
    [x]mostrar mensagem
    [x] reiniciar jogo
    [x] sleep 10
    [x] init()

[x] ajustar inicializacao para mostrar numeros de moedas adjacentes para cada casa
    [x] criar check para casas da esquerda
    [x] criar check para casas da direita
    [x] criar check para casas de cima
    [x] criar check para casas de baixo
    [x] criar check para casas dos cantos
    [x] criar check para casas do centro

"""
import random
import functools


def genererSous():
    # Retourne une liste de 15 à 20 éléments contenant un nombre entre 0 et 99, correspondant
    # aux positions où les sous seront plaés dans le tableau

    global quantiteDeSous

    quantiteDeSous = int(15 + random.random() * 6)  # Entre 15 et 20 cases auront un sous
    positionsDesSous = []
    nombreAleatoire = int(random.random() * 1000 // 10)  # Position où le sous sera mis

    for i in range(quantiteDeSous):

        # Éviter le même nombre plus d'une fois dans la liste et pièces en cases voisines
        while ((nombreAleatoire in positionsDesSous) or
               ((nombreAleatoire - 11) in positionsDesSous) or
               ((nombreAleatoire - 10) in positionsDesSous) or
               ((nombreAleatoire - 9) in positionsDesSous) or
               ((nombreAleatoire - 1) in positionsDesSous) or
               ((nombreAleatoire + 1) in positionsDesSous) or
               ((nombreAleatoire + 9) in positionsDesSous) or
               ((nombreAleatoire + 10) in positionsDesSous) or
               ((nombreAleatoire + 11) in positionsDesSous)):
            nombreAleatoire = int(random.random() * 1000 // 10)

        positionsDesSous.append(nombreAleatoire)

    return positionsDesSous

def grilleAvecSous(tab):
    # Réçoit la grille vide et substitue 15-20 cases par 'P', qui symbolize une pièce.

    sous = genererSous()
    tableau = tab
    for i in sous:
        tableau[i] = 'P'
    return tableau

def init():
    global grille, quantiteDeSous, nombreDerreurs, monnaiesTrouves, sousCaches, erreurs, piecesAdjacents

    main = document.querySelector("#main")

    main.innerHTML = ("""
      <button class="hcentered" id="boutonNouvellePartie" onclick="init()">Nouvelle partie</button>
      <p id="header" class="hcentered2" style="font-size: 24px;"> <b> Jouer! </b> </p>
      <p id="nombreDerreurs" class="gauche"></p>
      <p id="sousCaches" class= "droite"></p>
      <div id="jeu" class="centered">   
      """ + genererCarte() + """ 
      </div>
      <img src="symboles/coste.svg" width="40" height="40" class="droite" hidden>
      """)

    grille = [0]*100
    grille = grilleAvecSous(grille)

    nombreDerreurs = 0
    erreurs = document.querySelector('#nombreDerreurs')
    erreurs.innerHTML = 'Erreurs: ' + str(nombreDerreurs)

    monnaiesTrouves = 0

    sousCaches = document.querySelector('#sousCaches')
    sousCaches.innerHTML = 'Nombre des sous:' + str(quantiteDeSous - monnaiesTrouves)

    piecesAdjacents = 0

    #affichage
    gri = document.querySelector('#' + 'grille')
    gri.innerHTML = 'var grille: ' + str(grille.copy())

    for i in range(100): # Rédemarrage du grille
        case(i).innerHTML = str(i)

        if (i in [10,20,30,40,50,60,70,80]) and (grille[i] != "P"):
            for j in [-10,-9,1,10,11]:
                if grille[i+j] == 'P':
                    piecesAdjacents += 1
            case(i).innerHTML = str(piecesAdjacents)
            piecesAdjacents = 0

        if (i in [19,29,39,49,59,69,79,89]) and (grille[i] != "P"):
            for j in [-10,-11,-1,9,10]:
                if grille[i+j] == 'P':
                    piecesAdjacents += 1
            case(i).innerHTML = str(piecesAdjacents)
            piecesAdjacents = 0

        if (i in [1,2,3,4,5,6,7,8]) and (grille[i] != "P"):
            for j in [-1,9,10,11,1]:
                if grille[i+j] == 'P':
                    piecesAdjacents += 1
            case(i).innerHTML = str(piecesAdjacents)
            piecesAdjacents = 0

        if (i in [91,92,93,94,95,96,97,98]) and (grille[i] != "P"):
            for j in [-1,-11,-10,-9,1]:
                if grille[i+j] == 'P':
                    piecesAdjacents += 1
            case(i).innerHTML = str(piecesAdjacents)
            piecesAdjacents = 0

        if (i in [0]) and (grille[i] != "P"):
            for j in [1,10,11]:
                if grille[i+j] == 'P':
                    piecesAdjacents += 1
            case(i).innerHTML = str(piecesAdjacents)
            piecesAdjacents = 0

        if (i in [9]) and (grille[i] != "P"):
            for j in [-1,9,10]:
                if grille[i+j] == 'P':
                    piecesAdjacents += 1
            case(i).innerHTML = str(piecesAdjacents)
            piecesAdjacents = 0

        if (i in [90]) and (grille[i] != "P"):
            for j in [-10,-9,1]:
                if grille[i+j] == 'P':
                    piecesAdjacents += 1
            case(i).innerHTML = str(piecesAdjacents)
            piecesAdjacents = 0

        if (i in [99]) and (grille[i] != "P"):
            for j in [-1,-10,-11]:
                if grille[i+j] == 'P':
                    piecesAdjacents += 1
            case(i).innerHTML = str(piecesAdjacents)
            piecesAdjacents = 0

        for k in range(1,9):
            if k*10 <= i <= k*10+8 and (grille[i] != "P"):
                for j in [-11,-10,-9,-1,1,9,10,11]:
                    if grille[i+j] == 'P':
                        piecesAdjacents += 1
                case(i).innerHTML = str(piecesAdjacents)
                piecesAdjacents = 0

        if (grille[i] == 'P') or case(i).innerHTML == str(0):
            case(i).innerHTML = ''

def table(contenu): return '<table>' + contenu + '</table>'
def tr(contenu): return '<tr>' + contenu + '</tr>'
def td(contenu): return '<td id="case' + str(contenu) + '" onclick="clic(' + str(contenu) + ')"></td>'

def genererCarte():
    grille = ''
    for i in range(0,10):
        temp = ''
        for j in range(0,10):
                index  = i*10+j
                temp += td(index)
        grille += tr(temp)

    return table(grille)

def clic(index):
    global grille, monnaiesTrouves, sousCaches, quantiteDeSous, msgVictoire, nombreDerreurs, erreurs

    # Si la case a une monnaie caché
    if grille[index] == "P":
        case(index).innerHTML = '<img src="symboles/coste.svg" width="20" height="20">'
        monnaiesTrouves += 1
        sousCaches.innerHTML = 'Nombre des sous:' + str(quantiteDeSous - monnaiesTrouves)

        # Victoire
        if monnaiesTrouves == quantiteDeSous:
            msgVictoire = document.querySelector('#header')
            msgVictoire.innerHTML = 'Vous avez gagné!'
            sleep(10)
            init()

    # Si la case n'a pas une monnaie
    if grille[index] == 0:
        grille[index] = 1
        nombreDerreurs +=1
        erreurs = document.querySelector('#nombreDerreurs')
        erreurs.innerHTML = 'Erreurs: ' + str(nombreDerreurs)

        # Défaite
        if nombreDerreurs > 3:
            msgDefaite = document.querySelector('#header')
            msgDefaite.innerHTML = 'Vous avez perdu!'
            sleep(10)
            init()

    #affichage
    gri = document.querySelector('#' + 'grille')
    gri.innerHTML = 'var grille: ' + str(grille.copy())

def element(id):
    return document.querySelector('#' + id)

def case(index):
    return element('case' + str(index))