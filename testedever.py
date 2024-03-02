def funcao_fdp(annee):

    g = annee % 19
    c = annee // 100
    d = c-c//4
    e = (8 * c + 13) // 25
    i = (19 * g + 15) % 30
    h = (d-e+19*g+15) % 30
    k = h // 28
    p = 29 // (h+1)
    q = (21 - g) // 11
    i = h - k * (1 - k * p * q)
    j = (annee + annee // 4 + i + 2 - d) %7
    r = 28+i-j
    if r > 31 and r < 41:
        return "0"+str(r-31) + '-04-'+str(annee)

    elif r>= 41:
        return str(r - 31) + '-04-' + str(annee)

    else:
        return str(r) + '-03-'+str(annee)

"C" : "G"

print(funcao_fdp(1958))

# # print(funcao_fdp(2018))
# # for i in range(2000, 2100):
# #     print(i,funcao_fdp(i))
#
# def teste_fonction_fdp():
#
#     #1 cas général:
#     assert funcao_fdp(2024) == 31
#     #2 la date la plus tôt possible : le 22 mars
#     assert funcao_fdp(1818) == 22
#     #3 la date la plus tard possible : le 25 avril
#     assert funcao_fdp(1943) == 56
#     #4 vérification si la correction pour les années bissextiles est correcte:
#     assert funcao_fdp(1900) == 46
#     #5 vérifier si le nombre d'Or a été calculé pour un cycle ménotique de 19 ans
#     assert funcao_fdp(2013) == 31 and funcao_fdp(2014) == 51
#
# teste_fonction_fdp()
#
# # print (2024/19, 2024%19, 2024//19)
#
# #
# # print(r)
# #
# # print(type(14/02/2024))
# #
#
# #teste do assert
# # def teste(n):
# #     return n*n
# #
# # def test_teste():
# #     assert teste(0) == 0
# #     assert teste(-3) == 9
# #
# # test_teste()
