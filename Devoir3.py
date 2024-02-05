##Nom, Prénom ; Date
#Da Silva Faria, Stennio; 2024/fev/04

## Commentaire général
#The third exercise to the IFT1015 course. Winter/2024

## Déclaration des variables globales, constantes
#For the first question:

#a, b and c being the three integers of a Pythagoric triplet between 1 and 100, given that a <b < c
a = 1
b = 2
c = 3
biggest_Integer_Allowed = 100 #biggest integer allowed
triplet_Calculation = a**2 + b**2 #triplet calculation


## Calcul, commentaires détaillés nécessaires seulement
##First question:
def pythagoric_Triplets(a, b, c, biggest_Integer_Allowed=100, increasing_While=False, decreasing_While=False, repeat_Loop=False, for_Loop=False):
    ### Function to calculate the pythagoric triplets. The arguments sets the type of loop used to perform the calculations.

    if increasing_While == True: #First answer. While loop: increasing
        while c <= biggest_Integer_Allowed:

            triplet_Calculation = a**2 + b**2

            if c**2 == triplet_Calculation:
                print('c² = a² + b² //' ,c,'² =' , b, '² +', a, '²' , '//', c**2, '=', b**2, '+', a**2, '//', triplet_Calculation, c**2,  'um triplet')

            c +=1
            if c > 100: #
                b += 1
                c = b+1


            if b == 100: #b and c at its maximum value. Increase a and restart b and c respecting a < b < c
                a += 1
                b = a+1
                c = b+1
            if a > 98 :
                c = 101

    if decreasing_While == True: #Second answer. While loop: decreasing
        while c >= 3:
            triplet_Calculation = a**2 + b**2

            if c**2 == triplet_Calculation:
                print('c² = a² + b² //' ,c,'² =' , b, '² +', a, '²' , '//', c**2, '=', b**2, '+', a**2, '//', triplet_Calculation, c**2,  'um triplet')
                a -= 1
                if a == 1:
                    b -= 1
                    a = b-1
            else:
                a -= 1
                if a == 1:
                    b -= 1
                    a = b - 1
            if a <1:
                b -= 1
                a = b-1
            if b == 1:
                c -=1
                b = c-1
                a = b-1
            if c == 3 and b <2:
                c = 2
        # if repeat_Loop = True:





## Affichage
#First answer:
print('Les triplets de d\'entiers pythagoriciens entre 1 et 100 calculés par boucle "Tant-Que" acendantes sont:') , pythagoric_Triplets(1,2,3, increasing_While=True)

#Second answer:
print('Les triplets de d\'entiers pythagoriciens entre 1 et 100 calculés par boucle "Tant-Que" descendantes sont:') , pythagoric_Triplets(98,99,100, decreasing_While=True)

#Third answer:
print('Les triplets de d\'entiers pythagoriciens entre 1 et 100 calculés par boucle "Répeter" ascendante sont:') , pythagoric_Triplets(98,99,100, decreasing_While=True)
# Après avoir terminé votre code, renommez votre fichier en fonction de la
# nature de calcul effectué dans votre programme.