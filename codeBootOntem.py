#COMEÇAR POR AQUI
# PROXIMOS PASSOS
# [X] VERIFICAR A FUNCAO DE ENCONTRAR GENES
# [X] TESTAR A FÇ DE ENCONTRAR INICIO DO GENE
# [X] TESTAR A FÇ DE ENCONTRAR FIM DO GENE
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


dnac = antisens(adn)


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
    resultatSpecial = []  # Garde le tableau spécial avec TAC en position 3, 67, 89

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

    listeDeGenes = [] # Garde les tuples avec les positions de début et fin d'un gène
    genesTemp = [] # Garde temporairemente les positions de genes qui vont être convertis en tuple
    stopAnterieur = 0 # Garde la position du stop codon anterieur. l'ARN polymerase arrête la transcription après avoir
                      # rencontré un stop codon. Il faut donc rencontrer un nouvel codon "TAC" pour commencer une nouvelle
                      # transcription.

    for stopPos in fin:
        for startPos in debut:
            if startPos < stopPos:
                if stopAnterieur < startPos: # Vérif. si le start codon analysé est après le dernier stop codon
                    if (stopPos - startPos) % 3 == 0: # Vérif. si les positions de fin et début sont multiples de 3

                        genesTemp.append(startPos)
                        genesTemp.append(stopPos)

                        # Conversion en tuple
                        listeDeGenes.append(tuple(genesTemp))

                        # # Réinitialisation du tableau pour une nouvelle conversion en tuples
                        genesTemp = []
                        print(listeDeGenes)
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

    #########################################################

    ##################### MODULO DE DESENHO DA PTN ############

    ###########################################


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

    rt(90)
    pu()
    fd(longeur / 2)
    lt(90)
    fd(longeur / 2)
    pd()


def carreTest():
    # 1 Doit dessineru un carré a partir du centre du tableau. Par limitation de codeBoot,
    # il n'est pas possible définir un test avec la fonction assert.
    carre(20, 0)


##
def dessinerLettre(lettre):
    # Dessine une lettre correspondant à un aminoacide de la protéine
    if lettre == "A":
        fd(5)
        rt(65)
        fd(5)
        bk(15)
        rt(50)
        fd(15)
        bk(5)
        lt(115)
        fd(4)

    if lettre == "B":
        bk(5)
        lt(90)
        fd(8)
        rt(90)
        fd(5)
        for _ in range(180):
            rt(1)
            fd(4 * 3.14 / 180)
        rt(180)
        for _ in range(180):
            rt(1)
            fd(4 * 3.14 / 180)
        fd(5)
        rt(90)
        fd(8)
        rt(90)

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
        ht()

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
        rt(90)

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
        rt(180)

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
        ht()

    if lettre == "J":
        pu()
        fd(4)
        lt(90)
        fd(5)
        rt(90)
        bk(5)
        pd()
        fd(8)
        pu()
        bk(4)
        pd()
        rt(90)
        fd(10)
        rt(90)
        fd(3)
        for _ in range(90):
            rt(1)
            fd(4 * 3.14 / 180)
        ht()

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
        pu()
        bk(7)
        rt(45)
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

        ht()

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
        rt(90)

    if lettre == "O":
        pu()
        bk(5)
        lt(90)
        fd(5)
        lt(90)
        bk(5)
        pd()
        for _ in range(360):
            lt(1)
            fd(5 * 3.14 / 180)

        ht()

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
        rt(180)

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
        rt(180)

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
        rt(180)

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
        lt(90)

    if lettre == "U":
        pu()
        bk(4)
        rt(90)
        bk(7)
        pd()
        fd(9)
        for _ in range(180):
            lt(1)
            fd(4 * 3.14 / 180)

        fd(9)
        ht()

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
        rt(60)
        rt(0)
        lt(0)

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

    if lettre == "X":
        rt(45)
        pu()
        bk(5)
        pd()
        fd(10)
        pu()
        bk(5)
        lt(90)
        bk(5)
        pd()
        fd(10)
        rt(45)

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
        lt(90)

    if lettre == "Z":
        rt(45)
        pu()
        bk(7)
        pd()
        lt(45)
        fd(10)
        lt(45)
        bk(14)
        rt(45)
        fd(10)


def testDessinerLettre():
    # 1 Doit dessiner la lettre "A" au centre du tableau. Par limitation de codeBoot,
    # il n'est pas possible définir un test avec la fonction assert.
    dessinerLettre("A")


##
def dessinerSeq(sequence):
    # Réçoit une séquence d'ARN et la déssine avec la tortue

    columnCounter = 0  # Mettre le carré à la bonne colonne
    lineCounter = 0  # Mettre le carré à la bonne ligne
    sequenceAAcides = ''

    # Conversion de la séquence d'ARN en séquence de lettres correspondant à acides aminés
    for j in range(0, len(sequence), 3):
        if sequence[j:j + 3] == "UAA" or sequence[j:j + 3] == "UAG" or sequence[
                                                                       j:j + 3] == "UGA":  # Élimination d'affichage des stop codons
            pass
        else:
            sequenceAAcides += lettreAa[sequence[j:j + 3]]

    # Dessin des carrés avec lettres
    for i in sequenceAAcides:
        positionner(-180, 120)
        if i == "*":
            pass
        else:
            # décalage vers la bonne ligne
            pu()
            rt(90)
            fd(20 * lineCounter)
            lt(90)
            pd()

            # affichache du carre
            carre(20, columnCounter)

            # affichage de la lettre
            dessinerLettre(i)

            columnCounter += 1

            # limitation de 15 carrés par ligne
            if columnCounter > 14:
                columnCounter = 0
                lineCounter += 1


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

    proteinString = ''

    # Affichage de la proteine sous forme de chaine de caractères
    for i in range(0, len(brinArn), 3):

        if codons_aa[brinArn[i:i + 3]] == "Stop":
            pass
        else:
            proteinString += codons_aa[brinArn[i:i + 3]] + '-'

    print(proteinString.rstrip('-'))

    # Affichage de la proteine sous forme de dessin

    dessinerSeq(brinArn)


# traduire("UUUUUCUUAUUGCUUCUCCUACUGAUUAUCAUAAUGGUUGUCGUAGUGUCUUCCUCAUCGCCUCCCCCACCGACUACCACAACGGCUGCCGCAGCGUAUUACUAAUAGCAUCACCAACAGAAUAACAAAAAGGAUGACGAAGAGUGUUGCUGAUGGCGUCGCCGACGGAGUAGCAGAAGGGGUGGCGGAGGG")
# st()
# dessinerSeq("GCCUGUGACGAGUUUGGAUAU")


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


print(trouveFin("TCGACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGATACCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATACCCAGCCAGCCAGCCAGCGACG\
GCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGAGTGCCAGCCAGCCAGCCAGCGAACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGAATGCCAGCCAGC\
CAGCCAGCGAAGCCAGCCAGCCGATATTCAGCCAGCCAGCCAGCGAACACTCTTCGACAGCCAGCGAAGCCAGCCAGCCGATATTCAGCCAGCCAGCCAGCGA\
ACTCGACACTCTTCGACAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCATCCCAGCGATACCC\
AGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGCGAACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAG\
CCAGCGAACTCGTCTGCGTTCGACAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGC\
GATTGCCAGCCAGCCAGCCAGCGAAGCCAGCCAGCCGATTGCCAGCCAGCCAGCCAGCGAACTGCGATCGACAGCCAGCGAAGCCAGCCAGCCGTATGCCAGCC\
AGCATCCCAGCGA"))


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

    for stop in fin:  # Itération sur la liste des positions de stop codons

        for start in debut:  # Itération sur la liste des positions de start codons

            if start > stopAnterieur and start < stop:  # Vérif si la position de début d'un gène est entre deux stop codons

                if (
                        stop - start) % 3 == 0:  # Vérif si la fin du gène se situe à un multiple de trois nucléotide du début

                    # Construction d'un tableau avec une position de start et une position de stop d'un gene
                    genesTemp.append(start)
                    genesTemp.append(stop)

                    # Conversion du tableau en tuple
                    listeDeGenes.append(tuple(genesTemp))

                    # Réinitialisation du tableau pour une nouvelle conversion en tuples
                    genesTemp = []

        stopAnterieur = stop

    return listeDeGenes


# debut [38, 74, 402] OK verificado
# fin [3, 9, 154, 160, 226, 249, 283, 304, 311, 343, 379, 392, 437, 460, 466, 494, 517, 556, 592, 614, 650, 673, 679, 720] OK verificado

# os genes tem que ser [38,154], [74,154], [402,437]


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
    geneStart = 0
    for stopPos in fin:  # Itération sur la liste des positions de stop codons
        for startPos in debut:
            if startPos < stopPos and startPos >= geneStart:
                print(stopPos, startPos)
            else:
                pass
            geneStart = stopPos
            print(geneStart)

    return listeDeGenes


print(trouveGene([1, 2, 3, 4, 5], [4, 6]))



