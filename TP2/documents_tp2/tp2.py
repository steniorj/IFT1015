# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.
#proximo passo: usar random pra gerar as moedas e incorporá-las na var grille com o valor 'P'
import random
import functools
def teste():
    for i in range(100):
        case(i).innerHTML = '2'

def init():
    global grille
    main = document.querySelector("#main")

    main.innerHTML = ("""
      <button class="hcentered" id="boutonNouvellePartie" onclick="init()">Nouvelle partie</button>
      <p hidden="hidden" class="hcentered2"> Vous avez gagné</p>
      
      <div id="jeu" class="centered">   
      """ +  genererGrille() + """ 
      </div>
      <img src="symboles/coste.svg" width="40" height="40">
      """)

    grille = [0] * 100

    #affichage
    gri = document.querySelector('#' + 'grille')
    gri.innerHTML = 'var grille: ' + str(grille.copy())

    for i in range(100): # Nettoyage du grille
        case(i).innerHTML = ''


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

