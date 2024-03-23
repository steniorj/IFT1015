#Ex 1
tableau = [0,1,2,3,4]

def somme(tableau):
    s = 0
    for i in tableau:
        s += i
    return s

def moyenne(tableau):
    s = 0
    for i in tableau:
        s += i
    return s/(len(tableau))

tab_somme = somme(tableau)
tab_moyenne = moyenne(tableau)


#Ex 2

def occurences(tableau,val):
    nombre = []
    for i in tableau:
        if val == i:
            nombre.append(i)

    return len(nombre)

# print(occurences(tableau,11))

#Ex 3

def tabEgal(tableau1, tableau2):
    if len(tableau1) != len(tableau2):
        return False
    else:
        for i in range(len(tableau1)):
            if tableau1[i] not in tableau2:
                return False
        return True
tableau1 = [0,1,2,3,5,6]
tableau2 = [0,1,2,5,3,6]

# print(tabEgal(tableau1, tableau2))

#Ex 4

def histogramme(tableau):
    hist = [0,0,0,0,0]
    for i in range(len(tableau)):
        hist[tableau[i]] += 1
    return hist

tab = [3,2,2,3,0,2]
# print(histogramme(tab))