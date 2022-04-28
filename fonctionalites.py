from random import randint

''' Liste des variables globals '''

# tableau des Stratégies du point de vue de chaque joueur
posStrat = []

''' Liste des Fonctions de test '''
# Génére un jeu nul(1) ou non(0) de nbJoueurs joueurs,
# avec strat[i] stratégie pour le joueur i+1, et des valeurs compris dans l'intervale
def newListe(nul, nbJoueurs, strat, inter):
    liste = []
    nbCol = 1
    for i in strat[1:]:
        nbCol = nbCol * i
    for s in range(strat[0]):
        for i in range(nbCol):
            aux = []
            if nul == 1:
                somme = 0
            for k in range(nbJoueurs):
                tmp = randint(inter[0], inter[1])
                if nul == 1:
                    if k == nbJoueurs-1:
                        if somme == 0:
                            tmp = 0
                        else:
                            tmp = -somme
                    else:
                        somme += tmp
                aux.append(tmp)
            liste.append(aux)
    return liste


''' Liste des Fonctions utiles '''

# Donne un tableau comparant les nbStrats stratégies du joueurs n°numJ
def GenPosStrat(liste, strat):
    aux = 1
    n   = len(strat)
    for i in range(1, n):
        aux = aux * strat[i]

    stratJ = [1]*n
    for _ in range(0, len(liste)):
        tmp = []
        for j in range(n):
            tmp.append(stratJ[j])

        posStrat.append(tmp)

        if stratJ[n-1] >= strat[n-1]:
            stratJ[n-1] = 1
            opt = 0
            i = n-2
            while opt != 1 or i > 0:
                if stratJ[i] < strat[i]:
                   stratJ[i] += 1
                   opt = 1
                else:
                   stratJ[i] = 1
                i -= 1
        else:
           stratJ[n-1] = stratJ[n-1] + 1

# Obtenir les stratégie
def getStrat(liste, J, strat):
    result = []
    for i in range(len(liste)):
        if posStrat[i][J-1] == strat:
            aux = [posStrat[i], liste[i]]
            result.append(aux)
    return result


# Détermine si le jeu est à somme Nulles
def somNul(liste):
    for i in liste:
        somme = 0
        for j in i:
            somme = somme + j
        if somme != 0:
           return "Ce Jeu n'est pas un jeu à somme nulles"
    return "Ce Jeu est un jeu à somme nulles"

# Déterminer les stratégies dominantes
def domi(liste, strat):
    nbJ  = len(strat)
    i    = 0
    total = []                          # Liste contenant toute les stratégies dominée de chaque joueur

    for i in range(nbJ):
        jd  = []                            # Liste pour chaque stratégie du joueur, des stratégies par qui elle est dominé
        jsd = []                            # Liste pour chaque stratégie du joueur, des stratégies par qui elle est Strictement dominé
        jD  = []                            # Liste pour chaque stratégie du joueur, des stratégies qu'elle domine
        jsD = []                            # Liste pour chaque stratégie du joueur, des stratégies qu'elle domine Strictement

        for s1 in range(strat[i]):
            dom  = []
            sdom = []
            Dom  = []
            sDom = []
            tmp1 = getStrat(liste, i+1, s1+1)
            print(s1)
            for s2 in range(strat[i]):
                if s1 != s2:
                     tmp2 = getStrat(liste, i+1, s2+1)
                   # Variable déterminant si la stratégie est dominée ou Strictement dominée (1=oui, 0=indéterminer, -1=non)
                     d   = 0
                     sd  = 0
                     D   = 0
                     sD  = 0

                     for j in range(strat[i]):
                        if tmp1[j][1][i] < tmp2[j][1][i]:
                               D  = -1
                               sD = -1
                               if sd == 0:
                                  sd = 1
                               if d == 0:
                                  d = 1
                        elif tmp1[j][1][i] > tmp2[j][1][i]:
                            sd = -1
                            d  = -1
                            if sD == 0:
                               sD = 1
                            if D == 0:
                               D = 1
                        else:
                            sd = -1
                            sD = -1

                     if sd >= 0:
                        sdom.append(s2)
                     if d >= 0:
                        dom.append(s2)
                     if sD >= 0:
                        sDom.append(s2)
                     if D >= 0:
                        Dom.append(s2)
            jd.append(dom)
            jsd.append(sdom)
            jD.append(Dom)
            jsD.append(sDom)
        aux = [jsd, jd, jsD, jD]
        total.append(aux)
    return total

# calcul des équilibres de Nash Purs
def nashPur(liste, strat):
    eNash  = []                                     # Liste des Équilibres de Nash Purs
    pos    = 0                                      # Index dans la liste des stratégies possible

  # Nombre de possibilité restante d'avoir un Équilibre de Nash Pure
    possib = liste

    while len(possib) != 0:
        J   = 0

        for j in range(deb, fin):
            if liste[j][1] > liste[pos][1]:
                possib.remove(pos)
                pos = j
            elif liste[j][1] < liste[pos][1]:
                possib.remove(j)

      # parcours des stratégies du joueur 2
        deb = tmp[0]*dim2
        fin = (tmp[0]+1)*dim2
        for j in range(deb, fin):
            if liste[j][1] > liste[pos][1]:
                possib.remove(pos)
                pos = j
            elif liste[j][1] < liste[pos][1]:
                possib.remove(j)
        sauv = liste[coord[0]*dim2+coord[1]]
    return eNash

# calcul des équilibres de Nash Mixtes
def nashMixte(liste):
    equi = []

'''' Test des fonctions  '''


test1 = [[1, -1, 1, 2, -3], [3, -3, 2, -4, 2], [2, -2, 3, -5, 2], [4, 4, -5, -5, 2], [5, 6, -7, -3, -1], [6, 3, -3, -3, -3],  [-1, -9, 5, 4, 1]]
test2 = newListe(1, 3, [3, 2, 3], [-3, 3])
test3 = [[1, -1], [3, -3], [6, -2],
         [4,  4], [5,  6], [6,  3],
         [1,  9], [2,  8], [1,  4]]

strat = [3, 3]
var   = test3
print(var)

GenPosStrat(var, strat)
tt = domi(var, strat)
print("Joueur 1:")
print("dominée:")
print(tt[0][1])
print("Strictement dominée:")
print(tt[0][0])

print("Joueur 2:")
print("dominée:")
print(tt[1][1])
print("Strictement dominée:")
print(tt[1][0])
'''
print("Joueur 3:")
print("dominée:")
print(tt[2][1])
print("Strictement dominée:")
print(tt[2][0])
'''
