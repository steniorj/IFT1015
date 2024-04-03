tab = [1,2,3]

def renv(tab):
    if len(tab) <= 1:
        return [tab.copy()]
    resultat = []
    for i in range(len(tab)):
        tabSansX = tab.copy()
        tabSansX.pop(i)
        print(tabSansX)
        for p in renv(tabSansX):
            print(p)
    return tab

renv(tab)