def table(contenu): return '<table>' + contenu + '</table>'
def tr(contenu): return '<tr>' + contenu + '</tr>'
def td(contenu): return '<td id="case' + str(contenu) + '" onclick="clic(' + str(contenu) + ')">'+ str(contenu) +'</td>'

def genererGrille():
    grille = ''
    for i in range(0,10):
        grille += td(i)
    return grille

print(genererGrille())