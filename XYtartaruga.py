#odigo pra rodar no codeboot

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
