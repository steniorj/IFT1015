roerewur


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


def dessinerSeq(sequence):
    coluna = 0
    lineCounter = 0
    for i in sequence:
        positionner(-180, 120)

        # desce até a linha certa

        pu()
        rt(90)
        fd(20 * lineCounter)
        lt(90)
        pd()

        # avança até a coluna
        pu()
        fd(coluna * 20)
        pd()
        carreLettre(20, i)
        coluna += 1

        if coluna > 14:
            coluna = 0
            lineCounter += 1

        print(coluna)


dessinerSeq("XXXXXYYYYYXXXXXZZZZZ")
