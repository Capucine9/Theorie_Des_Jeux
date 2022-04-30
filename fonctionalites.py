from random import randint

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
    posStrat = []
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
    res = []
    for k in range(len(liste)):
        val = [posStrat[k], liste[k]]
        res.append(val)
    return res

# Obtenir la stratégie strat du joueur J
def getStrat(liste, J, strat):
    result = []
    for i in range(len(liste)):
        if liste[i][0][J] == strat:
            aux = [liste[i][0], liste[i][1]]
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
            tmp1 = getStrat(liste, i, s1+1)
            for s2 in range(strat[i]):
                if s1 != s2:
                     tmp2 = getStrat(liste, i, s2+1)
                   # Variable déterminant si la stratégie est dominée ou Strictement dominée (1=oui, 0=indéterminer, -1=non)
                     d   = 0
                     sd  = 0
                     D   = 0
                     sD  = 0

                     for j in range(len(tmp2)):
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

                     if sd > 0:
                        sdom.append(s2)
                     if d  > 0:
                        dom.append(s2)
                     if sD > 0:
                        sDom.append(s2)
                     if D  > 0:
                        Dom.append(s2)
            jd.append(dom)
            jsd.append(sdom)
            jD.append(Dom)
            jsD.append(sDom)
        aux = [jsd, jd, jsD, jD]
        total.append(aux)
    return total

def dans(liste, val):
    for i in liste:
        if i == val:
            return True
    return False

# calcul des équilibres de Nash Purs
def nashPur(liste, strat):
    eNash  = []                                   # Liste des Équilibres de Nash Purs
    nbJ    = len(strat)
    possib = list(liste)
    cmp    = len(liste)*nbJ
    actu   = liste[0]
    sauv   = liste[0]
    casu   = 0
    j      = 0

    while cmp >= 0:
        aux = getStrat(liste, j, actu[0][j])
        j   = (j+1)%len(strat)
        for i in range(len(aux)):
           if aux[i][1][j] > actu[1][j]:
               if dans(possib, actu):
                  possib.remove(actu)
                  cmp -= 1
               actu = aux[i]
           else:
               if dans(possib, aux[i]):
                  possib.remove(aux[i])
                  cmp -= 1
        if actu == sauv:
            casu += 1
        else:
            casu = 0
            sauv = actu
        if casu >= nbJ:
            if not dans(eNash, actu):
               eNash.append(actu)
            if dans(possib, actu):
               possib.remove(actu)
            if len(possib) != 0:
               actu = possib[0]
            casu = 0
            cmp -= 1
    return eNash

# calcul des équilibres de Nash Mixtes
def calculNashMixte(liste):
    equi = []
    val  = []
    # 1q + 2q + 3(1-q) + 4(1-q)
    for j in range(2):
        tmpJ = []
        for s in range(2):
            aux = getStrat(liste, j, s+1)
            tmpJ.append([aux[0][1][j], aux[1][1][j]])
        val.append(tmpJ)
    print("val: ", val)
    div = []
    for i in val:
        print("i: ", i)
        tmp = (i[0][0]-i[0][1]) - (i[1][0]-i[1][1])
        print(tmp)
        div.append(tmp)
    print("div: ", div)
    q   = (val[0][1][1] - val[0][0][1])/ div[0]
    p   = (val[1][1][1] - val[1][0][1])/ div[1]

    aux = [round(p, 4), round(1-p, 4)]
    equi.append(aux)
    aux = [round(q, 4), round(1-q, 4)]
    equi.append(aux)
    return equi

def nashMixte(liste, proba):
    n     = 100
    tmp   = calculNashMixte(liste)
    seuil = tmp[1][0]
    gain  = 0
    for _ in range(n):
        alea1 = randint(0, 100)
        alea2 = randint(0, 100)
        if alea1 > proba[0]*10:
            aux = getStrat(liste, 0, 2)
        else:
            aux = getStrat(liste, 0, 1)

        print(aux)
        if alea2 > int(seuil*10):
            gain += aux[1][1][1]
        else:
            gain += aux[0][1][1]
        print(gain)

    return gain/n


'''' Test des fonctions  '''


test1 = [[1, 2, 3], [4, 2, 3],
         [4, 5, 6], [2, 9, 4],
         [2, 3, 2], [4, 5, 6]]

test2 = newListe(1, 3, [3, 2, 3], [-3, 3])
test3 = [[1, -1], [3, -3], [6, -2],
         [4,  4], [5,  6], [6,  3]]
test4 = [[2, 1], [0, 0],
         [0, 0], [1, 2]]
test5 = [[-1, -1], [-5,  0],
         [ 0, -5], [-3, -3]]

strat = [2, 2]
var   = test4
aux = GenPosStrat(var, strat)
print(aux)

print("Équilibre:")
print(nashPur(aux, strat))

print("Équilibre Mixte:")
print(nashMixte(aux, [1/3, 2/3]))

'''
tt = domi(aux, strat)
print("Joueur 1:")
print("dominée:")
print(tt[0][1])
print("Strictement dominée:")
print(tt[0][0])
print("domine:")
print(tt[0][3])
print("Strictement domine:")
print(tt[0][2])

print("Joueur 2:")
print("dominée:")
print(tt[1][1])
print("Strictement dominée:")
print(tt[1][0])
print("domine:")
print(tt[0][3])
print("Strictement domine:")
print(tt[0][2])

print("Joueur 3:")
print("dominée:")
print(tt[2][1])
print("Strictement dominée:")
print(tt[2][0])
'''
