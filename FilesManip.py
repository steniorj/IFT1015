def readFile(path):
    # Recebe um string com o nome do arquivo e sua extensao. Ex: 'texto.txt'
    # retorna o conteudo em string
    return open(path,'rb').read().decode('utf-8')

def writeFile(path,texte):
    f = open(path,'wb')
    f.write(texte.encode('utf-8'))
    f.close()

def decouperEnLignes(contenu):
    lignes = contenu.split('\n')
    if lignes[-1] == '':
        lignes.pop()
    return lignes

def tailleFichier(path):
    contenu = readFile(path)
    lignes = decouperEnLignes(contenu)
    print('caracteres =', len(contenu))
    print('lignes = ',len(lignes))

# tailleFichier('texto.txt'))

# def decouperEnLignes(contenu):
#     lignes = readFile(contenu) #varType = string
#     lignes2 = lignes.split('\r\n') #varType = list
#
#     if len(lignes2) == 1:
#         lignes = lignes.split('\n') #lista nao tem metodo .split()
#
#     if lignes[-1] == '':
#         lignes.pop()
#
#     return lignes
#
# # print(decouperEnLignes('texto.txt'))
#

def lireCSV(path):
    lignes = decouperEnLignes(readFile(path))
    resultat = []
    for ligne in lignes:
        resultat.append(ligne.split(','))

    return resultat

def ecrireCSV(path, matrice):
    contenu = ''

    for rangee in matrice:
        contenu += ','.join(rangee) + '\n'
    writeFile(path, contenu)

def calculerTotal(matrice):

    resultat = []
    for rangee in matrice:
        nom = rangee[0]
        prenom = rangee[1]
        note1 = int(rangee[2])
        note2 = int(rangee[3])
        note3 = int(rangee[4])
        somme = note1 + note2 + note3
        resultat.append([nom, prenom, str(somme)])
    return resultat


def valNum(tab):
    resultat = []
    for elem in tab:
        resultat.append(int(elem))
    return resultat

def somme(tab):
    s = 0
    for elem in tab:
        s += elem
    return s

def calculerTotal(matrice):
    resultat = []
    s = 0
    for rangee in matrice:
        nom = rangee[0]
        prenom = rangee[1]
        notes = valNum(rangee[2:])
        s = somme(notes)
        resultat.append([nom, prenom, str(s)])
    return resultat

# notes = lireCSV('notes.csv')
#
# total = calculerTotal(notes)
#
# ecrireCSV('total.csv', total)

#
# def double(n):
#     return 2*n
#
# for x in map(double, range(6)):
#     print(x)
#
# tab1 = list(map(double, range(6)))
# print(tab1)
#
# tab2 = list(map(double, 'ABCDE'))
#
# print(tab2)
#
# def barre(n): return n*'#'
#
# print('\n'.join(map(barre, range(1,6))) )
# print('\n'.join(map(barre, range(6,1,-1))) )

l1 = [1,3,5,6]
l2 = [0,4,8,9]

def fusion(liste1,liste2):
    resultat = []
    i = 0
    j = 0

    while i < len(liste1) and j < len(liste2):
        if liste1[i] < liste2[j]:
            resultat.append(liste1[i])
            i += 1
        else:
            resultat.append(liste2[j])
            j += 1
    print(i)
    print(j)
    while i < len(liste1):
        resultat.append(liste1[i])
        i += 1

    while j < len(liste2):
        resultat.append(liste2[j])
        j += 1
    return resultat
# print(fusion(l1,l2))

notes1 = lireCSV('notes1.csv')
notes2 = lireCSV('notes2.csv')

def comparerId(id1,id2):
    print(id1)
    print(id1[1])
    if id1[0] < id2[0]: return -1
    if id1[0] < id2[0]: return 1
    if id1[1] < id2[1]: return -1
    if id1[1] > id2[1]: return 1
    return 0
# print(comparerId(notes1[0],notes2[0]))
# print(notes1[0])

def tableauNul(n):
    return [0]*n

print(notes1)

# def decouperEnLignes(contenu):
#     lignes = contenu.split('\n')
#     if lignes[-1] == '':
#         lignes.pop()
#     return lignes
#
# def tailleFichier(path):
#     contenu = readFile(path)
#     lignes = decouperEnLignes(contenu)
#     print('caracteres = ', len(contenu))
#     print('lignes =', len(lignes))
#
#
# def lireCSV(path):
#     lignes = decouperEnLignes(readFile(path))
#     resultat = []
#     for ligne in lignes:
#         resultat.append(ligne.split(','))
#     return resultat
#
# notes = lireCSV('notes.csv')
#
# def ecrireCSV(path,matrice):
#     contenu = ''
#     for rangee in matrice:
#         contenu += ','.join(rangee) + '\n'
#     writeFile(path,contenu)
#
# notes = lireCSV('notes.csv')
#
# #ecrireCSV('copie.csv','notes.csv')
#
# def calculerTotal(matrice):
#     resultat = []
#     for rangee in matrice:
#         nom = rangee[0]
#         prenom = rangee[1]
#         note1 = int(rangee[2])
#         note2 = int(rangee[3])
#         note3 = int(rangee[4])
#         resultat.append([nom, prenom, str(note1 + note2 + note3)])
#     return resultat
#
# notes = lireCSV('notes.csv')
# total = calculerTotal(notes)
# #ecrireCSV('total.csv',total)
#
#
# def valNum(tab):
#     resultat = []
#     for elem in tab:
#         resultat.append(int(elem))
#     return resultat
#
# def somme(tab):
#     s = 0
#     for elem in tab:
#         s += elem
#     return s
#
# def calculerTotal(matrice):
#     resultat = []
#     for rangee in matrice:
#         nom = rangee[0]
#         prenom = rangee[1]
#         notes = rangee[2:]
#         total = somme(valNum(notes))
#         resultat.append([nom, prenom, str(total)])
#
#     return resultat
#
# notes = lireCSV('notes.csv')
# total = calculerTotal(notes)
#
# def cols2Rec(cols):
#     return struct(id = struct(nom = cols[0], prenom = cols[1]), notes = valNum(cols[2:]))
#
# def mat2RecArray(mat):
#     resultat = []
#     for rangee in mat:
#         resultat.append(cols2Rec(rangee))
#     return resultat
#
#
#
#
#
#
# def double(n):
#     return 2*n
#
# tab1 = list(map(double,range(6)))
#
# tab2 = list(map(double,'ABCDE'))
#
# def fusion(liste1, liste2):
#
#     resultat = []
#     i = 0
#     j = 0
#
#     while i < len(liste1) and j < len(liste2):
#         if liste1[i] < liste2[j]:
#             resultat.append(liste1[i])
#             i +=1
#         else:
#             resultat.append(liste2[j])
#             j += 1
#
#     while i < len(liste1): resultat.append(liste1[i]) ; i +=1
#     while j < len(liste2): resultat.append(liste2[j]) ; j +=1
#     return resultat
#
# def comparerId(id1, id2):
#     if id1 < id2: return -1
#     if id1 > id2: return 1
#     if id1 < id2: return -1
#     if id1 > id2: return 1
#     return 0
#
# def comparerRec(rec1,rec2):
#     return comparerId(rec1, rec2)
#
#
#
