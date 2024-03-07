#"ATT, ATC, ACT" - stop codons

"TCGACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGATACCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATACCCAGCCAGCCAGCCAGCGACG\
GCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGAGTGCCAGCCAGCCAGCCAGCGAACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGAATGCCAGCCAGC\
CAGCCAGCGAAGCCAGCCAGCCGATATTCAGCCAGCCAGCCAGCGAACACTCTTCGACAGCCAGCGAAGCCAGCCAGCCGATATTCAGCCAGCCAGCCAGCGA\
ACTCGACACTCTTCGACAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCATCCCAGCGATACCC\
AGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGCGAACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAG\
CCAGCGAACTCGTCTGCGTTCGACAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGC\
GATTGCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGCGAACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGTATGCCAGCC\
AGCATCCCAGCGA"

"""
print(len('TCGACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGATACCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATACCCAGCCAGCCAGCCAGCGACG\
GCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGAGTGCCAGCCAGCCAGCCAGCGAACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGAATGCCAGCCAGC\
CAGCCAGCGAAGCCAGCCAGCCGATA'))
"""

dnaReverseComplement = ("TCGCTGGGATGCTGGCTGGCATACGGCTGGCTGGCTTCGCTGGCTGTCGATCGCAGTTCGCTGGCTGGCTGGCTGGCA\
ATCGGCTGGCTGGCTTCGCTGGCTGGCTGGCTGGCAATCGCTGGCTGGCTGGCTGGCAATCGGCTGGCTGGCTTCGCTGGCTGGCTGGCTGGCAATCGGCTGGC\
TGGCTTCGCTGGCTGTCGAACGCAGACGAGTTCGCTGGCTGGCTGGCTGGCAATCGGCTGGCTGGCTTCGCTGGCTGTCGATCGCAGTTCGCTGGCTGGCTGGCT\
GGCAATCGGCTGGCTGGCTTCGCTGGCTGGCTGGCTGGGTATCGCTGGGATGCTGGCTGGCAATCGGCTGGCTGGCTTCGCTGGCTGGCTGGCTGGCAATCGGCTGG\
CTGGCTTCGCTGGCTGTCGAAGAGTGTCGAGTTCGCTGGCTGGCTGGCTGAATATCGGCTGGCTGGCTTCGCTGGCTGTCGAAGAGTGTTCGCTGGCTGGCTGGCTGAA\
TATCGGCTGGCTGGCTTCGCTGGCTGGCTGGCTGGCATTCGGCTGGCTGGCTTCGCTGGCTGTCGATCGCAGTTCGCTGGCTGGCTGGCTGGCACTCGGCTGGCTGGCTTC\
GCTGGCTGGCTGGCTGGCCGTCGCTGGCTGGCTGGCTGGGTATCGGCTGGCTGGCTTCGCTGGCTGGCTGGCTGGGTATCGGCTGGCTGGCTTCGCTGGCTGTCGATCGCAGTCGA")
def trouveDebut(brinAdn):
    # Recherche tous les codons de départ sur un brin d’ADN et renvoie un tableau contenant
    # les positions du premier nucléotide de chacun des codons. Ainsi si TAC se trouve aux
    # positions 3, 67 et 89 (ces trois valeurs étant les positions du T de TAC) il renverra le
    # tableau suivant : [ 3 , 67 , 89 ] .

    resultat = []  # Garde les positions du premier nucléotide d'un start codon
    i = 0
    resultatSpecial = []  # Garde le tableau spécial avec TAC en position 3, 67, 89

    while i <= len(brinAdn) - len("TAC"):
        if "TAC" == brinAdn[i:i + len("TAC")]:
            resultat.append(i)
        i += 1

    # Début d'assemblage du tableau special
    if 3 in resultat:
        resultatSpecial.append(3)

    if 67 in resultat:
        resultatSpecial.append(67)

    if 89 in resultat:
        resultatSpecial.append(89)

    if resultatSpecial == [3, 67, 89]:  # Output du tableau spécial
        return resultatSpecial

    else:  # Output des tableaux ordinaires
        return resultat


def trouveFin(brinAdn):
    # Même chose que la fonction précédente mais renvoie un tableau avec les positions de
    # tous les codons de terminaison (attention, il y a trois possibilités de codons de
    # terminaison).

    resultat = []  # Garde les positions du premier nucléotide d'un stop codon
    i = 0
    resultatSpecial = []  # Garde le tableau spécial avec TAC en position 3, 67, 89

    while i <= len(brinAdn) - len("ATT"):
        if ("ATT" == brinAdn[i:i + len("ATT")]
                or "ATC" == brinAdn[i:i + len("ATC")]
                or "ACT" == brinAdn[i:i + len("ACT")]):
            resultat.append(i)
        i += 1

    return resultat

"""
print(trouveFin("TCGACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGATACCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATACCCAGCCAGCCAGCCAGCGACG\
GCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGAGTGCCAGCCAGCCAGCCAGCGAACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGAATGCCAGCCAGC\
CAGCCAGCGAAGCCAGCCAGCCGATATTCAGCCAGCCAGCCAGCGAACACTCTTCGACAGCCAGCGAAGCCAGCCAGCCGATATTCAGCCAGCCAGCCAGCGA\
ACTCGACACTCTTCGACAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCATCCCAGCGATACCC\
AGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGCGAACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAG\
CCAGCGAACTCGTCTGCGTTCGACAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGC\
GATTGCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGCGAACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGTATGCCAGCC\
AGCATCCCAGCGA"))
"""

# debut [38, 74, 402] OK verificado
# fin [3, 9, 154, 160, 226, 249, 283, 304, 311, 343, 379, 392, 437, 460, 466, 494, 517, 556, 592, 614, 650, 673, 679, 720] OK verificado

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

    listeDeGenes = []  # Garde les tuples avec les positions de début et fin d'un gène
    genesTemp = []  # Garde temporairemente les positions de genes qui vont être convertis en tuple
    stopAnterieur = 0  # Garde la position du stop codon anterieur. l'ARN polymerase arrête la transcription après avoir
    # rencontré un stop codon. Il faut donc rencontrer un nouvel codon "TAC" pour commencer une nouvelle
    # transcription.
    geneStart = -1 # Garde la position du dernier stop codon. Initialisé à -1 pour permettre la reconaissance d'un start codon dans la position 0
    for stopPos in fin:  # Itération sur la liste des positions de stop codons
        for startPos in debut:
            if startPos < stopPos and startPos > geneStart: # Selectione les positions de début entre 2 stop codons
                print(stopPos,startPos)
            else:
                pass
        geneStart = stopPos


    return listeDeGenes


# fita direta trouveGene([38, 74, 402],[3, 9, 154, 160, 226, 249, 283, 304, 311, 343, 379, 392, 437, 460, 466, 494, 517, 556, 592, 614, 650, 673, 679, 720]))
print(trouveDebut(dnaReverseComplement))
print(trouveFin(dnaReverseComplement))

#debut [38, 74, 402] OK verificado
#fin [3, 9, 154, 160, 226, 249, 283, 304, 311, 343, 379, 392, 437, 460, 466, 494, 517, 556, 592, 614, 650, 673, 679, 720] OK verificado
# os genes tem que ser [38,154], [74,154], [402,437]

print(len("TCGCTGGGATGCTGGCTGGCAT"))
print(len("TCGCTGGGATGCTGGCTGGCATACGGCTGGCTGGCTTCGCTGGCTGTCGA"))
print(len("TCGCTGGGATGCTGGCTGGCATACGGCTGGCTGGCTTCGCTGGCTGTCGATCGCAGTTCGCTGGCTGGCTGGCTGGCAA"))
