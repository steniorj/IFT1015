
def init():
    global tour, grille, occupees, coups

    tour = 1
    grille = [0] * 9
    occupees = 0
    coups = []

    for i in range(9):
        case(i).innerHTML = ''

    activer('redo', False)
    activer('undo', False)

def clic(index):
    global tour, occupees, coups, gri, coupvar, occupeesvar

    if grille[index] == 0:

        grille[index] = tour
        case(index).innerHTML = symboleJoueur(tour) # recebe símbolo: X ou O

        coups = coups[:occupees] #FÇ undo e redo. Pega o array do início até a jogada atual, apagando as jogadas que foram desfeitas
        coups.append(index) #Adição ao array

        activer('undo', True) # Ativa a fç undo a cada clic
        activer('redo', False) # Uma ez efetuada a jogada, a árvore muda e não é mais possível refazer a jogada

        gagnant = victoire()

        #prints
        print(grille)
        gri = document.querySelector('#' + 'grille')
        gri.innerHTML = 'var grille: ' + str(grille.copy())

        coupvar = document.querySelector('#coups')
        coupvar.innerHTML = 'var coups: ' + str(coups.copy())

        occupeesvar = document.querySelector('#occupees')
        #/prints

        if gagnant != 0:
            sleep(0.1)
            alert(nomJoueur(gagnant) + ' est le gagnant!')
            init()
        else:
            tour = autreJoueur(tour)
            occupees += 1

            occupeesvar.innerHTML = 'var occupees: ' + str(occupees)
            if occupees == 9:
                sleep(0.1)
                alert('match nul')
                init()

def sym(index):
    return case(index).innerHTML

alignements = [struct(pas=+1, departs=[0, 3, 6]),
               struct(pas=+3, departs=[0, 1, 2]),
               struct(pas=+4, departs=[0]),
               struct(pas=-2, departs=[6])]
def victoire():

    for alignement in alignements:

        pas = alignement.pas

        for pos in alignement.departs:
            joueur = grille[pos]
            if joueur != 0:
                for i in range(1,3):
                    if grille[pos+i*pas] != joueur:
                        break
                else:
                    return joueur
    return 0

def activer(id, oui):
    if oui:
        element(id).removeAttribute('disabled')
    else:
        element(id).setAttribute('disabled', 'true')

def element(id):
    return document.querySelector('#' + id)

def case(index):
    return element('case' + str(index))

def symboleJoueur(joueur):
    if joueur == 1:
        return '<img src="https://cdn-icons-png.flaticon.com/512/235/235392.png">'
    else:
        return '<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBB_9q2vcdjAJDLqIB4yNoQNJk63kxTLJSNG0w8SFJwg&s">'

def nomJoueur(joueur): # guarda o símbolo d jogador atual
    return 'x' if joueur == 1 else 'o'

def autreJoueur(joueur): # passa pra o próximo jogador
    return 3-joueur

def undo(): #limpa a grille e o tabuleiro, diminui o contador de casas ocupadas mas mantem a lista das posiçoes das jogadas (coup)
    global occupees, tour, gri, coupvar, occupeesvar

    if occupees > 0:
        occupees -= 1 # diminui em um o numero de casas ocupadas
        grille[coups[occupees]] = 0 # remove a última jogada do array que representa o tabuleiro
        case(coups[occupees]).innerHTML = '' # esvazia a última casa ocupada no tabuleiro
        tour = autreJoueur(tour) #retorna para o jogador anterior
        if occupees == 0:
            activer('undo', False)
        activer('redo', True)

def redo():
    global occupees, tour, gri, coupvar, occupeesvar
    if occupees < len(coups): #verif se o no de jogadas é maior que o numero de casa ocupadas de fato, ou seja, foi feito um undo
        grille[coups[occupees]] = tour # busca o ultimo valor da lista de jogadas (coup) e registra na lista do tabuleiro
        case(coups[occupees]).innerHTML = symboleJoueur(tour) # registra o simbolo do jogador no tabuleiro
        occupees += 1
        tour = autreJoueur(tour) #proximo jogador
        if occupees == len(coups):
            activer('redo', False)
        activer('undo', True)
