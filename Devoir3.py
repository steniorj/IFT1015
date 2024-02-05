##Nom, Prénom ; Date
#Da Silva Faria, Stennio; 2024/fev/04

## Commentaire général
#The third exercise to the IFT1015 course. Winter/2024

# First question:

## Déclaration des variables globales, constantes

#a, b and c being the three integers of a Pythagoric triplet between 1 and 100, given that a <b < c
a = 1
b = 2
c = 3
biggest_Integer_Allowed = 100 #biggest integer allowed
triplet_Calculation = a**2 + b**2 #triplet calculation
repeter = True #Repeat variable for the repeat lopp


## Calcul, commentaires détaillés nécessaires seulement
def pythagoric_Triplets(a, b, c, biggest_Integer_Allowed=100, increasing_While=False, decreasing_While=False, repeat_Loop=False, for_Loop=False):
    ### Function to calculate the pythagoric triplets. The arguments set the type of loop used to perform the calculations.

    if increasing_While == True: #First answer. While loop: increasing
        while c <= biggest_Integer_Allowed:

            triplet_Calculation = a**2 + b**2

            if c**2 == triplet_Calculation:
                print(c,'² =' , a, '² +', b, '²')

            c +=1
            if c > 100: # c at its maximum value. Increase b and restart c respecting a < b < c
                b += 1
                c = b+1

            if b == 100: # b and c at its maximum value. Increase a and restart b and c respecting a < b < c
                a += 1
                b = a+1
                c = b+1

            if a > 98 :
                c = 101

    if decreasing_While == True: #Second answer. While loop: decreasing
        while c >= 3:
            triplet_Calculation = a**2 + b**2

            if c**2 == triplet_Calculation:
                print(c,'² =' , a, '² +', b, '²')
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

    if repeat_Loop == True: #Third answer: While loop, repeat, increasing
        repeter = True
        while repeter:
            triplet_Calculation = a ** 2 + b ** 2

            if c ** 2 == triplet_Calculation:
                print(c,'² =' , a, '² +', b, '²')

            c += 1
            if c > 100:
                b += 1
                c = b + 1

            if b == 100:  # b and c at its maximum value. Increase a and restart b and c respecting a < b < c
                a += 1
                b = a + 1
                c = b + 1

            repeter = a <= 98

    if for_Loop == True: # Fourth answer
        for i in range (0,1000001): # range large enough to assure all the solutions are calculated
            triplet_Calculation = a ** 2 + b ** 2

            if c ** 2 == triplet_Calculation:
                print(c,'² =' , a, '² +', b, '²')

            c += 1

            if c > 100:  # c at its maximum value. Increase b and restart c respecting a < b < c
                b += 1
                c = b + 1

            if b == 100:  # b and c at its maximum value. Increase a and restart b and c respecting a < b < c
                a += 1
                b = a + 1
                c = b + 1

            if a > 98: # ending the loop after the last solution was calculated
                break

## Affichage
# First answer:
print('Les triplets de d\'entiers pythagoriciens entre 1 et 100 calculés par boucle "Tant-Que" acendantes en format c² = a² + b² sont:'), pythagoric_Triplets(1,2,3, increasing_While=True)

print('-='*10)

# Second answer:
print('Les triplets de d\'entiers pythagoriciens entre 1 et 100 calculés par boucle "Tant-Que" descendantes en format c² = a² + b² sont:') , pythagoric_Triplets(98,99,100, decreasing_While=True)

print('-='*10)

# Third answer:
print('Les triplets de d\'entiers pythagoriciens entre 1 et 100 calculés par boucle "Répeter" ascendante en format c² = a² + b² sont:') , pythagoric_Triplets(1,2,3, repeat_Loop=True)

print('-='*10)

# Fourth answer:
print('Les triplets de d\'entiers pythagoriciens entre 1 et 100 calculés par boucle "for" ascendante en format c² = a² + b² sont:') , pythagoric_Triplets(1,2,3, for_Loop=True)

print('-='*10)

## Second question: Armstrong numbers with three digits

## Calcul, commentaires détaillés nécessaires seulement

print('Les entiers d\'Armstrong qui s\'écrivent avec 3 chiffres sont:')
for n in range(100, 1000):
    next_Number = n // 10 # removes the last digit from the current number
    sum = 0 # stores result of the digit's sum
    original_Number = n # stores the original number to be analyzed

    while next_Number > 0:
        last_Digit = n % 10 # stores the last digit
        sum += (last_Digit**3)
        next_Number = n // 10
        n = next_Number

    ## Affichage

    if original_Number == sum:
        print(original_Number)


# Après avoir terminé votre code, renommez votre fichier en fonction de la
# nature de calcul effectué dans votre programme.