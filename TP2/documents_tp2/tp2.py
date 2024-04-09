# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.

def table(contenu): return '<table>' + contenu + '</table>'
def tr(contenu): return '<tr>' + contenu + '</tr>'
def td(contenu): return '<td>' + contenu + '</td>'

def genererGrille():
    grille = document.querySelector("#t1")
    return "5"





def init():
    main = document.querySelector("#main")
    main.innerHTML = """
      <button class="hcentered" id="boutonNouvellePartie onclick="init()">Nouvelle partie</button>
      <p class="hcentered2"> Vous avez gagné</p>
      <p id="t1"></p>
      <div id="jeu" class="centered">   
      <img src="symboles/coste.svg" width="20" height="20">
      
      </div>""" + table('29')
