# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.
import random
import functools
def table(contenu): return '<table>' + contenu + '</table>'
def tr(contenu): return '<tr>' + contenu + '</tr>'
def td(contenu): return '<td id="case' + str(contenu) + '" onclick = "clic' + str(contenu) + '">'+ str(contenu) +'</td>'

def clic():
    return
def genererGrille():
    grille = ''
    for i in range(0,10):
        grille += td(i)
    return grille
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

def init():
    main = document.querySelector("#main")
    main.innerHTML = """
      <button class="hcentered" id="boutonNouvellePartie onclick="init()">Nouvelle partie</button>
      <p class="hcentered2"> Vous avez gagné</p>
      <p id="t1"></p>
      <div id="jeu" class="centered">   
      <img src="symboles/coste.svg" width="40" height="40">
      
      </div>""" + genererGrille()
