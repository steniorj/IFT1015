# Solution (codeBoot)

def premiers(n):  # retourne un tableau des n premiers nombres premiers
    resultat = [2]
    i = 3
    while len(resultat) < n:
        d = 2
        while d*d <= i:
            if i % d == 0:
                break
            d += 1
        else:
            resultat.append(i)
        i += 2
    return resultat

def table(contenu): return '<table>' + contenu + '</table>'
def tr(contenu): return '<tr>' + contenu + '</tr>'
def td(contenu): return '<td>' + contenu + '</td>'

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

def styler(n):
    s = str(n)
    if len(s) >= 2 and s[0] == s[-1]:
        return '<div style="background-color: lime">'+s+'</div>'
    else:
        return s

main = document.querySelector('#main')

main.innerHTML = """
<style>
#main table td { font-size: 20px; height: 30px; width: 50px; }
</style>""" + listeToTable(list(map(styler, premiers(500))), 10)