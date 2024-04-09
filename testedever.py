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

print(genererGrille())

