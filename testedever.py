
codons_aa = {
    "UUU": "Phénylalanine",
    "UUC": "Phénylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "CUU": "Leucine",
    "CUC": "Leucine",
    "CUA": "Leucine",
    "CUG": "Leucine",
    "AUU": "Isoleucine",
    "AUC": "Isoleucine",
    "AUA": "Isoleucine",
    "AUG": "Méthionine (Start)",
    "GUU": "Valine",
    "GUC": "Valine",
    "GUA": "Valine",
    "GUG": "Valine",
    "UCU": "Sérine",
    "UCC": "Sérine",
    "UCA": "Sérine",
    "UCG": "Sérine",
    "CCU": "Proline",
    "CCC": "Proline",
    "CCA": "Proline",
    "CCG": "Proline",
    "ACU": "Thrénine",
    "ACC": "Thrénine",
    "ACA": "Thrénine",
    "ACG": "Thrénine",
    "GCU": "Alanine",
    "GCC": "Alanine",
    "GCA": "Alanine",
    "GCG": "Alanine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UAA": "Stop",
    "UAG": "Stop",
    "CAU": "Histidine",
    "CAC": "Histidine",
    "CAA": "Glutamine",
    "CAG": "Glutamine",
    "AAU": "Asparagine",
    "AAC": "Asparagine",
    "AAA": "Lysine",
    "AAG": "Lysine",
    "GAU": "Aspartate",
    "GAC": "Aspartate",
    "GAA": "Glutamate",
    "GAG": "Glutamate",
    "UGU": "Cystéine",
    "UGC": "Cystéine",
    "UGA": "Stop",
    "UGG": "Tryptophane",
    "CGU": "Arginine",
    "CGC": "Arginine",
    "CGA": "Arginine",
    "CGG": "Arginine",
    "AGU": "Sérine",
    "AGC": "Sérine",
    "AGA": "Arginine",
    "AGG": "Arginine",
    "GGU": "Glycine",
    "GGC": "Glycine",
    "GGA": "Glycine",
    "GGG": "Glycine"}

lettreAa = {
    "UUU": "F",
    "UUC": "F",
    "UUA": "L",
    "UUG": "L",
    "CUU": "L",
    "CUC": "L",
    "CUA": "L",
    "CUG": "L",
    "AUU": "I",
    "AUC": "I",
    "AUA": "I",
    "AUG": "M",
    "GUU": "V",
    "GUC": "V",
    "GUA": "V",
    "GUG": "V",
    "UCU": "S",
    "UCC": "S",
    "UCA": "S",
    "UCG": "S",
    "CCU": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "ACU": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "GCU": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "UAU": "Y",
    "UAC": "Y",
    "UAA": "*",
    "UAG": "*",
    "CAU": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "AAU": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "GAU": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "UGU": "C",
    "UGC": "C",
    "UGA": "*",
    "UGG": "W",
    "CGU": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "AGU": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GGU": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G"
}

# Utilisé pour la construction du brin d'ADN complementaire dans la fonction "antisens"
adnAppariement = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

# Utilisé pour faire la conversion d'ADN en ARN dans la fonction "transcrire"
adnTranscriptionDictionnaire = {
    "A": "U",
    "T": "A",
    "C": "G",
    "G": "C"
}

startCodonPos = [38, 74, 402]
stopCodonPos = [3, 9, 154, 160, 226, 249, 283, 304, 311, 343, 379, 392, 437, 460, 466, 494, 517, 556, 592, 614, 650, 673, 679, 720]

# stop codons:
# total [3, 9, 154, 160, 226, 249, 283, 304, 311, 343, 379, 392, 437, 460, 466, 494, 517, 556, 592, 614, 650, 673, 679, 720]
# ATT:  [226, 283, 343, 379, 437, 494, 556, 592, 614, 650]
# ATC:  [9, 160, 392, 466, 679, 720]
# ACT:  [3, 154, 249, 304, 311, 460, 517, 673]

adn = "TCGACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGATACCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATACCCAGCCAGCCAGCCAGCGACG\
GCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGAGTGCCAGCCAGCCAGCCAGCGAACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGAATGCCAGCCAGC\
CAGCCAGCGAAGCCAGCCAGCCGATATTCAGCCAGCCAGCCAGCGAACACTCTTCGACAGCCAGCGAAGCCAGCCAGCCGATATTCAGCCAGCCAGCCAGCGA\
ACTCGACACTCTTCGACAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCATCCCAGCGATACCC\
AGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGCGAACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAG\
CCAGCGAACTCGTCTGCGTTCGACAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGC\
GATTGCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGCGAACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGTATGCCAGCC\
AGCATCCCAGCGA"
################# FITA NEGATIVA

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
    genesTemp = [] # Garde temporairemente les positions des codons qui vont être convertis en tuple
    stopAnterieur = 0 # Garde la position du stop codon anterieur. l'ARN polymerase arrête la transcription après avoir
                      # rencontré un stop codon. Pour trouver le prochain gène il est donc nécéssaire rencontrer un nouvel codon "TAC" pour commencer une nouvelle
                      # transcription.
    stopFlag = False # Signale q'une tuple valide a été trouvé. Le prochain gène a un start codon situé après le stop codon courant

    for stopPos in fin:
        for startPos in debut:
            if startPos < stopPos:
                if stopAnterieur < startPos: # Vérif. si le start codon analysé est après le dernier stop codon
                    if (stopPos - startPos) % 3 == 0: # Vérif. si les positions de fin et début sont multiples de 3

                        genesTemp.append(startPos)
                        genesTemp.append(stopPos)

                        # Conversion en tuple et addition au tableau final
                        listeDeGenes.append(tuple(genesTemp))

                        # Réinitialisation du tableau pour une nouvelle conversion en tuples
                        genesTemp = []


                        # Activation du flag
                        stopFlag = True

        if startPos > stopPos and stopFlag == True: # Tous les start codons valides pour ce stop codon ont été enregistrés

            stopAnterieur = stopPos # Permettre que la recherche du prochain start codon soit faite après le dernier stop codon

            stopFlag = False # Réinitialiation du flag

    return listeDeGenes

genesBrinPositif = trouveGene([38, 74, 402],[3, 9, 154, 160, 226, 249, 283, 304, 311, 343, 379, 392, 437, 460, 466, 494, 517, 556, 592, 614, 650, 673, 679, 720])

##
def genesEnChaine(debut,fin,sequence):
    # Prend en paramètre les positions de début et fin d'un gene et une séquence d'adn,
    # en renvoyant la chaîne de caractères correspondant

    sousChaineEnADN = sequence[debut:fin+3]

    return sousChaineEnADN

def testGenesEnChaine():
    #1 cas général:
    assert genesEnChaine(0,5,"AAA--TTT----") == "AAA--TTT"

def transcrire(brinAdn):
    # Prend en paramètre la sous-chaine de caractère du brin d’ADN débutant au début du gène
    # et se terminant à la fin du gène et renvoie le brin d’ARN correspondant sous forme d’une
    # chaine de caractères.
    arnTranscrit = ''
    for i in brinAdn:
        arnTranscrit += adnTranscriptionDictionnaire[i]
    return arnTranscrit

gene1AdnBrinPositif = genesEnChaine(genesBrinPositif[0][0],genesBrinPositif[0][1],adn)
gene2AdnBrinPositif = genesEnChaine(genesBrinPositif[1][0],genesBrinPositif[1][1],adn)
gene3AdnBrinPositif = genesEnChaine(genesBrinPositif[2][0],genesBrinPositif[2][1],adn)

gene1ArnBrinPositif = transcrire(gene1AdnBrinPositif)
gene2ArnBrinPositif = transcrire(gene2AdnBrinPositif)
gene3ArnBrinPositif = transcrire(gene3AdnBrinPositif)

print(genesBrinPositif[0][0],genesBrinPositif[0][1])
print(genesBrinPositif[1][0],genesBrinPositif[1][1])
print(genesBrinPositif[2][0],genesBrinPositif[2][1])

print(gene1AdnBrinPositif)
print(gene2AdnBrinPositif)
print(gene3AdnBrinPositif)



def testTrouveGene():
    # 1 un gène avec un start codon et un stop codon:
    assert trouveGene([1], [4]) == [(1, 4)]

    # 2 deux gènes avec le même stop codon:
    assert trouveGene([1, 4], [7]) == [(1, 7), (4, 7)]

    # 3 un gène entre deux stop codons:
    assert trouveGene([5], [2, 11]) == [(5, 11)]

testTrouveGene()

# Utilisé pour la construction du brin d'ADN complementaire dans la fonction "antisens"
adnAppariement = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

# Utilisé pour faire la conversion d'ADN en ARN dans la fonction "transcrire"
adnTranscriptionDictionnaire = {
    "A": "U",
    "T": "A",
    "C": "G",
    "G": "C"
}


## <- indique le début d'un pair fonction et son test respectif
def antisens(brinAdn):
    # Part de brin ADN fourni et renvoie le brin d’ADN complémentaire.
    adnAntisens = ''
    for i in brinAdn:
        adnAntisens += adnAppariement[i]
    return adnAntisens




def testAntisens():
    # 1 cas géneral:
    assert antisens("AAATTTCCCGGG") == "TTTAAAGGGCCC"


##
def reverseComplement(brinAdn):
    # Inversion du brin complémentaire d'ADN pour qu'il soit affiché dans le sense 5' -> 3'
    brinAdn = antisens(brinAdn)  # Obtention du brin complémentaire d'ADN

    adnBrinReverseComplement = ''  # Variable pour garder l'output

    for i in str(brinAdn[len(brinAdn)::-1]):
        adnBrinReverseComplement += i

    return adnBrinReverseComplement

# print(reverseComplement(adn))
adnReverseComplement = "TCGCTGGGATGCTGGCTGGCATACGGCTGGCTGGCTTCGCTGGCTGTCGATCGCAGTTCGCTGGCTGGCTGGCTG\
GCAATCGGCTGGCTGGCTTCGCTGGCTGGCTGGCTGGCAATCGCTGGCTGGCTGGCTGGCAATCGGCTGGCTGGCTTCGCTGGCTGGCTGGCTGGCAAT\
CGGCTGGCTGGCTTCGCTGGCTGTCGAACGCAGACGAGTTCGCTGGCTGGCTGGCTGGCAATCGGCTGGCTGGCTTCGCTGGCTGTCGATCGCAGTTCG\
CTGGCTGGCTGGCTGGCAATCGGCTGGCTGGCTTCGCTGGCTGGCTGGCTGGGTATCGCTGGGATGCTGGCTGGCAATCGGCTGGCTGGCTTCGCTGGC\
TGGCTGGCTGGCAATCGGCTGGCTGGCTTCGCTGGCTGTCGAAGAGTGTCGAGTTCGCTGGCTGGCTGGCTGAATATCGGCTGGCTGGCTTCGCTGGCT\
GTCGAAGAGTGTTCGCTGGCTGGCTGGCTGAATATCGGCTGGCTGGCTTCGCTGGCTGGCTGGCTGGCATTCGGCTGGCTGGCTTCGCTGGCTGTCGAT\
CGCAGTTCGCTGGCTGGCTGGCTGGCACTCGGCTGGCTGGCTTCGCTGGCTGGCTGGCTGGCCGTCGCTGGCTGGCTGGCTGGGTATCGGCTGGCTGGC\
TTCGCTGGCTGGCTGGCTGGGTATCGGCTGGCTGGCTTCGCTGGCTGTCGATCGCAGTCGA"

# print(trouveDebut(adnReverseComplement))
# print(trouveFin(adnReverseComplement))
"""
Start:TAC
STOP: ATT, ATC, ACT"""
#startCodonPos = [21]
#stop codons:
#total [49, 78, 114, 136, 172, 234, 262, 291, 327, 349, 385, 447, 504, 539, 568, 596, 655, 691, 719]
# ATT:
# ATC:
# ACT:

    pu()
    bk(10)
    rt(90)
    bk(10)
    lt(90)
    pd()