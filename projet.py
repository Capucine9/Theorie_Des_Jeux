

''' Fonctions '''

# Détermine si le jeu est à somme Nulles
def SomNul(liste):
    for i in liste:
        somme = 0
        for j in i:
            somme = somme + j
        if somme != 0:
           return 0
    return 1

# calcul des équilibres de Nash Purs
def NashPur(liste, nbStrat1, nbStrat2):
    equi = []
    n    = len(liste)
    i    = 0
    while i != n:
        aux  = liste[0]
        sauv = liste[0]
        for i

    return equi

# calcul des équilibres de Nash Mixtes
def NashMixte(liste):
    equi = []


''' Test des fonctions '''

test1 = [[1, -1],  [3, -3], [2, -2], [3, -3], [2, 3]]
test2 = [[2, -2], [3, -4, 1]]
test3 = [[2, -2], [3, -3]]

print(SomNul(test1))
print(SomNul(test2))
print(SomNul(test3))
