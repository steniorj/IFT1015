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

adnAppariement = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C",
}

adnTranscriptionDictionnaire = {
    "A" : "U",
    "T" : "A",
    "C" : "G",
    "G" : "C",
}

""" ### FUNCAO COMPLETA ###
def antisens(brinAdn):
    # Part de brin ADN fourni et renvoie le brin d’ADN complémentaire.
    adnAntisens = ''
    for i in brinAdn:
        adnAntisens += adnAppariement[i]
    return adnAntisens


def testAntisens():
    # 1 cas géneral:
    assert antisens("AAATTTCCCGGG") == "TTTAAAGGGCCC"
"""

""" ### FUNCAO COMPLETA ###

def reverseComplement(brinAdn):
    # Inversion du brin complémentaire d'ADN pour qu'il soit affiché dans le sense 5' -> 3'
    brinAdn = antisens(brinAdn) # Obtention du brin complémentaire d'ADN

    adnBrinReverseComplement = '' # Variable pour garder l'output

    for i in str(brinAdn[len(brinAdn)::-1]):
        adnBrinReverseComplement += i

    return adnBrinReverseComplement

def testReverseComplement():
    #1 cas général:
    assert reverseComplement("AAATTTCCCGGG") == "GGGCCCTTTAAA"
    
"""

"""## FUNÇÃO COMPLETAMENTE PRONTA ##

def trouveDebut(brinAdn):
    # Recherche tous les codons de départ sur un brin d’ADN et renvoie un tableau contenant
    # les positions du premier nucléotide de chacun des codons. Ainsi si TAC se trouve aux
    # positions 3, 67 et 89 (ces trois valeurs étant les positions du T de TAC) il renverra le
    # tableau suivant : [ 3 , 67 , 89 ] .

    resultat = [] # Garde les positions du premier nucléotide d'un start codon
    i = 0
    resultatSpecial = [] # Garde le tableau spécial avec TAC en position 3, 67, 89

    while i <= len(brinAdn)-len("TAC"):
        if "TAC" == brinAdn[i:i+len("TAC")]:
            resultat.append(i)
        i+=1

    # Début d'assemblage du tableau special
    if 3 in resultat:
        resultatSpecial.append(3)

    if 67 in resultat:
        resultatSpecial.append(67)

    if 89 in resultat:
        resultatSpecial.append(89)

    if resultatSpecial == [3, 67, 89]: # Output du tableau spécial
        return resultatSpecial

    else: # Output des tableaux ordinaires
        return resultat



def testTrouveDebut():
    #1 cas général
    assert trouveDebut("-TAC--TAC---") == [1, 6]

    #2 test si la fonction retourne le tableau spécial même s'il y a d'autres start codons dans la séquence
    assert trouveDebut("---TAC------TAC----------------------------------------------------"
                       "TAC-------------------TAC") == [3, 67, 89]
    

testTrouveDebut()
"""

"""## FUNCAO COMPLETAMENTE PRONTA
def trouveFin(brinAdn):
    # Même chose que la fonction précédente mais renvoie un tableau avec les positions de
    # tous les codons de terminaison (attention, il y a trois possibilités de codons de
    # terminaison).

    resultat = []  # Garde les positions du premier nucléotide d'un stop codon
    i = 0
    resultatSpecial = []  # Garde le tableau spécial avec TAC en position 3, 67, 89

    while i <= len(brinAdn) - len("ATT"):
        if (   "ATT" == brinAdn[i:i + len("ATT")]
            or "ATC" == brinAdn[i:i + len("ATC")]
            or "ACT" == brinAdn[i:i + len("ACT")]   ):

            resultat.append(i)
        i += 1

    return resultat

def testTrouveFin():
    # 1 cas général pour le codon ATT:
    assert trouveFin("-ATT----") == [1]

    # 2 cas général pour le codon ATC:
    assert trouveFin("-ATT----ATC---") == [1, 8]

    # 3 cas général pour le codon ACT:
    assert trouveFin("-ATT----ATC---ACT---") == [1, 8, 14]

testTrouveFin()

"""


"""
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

def testTrouveGene():
    #1 un gène avec un start codon et un stop codon:
    assert trouveGene([1],[4]) == [(1,4)]

    #2 deux gènes avec le même stop codon:
    assert trouveGene([1,4], [7]) == [(1,7), (4,7)]

    #3 un gène entre deux stop codons:
    assert trouveGene([5], [2, 11]) == [(5,11)]
"""

""" ### COMPLETA 
def transcrire(brinAdn):
    # Prend en paramètre la sous-chaine de caractère du brin d’ADN débutant au début du gène
    # et se terminant à la fin du gène et renvoie le brin d’ARN correspondant sous forme d’une
    # chaine de caractères.
    arnTranscrit = ''
    for i in brinAdn:
        arnTranscrit += adnTranscriptionDictionnaire[i]
    return arnTranscrit

def testTranscrire():
    #1 cas géneral:
    assert transcrire("AAATTTCCCGGG") == "UUUAAAGGGCCC"
"""


def traduire(brinArn):
    # Prend en paramètre un brin d’ARN (chaine de caractères) et affiche la protéine sous
    # forme d’une chaine de caractères et la dessine à l’aide de la tortue.

    proteinString = ''

    for i in range(0,len(brinArn),3):

        if codons_aa[brinArn[i:i+3]] == "Stop":
            pass
        else:
            proteinString += codons_aa[brinArn[i:i+3]] + '-'

    print(proteinString.rstrip('-'))

traduire("AUGCUUAUAUGAUAGUAA")

def testTraduire():
    #1 cas général pour les codons codants:
    traduire("AUGCUU") == "Méthionine (Start)-Leucine"

    #2 séquence avec les trois stop codons
    traduire("AUGCUUAUAUGAUAGUAA") == "Méthionine (Start)-Leucine-Isoleucine"



def carre(longueur, nombre):
    # Prend deux entiers en paramètre (taille du côté du carré et l’indice du carré à dessiner) et
    # trace un carré à l’aide de la tortue.
    return



