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

# Converti un tableau 1D en tableau 2D
def convert(liste, col):
    i   = 0
    tab = []
    aux = []
    for i in range(len(liste)):
       aux.append(liste[i])
       if (i+1)%col == 0:
          print(aux)
          tab.append(aux)
          aux =[]
    return tab

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

# Détermine si le jeu est à somme Nulles
def somNul(liste):
    for i in liste:
        somme = 0
        for j in i:
            somme = somme + j
        if somme != 0:
           return "Ce Jeu n'est pas un jeu à somme nulles"
    return "Ce Jeu est un jeu à somme nulles"

# Détermine les coordonnées dans un tableau 2D à partir de la position dans un tableau 1D
def coord(dim, pos):
    ligne = 0
    col   = 0
    if dim > pos:
        return[0, pos]

    aux = pos % dim
    tmp = pos - aux

    while ligne*dim != tmp:
        ligne += 1

    col = aux

    return [ligne, col]

# Déterminer les stratégies dominantes
def domi(liste, dim1, dim2):
    tab  = convert(liste, dim2)
    i    = 0

    for
    jd  = []                            # Liste pour chaque stratégie du joueur1, des stratégies par qui elle est dominé
    jsd = []                            # Liste pour chaque stratégie du joueur1, des stratégies par qui elle est Strictement dominé
    jD  = []
    jsD = []
  # Parcours des stratégies pour le Joueur 1
    for i in range(dim1):
        dom  = []
        sdom = []
        for k in range(dim1):
          # Variable déterminant si la stratégie est dominée ou Strictement dominée (1=oui, 0=indéterminer, -1=non)
            d   = 0
            sd  = 0

            D   = 0
            sD  = 0
            for j in range(dim2):
                if k != i:
                   if tab[i][j][0] < tab[k][j][0]:
                      sD = -1
                      D  = -1
                      if sd == 0:
                          sd = 1
                      if d == 0:
                          d = 1
                   elif tab[i][j][0] > tab[k][j][0]:
                      sd = -1
                      d  = -1
                      if sd == 0:
                        sd = 1
                      if d == 0:
                        d = 1
                   else:
                      sd = -1
                      sD = -1

           # Attribution pour savoir si la stratégie est dominée ou dominante
            if sd == 1:
                sdom.append(k)
            if d == 1:
                dom.append(k)

        j1d.append(dom)
        j1sd.append(sdom)

  # Parcours des stratégies pour le Joueur 2
    for j in range(0, dim2):
        dom  = []
        sdom = []
        for k in range(0, dim2):
          # Variable déterminant si la stratégie est (Strictement) dominée ou (Strictement) dominante (1=oui, 0=indéterminer, -1=non)
            d   = 0
            sd  = 0
            for i in range(0, dim1):
                if k != j:
                   if tab[i][j][1] < tab[i][k][1]:
                      if sd == 0:
                         sd = 1
                      if d == 0:
                         d = 1
                   elif tab[i][j][1] > tab[i][k][1]:
                      sd = -1
                      d  = -1
                   else:
                      sd = -1
          # Attribution pour savoir si la stratégie est dominée ou dominante
            if sd == 1:
                sdom.append(k)
            if d == 1:
                dom.append(k)

        j2d.append(dom)
        j2sd.append(sdom)

    return j1d, j1sd, j2d, j2sd

# calcul des équilibres de Nash Purs
def nashPur(col, nbJ):
    eNash  = []                                     # Liste des Équilibres de Nash Purs
    pos    = 0                                      # Index dans la liste des stratégies possible

    # Nombre de possibilité restante d'avoir un Équilibre de Nash Pure
    possib = liste

    while len(possib) != 0:
        aux = liste[coord[0]*dim2+coord[1]]
        tmp = coord(pos)
        # parcours des stratégies du joueur 2
        deb = tmp[0]*dim2
        fin = (tmp[0]+1)*dim2
        joueur = 2
        if joueur == 1:
           aux = vuJ1
        elif joueur == 2:
           aux = vuJ2
        elif joueur == 3:
           aux = vuJ3
        elif joueur == 4:
           aux = vuJ4
        elif joueur == 5:
           aux = vuJ5

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


''' Test des fonctions '''

test1 = [[1, -1, 1, 2, -3], [3, -3, 2, -4, 2], [2, -2, 3, -5, 2], [4, 4, -5, -5, 2], [5, 6, -7, -3, -1], [6, 3, -3, -3, -3],  [-1, -9, 5, 4, 1]]
test2 = newListe(1, 3, [3, 2, 3], [-3, 3])
test3 = [[1, -1],  [3, -3], [6, -2], [4, 4], [5, 6], [6, 3],  [1, 9], [2, 8], [1, 4]]

#jeu = convert(test2, 6)
GenPosStrat(test2, [3, 2, 3])
print(posStrat)

'''
dom1, sdom1, dom2, sdom2 =domi(test3, 3, 3)
print("Joueur 1:")
print("dominée:")
print(dom1)
print("Strictement dominée:")
print(sdom1)

print("\n Joueur 2:")
print("dominée:")
print(dom2)
print("Strictement dominée:")
print(sdom2)
'''
