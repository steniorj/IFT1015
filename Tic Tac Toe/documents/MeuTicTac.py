def init():
    global tour, occupees
    occupees = 0
    tour = 'x'
    for i in range(9):
        case(i).innerHTML = ''
    vencedor = document.querySelector('#vencedor')
    vencedor.innerHTML = ''

def clic(index):
    global tour, occupees


    if case(index).innerHTML == '':
        case(index).innerHTML = tour
        joueur = victoire()
        if joueur != '':
            sleep(0.1)
            vencedor = document.querySelector('#vencedor')
            vencedor.innerHTML = 'temos um vencedor'
            sleep(5)
            init()
        else:
            tour = 'o' if tour == 'x' else 'x'
            occupees += 1
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
            joueur = sym(pos)
            if joueur != '':
                for i in range(1,3):
                    if sym(pos+i*pas) != joueur:
                        break
                else:
                    return joueur
    return ''

def element(id):
    return document.querySelector("#" + id)

def case(index):
    return element('case' + str(index))