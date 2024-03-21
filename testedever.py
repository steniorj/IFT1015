adn="TCGACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGATACCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATACCCAGCCAGCCAGCCAGCGACG\
GCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGAGTGCCAGCCAGCCAGCCAGCGAACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGAATGCCAGCCAGC\
CAGCCAGCGAAGCCAGCCAGCCGATATTCAGCCAGCCAGCCAGCGAACACTCTTCGACAGCCAGCGAAGCCAGCCAGCCGATATTCAGCCAGCCAGCCAGCGA\
ACTCGACACTCTTCGACAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCATCCCAGCGATACCC\
AGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGCGAACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAG\
CCAGCGAACTCGTCTGCGTTCGACAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGC\
GATTGCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGCGAACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGTATGCCAGCC\
AGCATCCCAGCGA"

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

# Dictionnaire pour la construction du brin d'ADN complementaire dans la fonction "antisens(brinAdn)"
adnAppariement = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

# Dictionnaire pour faire la conversion d'ADN en ARN dans la fonction "transcrire(brinAdn)"
adnTranscriptionDictionnaire = {
    "A": "U",
    "T": "A",
    "C": "G",
    "G": "C"
}


## <- indique le début d'un pair fonction/fonction de test
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


def testReverseComplement():
    # 1 cas général:
    assert reverseComplement("AAATTTCCCGGG") == "GGGCCCTTTAAA"


##
def trouveDebut(brinAdn):
    # Recherche tous les codons de départ sur un brin d’ADN et renvoie un tableau contenant
    # les positions du premier nucléotide de chacun des codons. Ainsi si TAC se trouve aux
    # positions 3, 67 et 89 (ces trois valeurs étant les positions du T de TAC) il renverra le
    # tableau suivant : [ 3 , 67 , 89 ] .

    resultat = []  # Garde les positions du premier nucléotide d'un start codon
    resultatSpecial = []  # Garde le tableau spécial avec TAC en position 3, 67, 89

    for i in range(0, len(brinAdn)):
        if brinAdn[i:i + 3] == "TAC":
            resultat.append(i)

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


def testTrouveDebut():
    # 1 cas général
    assert trouveDebut("-TAC--TAC---") == [1, 6]

    # 2 test si la fonction retourne le tableau spécial même s'il y a d'autres start codons dans la séquence
    assert trouveDebut("---TAC------TAC----------------------------------------------------"
                       "TAC-------------------TAC") == [3, 67, 89]


##
def trouveFin(brinAdn):
    # Recherche tous les codons de départ sur un brin d’ADN et renvoie un tableau contenant
    # les positions du premier nucléotide de chacun des codons. Ainsi si TAC se trouve aux
    # positions 3, 67 et 89 (ces trois valeurs étant les positions du T de TAC) il renverra le
    # tableau suivant : [ 3 , 67 , 89 ] .

    resultat = []  # Garde les positions du premier nucléotide d'un start codon

    for i in range(0, len(brinAdn)):
        if (brinAdn[i:i + 3] == "ATT") or (brinAdn[i:i + 3] == "ATC") or (brinAdn[i:i + 3] == "ACT"):
            resultat.append(i)

    return resultat


def testTrouveFin():
    # 1 cas général pour le codon ATT:
    assert trouveFin("-ATT----") == [1]

    # 2 cas général pour le codon ATC:
    assert trouveFin("-ATT----ATC---") == [1, 8]

    # 3 cas général pour le codon ACT:
    assert trouveFin("-ATT----ATC---ACT---") == [1, 8, 14]


##
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

    genesTemp = []  # Garde temporairement les positions des codons qui vont être convertis en tuple

    stopAnterieur = 0  # Garde la position du dernier stop codon valide. La transcription s'arrête après avoir
    # rencontré un stop codon. Pour trouver le prochain gène il est donc impératif rencontrer un nouvel codon "TAC"
    # pour commencer une nouvelle transcription.

    stopFlag = False  # Signale q'une tuple valide a été trouvé. Le prochain gène a un start codon situé après le stop codon courant

    nouveauStart = -3  # Limite inférieur où le start codon du gène actuel peut se trouver. Initialisé a -3 simuler un
                       # un stop codon avant la position zero.

    for stopPos in fin:
        for startPos in debut:

            # Vérif. si tous les start codons valides pour le stop codon actuel ont été enregistrés
            if stopAnterieur != stopPos and stopFlag == True:

                nouveauStart = stopAnterieur # Exclure les start codons qui viennent avant le dernier stop codon

                stopFlag = False  # Réinitialiation du flag

            if startPos < stopPos:
                if nouveauStart < startPos:  # Vérif. si le start codon analysé est après le dernier stop codon.

                    if (stopPos - startPos) % 3 == 0:  # Vérif. si les positions de fin et début sont multiples de 3

                        genesTemp.append(startPos)
                        genesTemp.append(stopPos)

                        # Conversion en tuple et addition au tableau final
                        listeDeGenes.append(tuple(genesTemp))

                        # Réinitialisation du tableau pour une nouvelle conversion en tuples
                        genesTemp = []

                        # Activation du flag
                        stopFlag = True

                        # Enregistre la position do stop codon actuel pour permettre une comparaison
                        # visant identifier si la fonction est passé au stop codon suivant
                        stopAnterieur = stopPos

    return print(listeDeGenes)

adninit = trouveDebut(adn)
adnfin = trouveFin(adn)
#[38, 74, 402]
#[3, 9, 154, 160, 226, 249, 283, 304, 311, 343, 379, 392, 437, 460, 466, 494, 517, 556, 592, 614, 650, 673, 679, 720]
genes = trouveGene(adninit,adnfin)
