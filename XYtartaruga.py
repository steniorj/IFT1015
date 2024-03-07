#arquivo do codeboot:
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


## <- indique le début d'un pair fonction et son test respectif
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
