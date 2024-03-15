#COMEÇAR POR AQUI
# PROXIMOS PASSOS
# [X] TESTAR A FÇ DE ENCONTRAR INICIO DO GENE
# [X] TESTAR A FÇ DE ENCONTRAR FIM DO GENE
# [X] VERIFICAR A FUNCAO DE ENCONTRAR GENES
# [] TESTAR A FUNCAO DE ENCOTRAR GENES PARA O COMPLEMENTO REVERSO USANDO O ARQUIVO TESTE DEVER
# [] TESTAR TODAS AS FÇ
# [] UNIR TDS AS FÇ
# [] RODAR TODAS AS FÇ COM DNA + E -

adn = "TCGACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGATACCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATACCCAGCCAGCCAGCCAGCGACG\
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
    genesTemp = []  # Garde temporairemente les positions des codons qui vont être convertis en tuple
    stopAnterieur = 0  # Garde la position du stop codon anterieur. l'ARN polymerase arrête la transcription après avoir
    # rencontré un stop codon. Pour trouver le prochain gène il est donc nécéssaire rencontrer un nouvel codon "TAC" pour commencer une nouvelle
    # transcription.
    stopFlag = False  # Signale q'une tuple valide a été trouvé. Le prochain gène a un start codon situé après le stop codon courant

    for stopPos in fin:
        for startPos in debut:
            if stopAnterieur < stopPos and stopFlag == True:  # Tous les start codons valides pour ce stop codon ont été enregistrés

                stopFlag = False  # Réinitialiation du flag

            if startPos < stopPos:
                if stopAnterieur < startPos:  # Vérif. si le start codon analysé est après le dernier stop codon
                    if (stopPos - startPos) % 3 == 0:  # Vérif. si les positions de fin et début sont multiples de 3

                        genesTemp.append(startPos)
                        genesTemp.append(stopPos)

                        # Conversion en tuple et addition au tableau final
                        listeDeGenes.append(tuple(genesTemp))

                        # Réinitialisation du tableau pour une nouvelle conversion en tuples
                        genesTemp = []

                        # Activation du flag
                        stopFlag = True

                        stopAnterieur = stopPos  # Permettre que la recherche du prochain start codon soit faite après le dernier stop codon

    return listeDeGenes


def testTrouveGene():
    # 1 un gène avec un start codon et un stop codon:
    assert trouveGene([1], [4]) == [(1, 4)]

    # 2 deux gènes avec le même stop codon:
    assert trouveGene([1, 4], [7]) == [(1, 7), (4, 7)]

    # 3 un gène entre deux stop codons:
    assert trouveGene([5], [2, 11]) == [(5, 11)]


##
def genesEnChaine(debut, fin, sequence):
    # Prend en paramètre les positions de début et fin d'un gene et une séquence d'adn,
    # en renvoyant la chaîne de caractères correspondant

    sousChaineEnADN = sequence[debut:fin + 3]

    return sousChaineEnADN


def testGenesEnChaine():
    # 1 cas général:
    assert genesEnChaine(0, 5, "AAA--TTT----") == "AAA--TTT"


##
def transcrire(brinAdn):
    # Prend en paramètre la sous-chaine de caractère du brin d’ADN débutant au début du gène
    # et se terminant à la fin du gène et renvoie le brin d’ARN correspondant sous forme d’une
    # chaine de caractères.
    arnTranscrit = ''
    for i in brinAdn:
        arnTranscrit += adnTranscriptionDictionnaire[i]
    return arnTranscrit


def testTranscrire():
    # 1 cas géneral:
    assert transcrire("AAATTTCCCGGG") == "UUUAAAGGGCCC"

## Définition des variables ####

#Brin positif


debutBrinPositif = trouveDebut(adn)

finBrinPositif = trouveFin(adn)

genesBrinPositif = trouveGene(debutBrinPositif, finBrinPositif)

gene1AdnBrinPositif = genesEnChaine(genesBrinPositif[0][0], genesBrinPositif[0][1], adn)
gene2AdnBrinPositif = genesEnChaine(genesBrinPositif[1][0], genesBrinPositif[1][1], adn)
gene3AdnBrinPositif = genesEnChaine(genesBrinPositif[2][0], genesBrinPositif[2][1], adn)

gene1ArnBrinPositif = transcrire(gene1AdnBrinPositif)
gene2ArnBrinPositif = transcrire(gene2AdnBrinPositif)
gene3ArnBrinPositif = transcrire(gene3AdnBrinPositif)

#Brin négatif

adnComplementReverse = reverseComplement(adn)

debutBrinNegatif = trouveDebut(adnComplementReverse)

finBrinNegatif = trouveFin(adnComplementReverse)

genesBrinNegatif = trouveGene(debutBrinNegatif, finBrinNegatif)


print(debutBrinNegatif,finBrinNegatif)
