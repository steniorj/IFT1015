# Date: 2024-03-18
# Nom, prénom: Da Silva Faria, Stennio
# Programme pour détection, transcription et traduction des gènes d'une séquence d'ADN, affichage des aminoacides de la
# protéines résultant en forme de chaîne de caractéres dans le console et en forme de blocs dessinnés par tortue en codeBoot.


##########################################################
####### PARTIE 1/2: MODULE DE TRAITEMENT DE L'ADN ########
##########################################################

adn = "CTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGATACCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATACCCAGCCAGCCAGCCAGCGACG\
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
    "ACU": "Thréonine",
    "ACC": "Thréonine",
    "ACA": "Thréonine",
    "ACG": "Thréonine",
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

    # Output du tableau spécial
    if resultatSpecial == [3, 67, 89]:
        return resultatSpecial

    # Output des tableaux ordinaires
    else:
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

    nouveauStart = -3  # Limite inférieur où le start codon du gène actuel peut se trouver. Initialisé a -3 pour simuler un
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


    ##########################################################
    ####### PARTIE 2/2: MODULE DE DESSIN DE LA PROTÉINE ######
    ##########################################################

##
def positionner(x, y):
    # Positionne la tortue pour démarrer le dessin de la protéine.

    pu()
    goto(0, 0)
    lt(90)
    fd(y)
    rt(90)
    fd(x)
    pd()

def testPositionner():
    # 1 Doit mettre la tortue au centre du tableau. Par limitation de codeBoot,
    # il n'est pas possible définir un test avec la fonction assert.
    positionner(0, 0)


##
def carre(longeur, nombre):
    # Prend deux entiers en paramètre (taille du côté du carré et l’indice du carré à dessiner) et
    # trace un carré à l’aide de la tortue.

    pu()
    fd(nombre * 20)
    pd()

    for _ in range(4):
        fd(longeur)
        rt(90)

def carreTest():
    # 1 Doit dessiner un carré a partir du centre du tableau. Par limitation de codeBoot,
    # il n'est pas possible définir un test avec la fonction assert.
    carre(20, 0)


##
def dessinerLettre(lettre):
    # Dessine une lettre correspondant à un aminoacide de la protéine dans le carré dessiné par la fonction carre(longeur, nombre)

    # Mettre la tortue au centre du carré
    rt(90)
    pu()
    fd(20 / 2)
    lt(90)
    fd(20 / 2)
    pd()

    # Dessiner la lettre
    if lettre == "A":
        fd(5)
        rt(65)
        fd(5)
        bk(15)
        rt(50)
        fd(15)
        bk(5)
        lt(115)
        fd(5)

        # Répositionner la tortue au centre du carré
        pu()
        bk(5)
        rt(115)
        fd(5)
        bk(15)
        lt(50)
        fd(15)
        bk(5)
        lt(65)
        bk(5)
        pd()

    if lettre == "C":
        pu()
        lt(90)
        fd(5)
        lt(90)
        bk(5)
        pd()
        fd(5)
        for _ in range(180):
            lt(1)
            fd(5 * 3.14 / 180)
        fd(5)

        # Répositionner la tortue au centre du carré
        pu()
        bk(5)
        for _ in range(180):
            lt(1)
            fd(5 * 3.14 / 180)
        bk(5)
        fd(5)
        rt(90)
        bk(5)
        rt(90)
        pd()

    if lettre == "D":
        pu()
        lt(90)
        fd(5)
        rt(90)
        bk(5)
        pd()
        fd(3)

        for _ in range(180):
            rt(1)
            fd(5 * 3.14 / 180)
        fd(3)
        rt(90)
        fd(10)

        # Répositionner la tortue au centre du carré
        pu()
        bk(10)
        lt(90)
        bk(3)
        for _ in range(180):
            rt(1)
            fd(5 * 3.14 / 180)
        bk(3)
        fd(5)
        lt(90)
        bk(5)
        rt(90)
        pd()

    if lettre == "E":
        pu()
        lt(90)
        fd(5)
        lt(90)
        bk(5)
        pd()
        fd(10)
        lt(90)
        fd(10)
        lt(90)
        fd(10)
        pu()
        bk(10)
        lt(90)
        fd(5)
        rt(90)
        pd()
        fd(10)

        # Répositionner la tortue au centre du carré
        pu()
        bk(10)
        lt(90)
        bk(5)
        rt(90)
        fd(10)
        bk(10)
        rt(90)
        bk(10)
        rt(90)
        bk(10)
        fd(5)
        rt(90)
        bk(5)
        rt(90)
        pd()

    if lettre == "F":
        pu()
        lt(90)
        fd(5)
        lt(90)
        bk(5)
        pd()
        fd(10)
        lt(90)
        fd(10)
        lt(90)
        pu()
        fd(10)
        bk(10)
        lt(90)
        fd(5)
        rt(90)
        pd()
        fd(10)

        # Répositionner la tortue au centre du carré
        pu()
        bk(5)
        pd()

    if lettre == "G":
        pu()
        lt(90)
        fd(5)
        lt(90)
        bk(5)
        pd()
        fd(5)
        for _ in range(180):
            lt(1)
            fd(5 * 3.14 / 180)
        fd(5)
        lt(90)
        fd(5)
        lt(90)
        fd(5)

        # Répositionner la tortue au centre du carré
        pu()
        bk(5)
        rt(90)
        bk(5)
        rt(90)
        bk(5)
        for _ in range(180):
            lt(1)
            fd(5 * 3.14 / 180)
        bk(5)
        fd(5)
        rt(90)
        bk(5)
        rt(90)
        pd()

    if lettre == "H":
        pu()
        bk(2)
        rt(90)
        bk(5)
        pd()
        fd(10)
        pu()
        bk(5)
        lt(90)
        pd()
        fd(5)
        lt(90)
        pu()
        bk(5)
        pd()
        fd(10)
        rt(90)

        # Répositionner la tortue au centre du carré
        pu()
        lt(90)
        bk(5)
        rt(90)
        bk(3)
        pd()

    if lettre == "I":
        pu()
        lt(90)
        fd(5)
        rt(90)
        bk(5)
        pd()
        fd(10)
        pu()
        bk(5)
        rt(90)
        pd()
        fd(10)
        lt(90)
        pu()
        bk(5)
        pd()
        fd(10)

        # Répositionner la tortue au centre du carré
        pu()
        bk(5)
        rt(90)
        bk(5)
        lt(90)
        pd()

    if lettre == "K":
        pu()
        bk(2)
        rt(90)
        bk(8)
        pd()
        fd(14)
        pu()
        bk(7)
        lt(45)
        pd()
        fd(8)
        pu()
        bk(8)
        lt(90)
        pd()
        fd(7)

        # Répositionner la tortue au centre du carré
        pu()
        bk(7)
        rt(45)
        lt(45)
        fd(7)
        bk(7)
        rt(90)
        fd(8)
        bk(8)
        rt(45)
        fd(7)
        bk(14)
        fd(8)
        lt(90)
        fd(2)
        pd()

    if lettre == "L":
        pu()
        bk(2)
        rt(90)
        bk(6)
        pd()
        fd(12)
        lt(90)
        fd(6)

        # Répositionner la tortue au centre du carré
        pu()
        bk(6)
        rt(90)
        bk(12)
        fd(6)
        lt(90)
        fd(2)
        pd()

    if lettre == "M":
        pu()
        bk(4)
        rt(90)
        fd(6)
        pd()
        bk(12)
        lt(45)
        fd(6)
        lt(90)
        fd(6)
        rt(135)
        fd(12)
        lt(90)

        # Répositionner la tortue au centre du carré
        pu()
        rt(90)
        bk(12)
        lt(135)
        bk(6)
        rt(90)
        bk(6)
        rt(45)
        fd(6)
        lt(90)
        fd(4)
        pd()

    if lettre == "N":
        pu()
        bk(3)
        rt(90)
        fd(6)
        pd()
        bk(12)
        lt(30)
        fd(14)
        lt(150)
        fd(12)

        # Répositionner la tortue au centre du carré
        pu()
        bk(12)
        rt(150)
        bk(14)
        rt(30)
        fd(12)
        bk(6)
        lt(90)
        fd(3)
        pd()

    if lettre == "P":
        pu()
        bk(3)
        rt(90)
        fd(7)
        pd()
        bk(14)
        lt(90)
        fd(4)
        for _ in range(180):
            rt(1)
            fd(4 * 3.14 / 180)
        fd(2)

        # Répositionner la tortue au centre du carré
        pu()
        bk(2)
        for _ in range(180):
            lt(1)
            bk(4 * 3.14 / 180)

        bk(4)
        rt(90)
        fd(14)
        bk(7)
        lt(90)
        fd(3)
        pd()

    if lettre == "Q":
        pu()
        bk(5)
        lt(90)
        fd(6)
        lt(90)
        bk(5)
        pd()
        for _ in range(180):
            lt(1)
            fd(5 * 3.14 / 180)
        fd(2)
        rt(45)
        fd(4)
        pu()
        bk(4)
        lt(45)
        bk(2)
        pd()
        for _ in range(180):
            lt(1)
            fd(5 * 3.14 / 180)

        # Répositionner la tortue au centre du carré
        pu()
        for _ in range(180):
            rt(1)
            bk(5 * 3.14 / 180)
        fd(2)
        rt(45)
        fd(4)
        bk(4)
        lt(45)
        bk(2)
        for _ in range(180):
            rt(1)
            bk(5 * 3.14 / 180)
        fd(5)
        rt(90)
        bk(6)
        rt(90)
        fd(5)
        pd()

    if lettre == "R":
        bk(5)
        lt(90)
        fd(8)
        rt(90)
        fd(5)
        for _ in range(180):
            rt(1)
            fd(4 * 3.14 / 180)
        rt(180)
        rt(45)
        fd(8)
        pu()
        bk(8)
        lt(45)
        bk(5)
        pd()
        rt(90)
        fd(7)
        lt(90)

        # Répositionner la tortue au centre du carré
        pu()
        rt(90)
        bk(7)
        lt(90)
        fd(5)
        rt(45)
        fd(8)
        bk(8)
        lt(45)
        lt(180)
        for _ in range(180):
            rt(1)
            fd(4 * 3.14 / 180)
        bk(5)
        lt(90)
        bk(8)
        rt(90)
        fd(5)
        pd()

    if lettre == "S":
        pu()
        lt(90)
        fd(5)
        lt(90)
        bk(5)
        pd()
        fd(5)
        for _ in range(180):
            lt(1)
            fd(3 * 3.14 / 180)

        for _ in range(180):
            rt(1)
            fd(3 * 3.14 / 180)
        fd(5)

        # Répositionner la tortue au centre du carré
        pu()
        bk(5)
        for _ in range(180):
            lt(1)
            bk(3 * 3.14 / 180)

        for _ in range(180):
            rt(1)
            bk(3 * 3.14 / 180)

        bk(5)
        fd(5)
        rt(90)
        bk(5)
        rt(90)
        pd()

    if lettre == "T":
        pu()
        lt(90)
        fd(5)
        rt(90)
        bk(5)
        pd()
        fd(10)
        pu()
        bk(5)
        rt(90)
        pd()
        fd(12)

        # Répositionner la tortue au centre du carré
        pu()
        bk(7)
        lt(90)
        pd()

    if lettre == "V":
        pu()
        bk(6)
        rt(90)
        bk(5)
        pd()
        lt(30)
        fd(12)
        lt(120)
        fd(12)

        # Répositionner la tortue au centre du carré
        pu()
        bk(12)
        rt(120)
        bk(12)
        rt(30)
        fd(5)
        lt(90)
        fd(6)
        pd()

    if lettre == "W":
        pu()
        bk(5)
        rt(90)
        bk(6)
        pd()
        fd(12)
        lt(135)
        fd(7)
        rt(90)
        fd(7)
        lt(135)
        fd(12)
        rt(90)

        # Répositionner la tortue au centre du carré
        pu()
        lt(90)
        bk(12)
        rt(135)
        bk(7)
        lt(90)
        bk(7)
        rt(135)
        bk(12)
        fd(6)
        lt(90)
        fd(5)
        pd()

    if lettre == "Y":
        rt(45)
        pu()
        bk(5)
        pd()
        fd(5)
        lt(90)
        fd(5)
        pu()
        bk(5)
        pd()
        rt(135)
        fd(5)

        # Répositionner la tortue au centre du carré
        pu()
        bk(5)
        lt(90)
        pd()

    # Retourner la tortue à la position originale
    pu()
    bk(10)
    rt(90)
    bk(10)
    lt(90)
    pd()

def testDessinerLettre():
    # 1 Doit dessiner la lettre "A" au centre du tableau. Par limitation de codeBoot,
    # il n'est pas possible définir un test avec la fonction assert.
    dessinerLettre("A")


##
def dessinerSeq(sequence):
    # Réçoit une séquence d'ARN et la déssine avec la tortue. Utilisée dans la fonction traduire(brinArn)

    columnCounter = 0  # Mettre le carré à la bonne colonne

    columnLimit = 0 # Limite le nombre de carrés par ligne

    sequenceAAcides = '' # Garde la seq de lettres à être déssinés

    # Conversion de la séquence d'ARN en séquence de lettres correspondant à acides aminés
    for j in range(0, len(sequence), 3):
        sequenceAAcides += lettreAa[sequence[j:j + 3]]

    # Dessin des carrés avec lettres
    for i in sequenceAAcides:

        if i == "*":  # Ignorer les stop codons
            pass

        else:
            # Affichache du carre
            carre(20, columnCounter)

            # Affichage de la lettre dans le carré
            dessinerLettre(i)

            columnCounter = 1  # Passer à la prochaine colonne

            columnLimit += 1

            # limitation de 15 carrés par ligne
            if columnLimit > 14:
                columnCounter = 0
                columnLimit = 0
                pu()
                bk(20 * 14)
                pd()
                pu()
                rt(90)
                fd(20)
                lt(90)
                pd()

    # Positionner la tortue pour le dessin d'une prochaine protéine
    pu()
    bk(20 * (columnLimit - 1))
    pd()
    pu()
    rt(90)
    fd(40)
    lt(90)
    pd()

def testDessinerSeq():
    # 1 Doit dessiner un carré avec la lettre "M"
    dessinerSeq("AUG")
    sleep(3)

    # 2 Doit dessiner 15 carrés avec la lettre "M", passer à la ligne suivante
    # et dessiner 4 carrés avec la lettre "Y"
    dessinerSeq("AUGAUGAUGAUGAUGAUGAUGAUGAUGAUGAUGAUGAUGAUGAUGUAUUAUUAUUAU")
    sleep(3)

    3  # Ne doit pas montrer les stop codons. Ne doit rien afficher
    clear()
    dessinerSeq("UAAUAGUGA")


##
def traduire(brinArn):
    # Prend en paramètre un brin d’ARN (chaine de caractères) et affiche la protéine sous
    # forme d’une chaine de caractères et la dessine à l’aide de la tortue.

    proteinString = '' # Garde le nom des acides aminés à être affichés dans le console

    # Affichage de la proteine sous forme de chaine de caractères
    for i in range(0, len(brinArn), 3):

        if codons_aa[brinArn[i:i + 3]] == "Stop":  # Empêcher l'affichage des stop codons
            pass
        else:
            proteinString += codons_aa[brinArn[i:i + 3]] + '-'

    print(proteinString.rstrip('-'), '\n')

    # Affichage de la proteine sous forme de dessin
    dessinerSeq(brinArn)


## Définition des variables ##

#Brin positif
debutBrinPositif = trouveDebut(adn) # Positions des start codons

finBrinPositif = trouveFin(adn) # Positions des stop codons

genesBrinPositif = trouveGene(debutBrinPositif, finBrinPositif) # Positions de départ et fin de chaque gene

gene1AdnBrinPositif = genesEnChaine(genesBrinPositif[0][0], genesBrinPositif[0][1], adn) # Chaine d'ADN du premier gène
gene2AdnBrinPositif = genesEnChaine(genesBrinPositif[1][0], genesBrinPositif[1][1], adn) # Chaine d'ADN du deuxième gène
gene3AdnBrinPositif = genesEnChaine(genesBrinPositif[2][0], genesBrinPositif[2][1], adn) # Chaine d'ADN du troisième gène

gene1ArnBrinPositif = transcrire(gene1AdnBrinPositif) # Chaine d'ARN du premier gène
gene2ArnBrinPositif = transcrire(gene2AdnBrinPositif) # Chaine d'ARN du deuxième gène
gene3ArnBrinPositif = transcrire(gene3AdnBrinPositif) # Chaine d'ARN du troisième gène

#Brin négatif
adnComplementReverse = reverseComplement(adn) # Génération du complement reverse à partir du brin positif d'ADN

debutBrinNegatif = trouveDebut(adnComplementReverse) # Positions du start codon

finBrinNegatif = trouveFin(adnComplementReverse) # Positions des stop codons

genesBrinNegatif = trouveGene(debutBrinNegatif,finBrinNegatif) # Positions de départ et fin du gene

gene1AdnBrinNegatif = genesEnChaine(genesBrinNegatif[0][0], genesBrinNegatif[0][1],adnComplementReverse) # Chaine d'ADN du gène

gene1ArnBrinNegatif = transcrire(gene1AdnBrinNegatif) # Chaine d'ARN du gène


## Affichage du travail ##
clear(370,600) # Augmenter la fenêtre
positionner(-180, 300)  # Positionner la tortue au coin supérieur gauche

traduire(gene1ArnBrinPositif)
traduire(gene2ArnBrinPositif)
traduire(gene3ArnBrinPositif)
traduire(gene1ArnBrinNegatif)