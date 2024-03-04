def dessinerSeq(sequence):
    columnCounter = 0
    lineCounter = 0
    for i in sequence:
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
