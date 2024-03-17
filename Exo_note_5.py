# Date: 2024-03-17
# Nom, prénom: Da Silva Faria, Stennio

# Question 1
def carre(taille):
    # Prend comme paramètre un entier e dessine un carré de même taille
    pensize(taille)
    fd(taille)


# Question 2
def triangle(base):
    # Prend comme paramètre un entier e dessine un triangle de même base

    # Positionner la tortue au but du triangle
    pu()
    bk(0.5 * base)
    pd()

    # Dessin du triangle
    for i in range(0, base):
        pensize(base - (base - i))
        fd(0.5)


# Question 3
def ligne(base, taille, n):
    # Prend comme paramètre des entiers positifs e dessine une suite de n sous
    # séquences altérant un triangle et un carré. Les carrés ont des cotés
    # taille et les triangles ont des bases base.

    # Positionner la tortue à la position (-100,0)
    pu()
    bk(100)
    pd()

    # Dessin de la suite
    for i in range(0, n):
        # Positionner la tortue au but du triangle
        pu()
        fd(0.5 * base)
        pd()

        # Dessin des images
        triangle(base)
        carre(taille)


# Question 4
def spirale(base, taille, nbFormes):
    # Dessine une spirale formée de flèches faites par un triangle et un carré
    # chaque. Le paramètre taille défine la taille des carrés, le paramètre
    # base défine la base des triangles. Le paramètre nbFormes défine la taille
    # maximale des démi-toues de la spirale. Tous les paramètres sont des
    # entiers positifs.

    for k in range(1, nbFormes + 1):  # Contrôle de nombre de flèches dessinées
        # à la fois

        for i in range(0, k):  # flèches avant le premier tour
            pu()
            fd(100)
            pd()
            ligne(base, taille, 1)
        lt(90)

        for j in range(0, k):  # flèches après le premier tour
            pu()
            fd(100)
            pd()
            ligne(base, taille, 1)
        lt(90)


# Question 5
def spiraleTournante(base, taille, nbForme, vAng):
    # Anime la spirale obtenue par la procédure spirale. vAng prend des entiers
    # et défine le nombre de dégrées que la spirale va être tourné à chaque fois.
    # La spirale se tourne en sens horaire si vAng positif et en sens anti-horaire
    # si vAng négatif.

    rotation = 0
    while True:
        clear()
        rt(rotation)
        spirale(base, taille, nbForme)
        ht()
        sleep(0.01)
        rotation += vAng

# carre(100)
# triangle(100)
# ligne(20,10,5)
# spirale(10,10,10)
# spiraleTournante(15,10,10,-2)