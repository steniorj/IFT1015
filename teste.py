
tableauTest = [['Chr1', 'gene', '123270', '124917'], ['Chr1', 'exon', '123270', '124917'], ['Chr1', 'exon', '123542', '123712'], ['Chr1', 'exon', '123859', '124917'], ['Chr1', 'gene', '123270', '124917'], ['Chr1', 'exon', '123270', '123404'], ['Chr1', 'exon', '123542', '123712'], ['Chr1', 'exon', '123859', '124917']]
"""Chr1 gene 116109 116466
Chr1 exon 116109 116466
Chr1 exon 116450 116862
Chr1 exon 116854 117076"""

def intronPos(tab):
    exon1 = []
    exon2 = []
    
    geneDebut = 0
    geneFin = 0

    flag = False
    exon1temp = False

    introns = []

    for i in tab:
         if i[1] == "gene":
               exon1 = []
               exon2 = []

               geneDebut = int(i[2])
               geneFin = int(i[3])

               flag = False
         
         if (i[1] == "exon") and (int(i[2]) == geneDebut) and (int(i[3]) == geneFin):
              flag == True
         
         if (i[1] == "exon") and (flag == False):
               exon1.append(int(i[2]))
               exon1.append(int(i[3]))

         if (i[1] == "exon") and (flag == False):
               
               if int(i[2]) > exon1[1]:
                  exon2.append(int(i[2]))
                  exon2.append(int(i[3]))
                  
                  if exon2[0] > exon1[1]:
                       introns.append(str(i[0]) + '\t' + str((exon1[1]+1)) + "\t" + str(exon2[0]-1) + '\n')
                       
                       exon1 = exon2.copy()
                       exon2 = []
    return ''.join(introns)
        


introns = intronPos(tableauTest)
print(introns)


















# def intronPos(tab):
#     # réçoit un tableau avec des positions des genes et des exons pour extraire les positions des introns dans le format:
#     # Input: [['gene', '454855', '455601'], ['exon', '454855', '455601']]
#     # Output: liste de tuples avec positions de début et fin des introns: [(397303, 397069), (401374, 401522)]
#     geneDebut = 0
#     geneFin = 0

#     intronDebut = 0
#     intronFin = 0

#     flag = False

#     introns = []

#     for i in tab:
      
#       if i[1] == 'gene':
#         flag = False
#         geneDebut = int(i[2])
#         geneFin = int(i[3])
      
#       if i[1] == 'exon':
         
#          if (int(i[2]) == geneDebut) and (int(i[3]) == geneFin):
#             flag = True
         
#          if (int(i[3]) > geneFin) or (int(i[2]) < geneDebut):
#             flag = True
      
#          if (int(i[2])) > geneDebut and (flag == False):
#             intronFin = int(i[2])
#             print(intronFin)
#             if intronDebut > 0:
#                introns.append(str(intronDebut) + '\t' + str(intronFin) + '\n')
#             intronDebut = 0
#             intronFin = 0

#          if (int(i[3]) < geneFin) and (flag == False):
#             print(i[3], 'filhadaputa')
#             intronDebut = int(i[3])
            

#     return ''.join(introns)

# bora = intronPos(tableauTest)
# print(bora)

# """tab = [0,1,2,3,4,5]

# for i in tab:
#     if i == 1:
#         pass
#     else:
#         print(i)"""