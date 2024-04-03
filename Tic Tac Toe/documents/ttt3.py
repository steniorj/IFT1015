def init():
    global tour
    tour = 'x'
    for i in range(9):
        case(i).innerHTML = ''

def clic(index):
    global tour
    if case(index).innerHTML == '':
        case(index).innerHTML = tour
        joueur = victoire()
        if joueur != '':
            alert(joueur + ' a gagné')
            init()
        else:
            tour = 'o' if tour=='x' else 'x'

def element(id):
    return document.querySelector('#' + id)

def case(index):
    return element('case' + str(index))

def sym(index):
    return case(index).innerHTML

alignements = [struct(pas= +1, departs= [0,3,6]),
               struct(pas= +3, departs= [0,1,2]),
               struct(pas= +4, departs= [0]),
               struct(pas= -2, departs= [6])]

def victoire():

    for alignement in alignements:

        pas = alignement.pas

        for pos in alignement.departs:
            joueur = sym(pos)
            if joueur != '':
                for i in range(1, 3):
                    if sym(pos+i*pas) != joueur:
                        break
                else:
                    return joueur  # il y a un gagnant

    return ''  # pas de gagnant
