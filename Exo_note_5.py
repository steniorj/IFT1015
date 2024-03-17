# Date: 2024-03-17
# Nom, prénom: Da Silva Faria, Stennio

# Question 1

def carre(taille):
    pensize(taille)
    fd(taille)


# carre(100)


# Question 2

def triangle(base):
    pu()
    bk(0.5 * base)
    pd()
    for i in range(0, base):
        pensize(base - (base - i))
        fd(0.5)


# triangle(100)

# Question 3

def ligne(base, taille, n):
    pu()
    bk(100)
    pd()
    for i in range(0, n):
        pu()
        fd(0.5 * base)
        pd()
        triangle(base)
        carre(taille)


# ligne(20,10,5)

# Question 4

def spirale(base, taille, nbFormes)