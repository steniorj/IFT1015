#odigo pra rodar no codeboot

do desktop:


def positionnerCursor(x, y):
    pu()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    pd()


def debutDessin():
    pu()
    goto(0, 0)
    pd()
    positionnerCursor(-180, 120)
    pd()
    st()


def carreAvecLettre(largeur, lettre):
    # Dessine un carré et positionne le cursor au milieu
    for _ in range(4):
        fd(largeur)
        rt(90)
    pu()
    rt(90)
    fd(largeur / 2)
    lt(90)
    fd(largeur / 2)
    pd()

    # Dessine la lettre
    dessinerLettre(lettre)

    # Repositionne le cursor au début de la 1ere ligne


def dessinerLettre(lettre):
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
        ht()

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

        ht()

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
        ht()

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

        ht()

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
        ht()

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

        ht()

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
        ht()

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

        ht()

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

        ht()

    if lettre == "W":
        pu()
        bk(5)
        rt(90)
        bk(6)
        pd()
        fd(12)
        rt(45)
        fd(5)

        ht()


debutDessin()
carreAvecLettre(20, "W")

________________________
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


def positionner(x, y):
    pu()
    goto(0, 0)
    lt(90)
    fd(y)
    rt(90)
    fd(x)
    pd()


def carreLettre(largeur, lettre):
    for _ in range(4):
        fd(largeur)
        rt(90)

    rt(90)
    pu()
    fd(largeur / 2)
    lt(90)
    fd(largeur / 2)
    pd()

    dessinerLettre(lettre)


def dessinerLettre(lettre):
    if lettre == "A":
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

    if lettre == "H":
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


def dessinerSeq(sequence):
    columnCounter = 0
    lineCounter = 0
    sequenceAAcides = ''
    for j in range(0, len(sequence), 3):
        sequenceAAcides += lettreAa[sequence[j:j + 3]]
    print(sequenceAAcides)

    for i in sequenceAAcides:
        positionner(-180, 120)

        # desce até a linha certa

        pu()
        rt(90)
        fd(20 * lineCounter)
        lt(90)
        pd()

        # avança até a colonne
        pu()
        fd(columnCounter * 20)
        pd()
        carreLettre(20, i)
        columnCounter += 1

        if columnCounter > 14:
            columnCounter = 0
            lineCounter += 1


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


dessinerSeq("UAUUAUUAUGCCCAUCAUCAUCAUCAUCAUCAUCAUCAUCAUCAUCAUCAUCAUCAUCAUCAUCAUCAUCAUCAU")
