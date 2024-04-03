def init():
    global tour
    tour = 'x'
    for i in range(9):
        case(i).innerHTML = ''

def clic(index):
    global tour
    case(index).innerHTML = tour
    tour = 'o' if tour=='x' else 'x'

def element(id):
    return document.querySelector('#' + id)

def case(index):
    return element('case' + str(index))
