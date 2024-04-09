# Solution (codeBoot)

main = document.querySelector('#main')

mois = ['jan','feb','mar','apr','may','jun',
        'jul','aug','sep','oct','nov','dec']

def ol(contenu): return '<ol>' + contenu + '</ol>'
def li(contenu): return '<li>' + contenu + '</li>'

main.innerHTML = ol(''.join(list(map(li, mois))))

breakpoint()

def table(contenu): return '<table>' + contenu + '</table>'
def tr(contenu): return '<tr>' + contenu + '</tr>'
def td(contenu): return '<td>' + contenu + '</td>'

main.innerHTML = table(tr(''.join(list(map(td, mois)))))

breakpoint()

def grouper(lst, taille):  # taille = taille maximale des groupes
    groupes = []
    accum = []
    for elem in lst:
        accum.append(elem)
        if len(accum) == taille:
            groupes.append(accum)
            accum = []
    if len(accum) > 0:
        groupes.append(accum)
    return groupes

def trJoin(lst): return tr(''.join(lst))
def tableJoin(lst): return table(''.join(lst))

def listeToTable(lst, taille):
    return tableJoin(list(map(trJoin, grouper(list(map(td, lst)), taille))))

main.innerHTML = listeToTable(mois, 5)