# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.

"""
[] colocar os sous na lista da grille
[] criar contador de moedas na grille
[] criar contador de moedas descobertas
[] criar contador de jogadas
[] criar checagem de vitoria

caso jogada numa casa com moeda:
[] ajustar função clic para mostrar a moeda somente se a casa na grille contiver uma moeda
[] modificar contador de moedas achadas
[] checar condicoes de vitoria

caso jogada numa casa sem moeda:
[] ajustar função clic para mostrar numeros de moedas adjacentes
[] ajustar fç clic para diminuir numero de jogadas
[] checar derrota
    em caso de derrota:
    []mostrar mensagem
    [] reiniciar jogo
    []verificar pdf se há algo mais a fazer

em caso de vitoria:
[] seguir o que é descrito no pdf



"""
import random
import functools


def genererSous():
    # Retourne une liste de 15 à 20 éléments contenant un nombre entre 0 et 99, correspondant
    # aux positions où les sous seront placés dans le tableau

    quantiteDeSous = random.randint(15, 20)  # Entre 15 et 20 cases auront un sous
    positionsDesSous = []
    nombreAleatoire = random.randint(0, 99)  # Position où le sus sera mis

    for i in range(quantiteDeSous):

        # Éviter le même nombre plus d'une fois dans la liste et pièces en cases voisines
        while nombreAleatoire in positionsDesSous or (nombreAleatoire - 11) in positionsDesSous or (nombreAleatoire - 10) in positionsDesSous or (nombreAleatoire - 9) in positionsDesSous or (nombreAleatoire - 1) in positionsDesSous or (nombreAleatoire + 1) in positionsDesSous or (nombreAleatoire + 9) in positionsDesSous or (nombreAleatoire + 10) in positionsDesSous or (nombreAleatoire + 11) in positionsDesSous:
            nombreAleatoire = random.randint(0, 99)

        positionsDesSous.append(nombreAleatoire)

    return positionsDesSous

def init():
    global grille
    main = document.querySelector("#main")

    main.innerHTML = ("""
      <button class="hcentered" id="boutonNouvellePartie" onclick="init()">Nouvelle partie</button>
      <p hidden="hidden" class="hcentered2"> Vous avez gagné</p>
      
      <div id="jeu" class="centered">   
      """ + genererGrille() + """ 
      </div>
      <img src="symboles/coste.svg" width="40" height="40">
      """)

    grille = [0] * 100

    #affichage
    gri = document.querySelector('#' + 'grille')
    gri.innerHTML = 'var grille: ' + str(grille.copy())

    for i in range(100): # Nettoyage du grille
        case(i).innerHTML = str(i)


def table(contenu): return '<table>' + contenu + '</table>'
def tr(contenu): return '<tr>' + contenu + '</tr>'
def td(contenu): return '<td id="case' + str(contenu) + '" onclick="clic(' + str(contenu) + ')">'+ str(contenu) +'</td>'

def genererGrille():
    grille = ''
    for i in range(0,10):
        temp = ''
        for j in range(0,10):
                index  = i*10+j
                temp += td(index)
        grille += tr(temp)

    return table(grille)
    # nombrePieces = math.floor(random.random()*5) + 15
    #
    # returnValue = ''
    # for i in range(0,10):
    #     temp = ''
    #     for j in range(0,10):
    #         index = i*10 + j
    #
    #         temp = td("<div><p>P" + str(index) + "</p></div>")
    #     returnValue += tr(temp)
    #
    # return table(returnValue) + str(nombrePieces)

    #grille = ''
    #grille = <td id="case0" onclick="clic(0)"></td>
    #return grille

def clic(index):
    global grille
    case(index).innerHTML = '<img src="symboles/coste.svg" width="20" height="20">'

    if grille[index] == 0:
        grille[index] = 1
    #affichage
    gri = document.querySelector('#' + 'grille')
    gri.innerHTML = 'var grille: ' + str(grille.copy())

def element(id):
    return document.querySelector('#' + id)

def case(index):
    return element('case' + str(index))

