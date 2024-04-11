p = ''

for rangee in range(1,9):
    for colomne in range(1,9):
        if (grille[rangee*10 + colomne] != "P"):
            for j in [-11,-10,-9,-1,1,9,10,11]:
                if grille[(rangee*10 + colomne)+j] == 'P':
                    piecesAdjacents += 1
            p = str(piecesAdjacents)
            piecesAdjacents = 0

print(p)