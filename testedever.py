
def trouveGene(debut, fin):
    # Prend en paramètre un tableau contenant les positions de tous les codons de départ et un
    # autre tableau contenant les positions de tous les codons de terminaison pour un brin
    # d’ADN et renvoie un tableau de tuples contenant la liste des gènes (début et fin) trouvés
    # sur un brin.
    # Ainsi, s’il y a trois gènes sur un brin, le tableau renvoyé ressemblera à :
    # [ (debutGene1, finGene1) , (debutGene2, finGene2) ,
    # (debutGene3, finGene3) ]
    # FinGene doit être supérieur à debutGene et finGene doit être situé à un multiple
    # de trois nucléotides de debutGene.

    listeDeGenes = [] # Garde les tuples avec les positions de début et fin d'un gène
    genesTemp = [] # Garde temporairemente les positions de genes qui vont être convertis en tuple
    stopAnterieur = 0 # Garde la position du stop codon anterieur. l'ARN polymerase arrête la transcription après avoir
                      # rencontré un stop codon. Il faut donc rencontrer un nouvel codon "TAC" pour commencer une nouvelle
                      # transcription.

    for stop in fin: # Itération sur la liste des positions de stop codons

        for start in debut: # Itération sur la liste des positions de start codons

            if start > stopAnterieur and start < stop: # Vérif si la position de début d'un gène est entre deux stop codons

                if (stop - start) % 3 == 0:  # Vérif si la fin du gène se situe à un multiple de trois nucléotide du début

                    # Construction d'un tableau avec une position de start et une position de stop d'un gene
                    genesTemp.append(start)
                    genesTemp.append(stop)

                    # Conversion du tableau en tuple
                    listeDeGenes.append(tuple(genesTemp))

                    # Réinitialisation du tableau pour une nouvelle conversion en tuples
                    genesTemp = []

        stopAnterieur = stop

    return listeDeGenes

print(trouveGene([1, 5, 9], [ 11 ]))

def testTrouveGene():
    #1 un gène avec un start codon et un stop codon:
    assert trouveGene([1],[4]) == [(1,4)]

    #2 deux gènes avec le même stop codon:
    assert trouveGene([1,4], [7]) == [(1,7), (4,7)]

    #3 un gène entre deux stop codons:
    assert trouveGene([5], [2, 11]) == [(5,11)]
