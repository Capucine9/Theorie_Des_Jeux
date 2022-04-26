from tkinter import *
from tkinter.ttk import *

# Importation d'autres fichiers Python
import Fen_strat
import Fen_nom
import Nb_joueur
import Nb_strat
import Changer_page
import Bouton

# numero du joueur dont on recupere les noms des strategies
strat_joueur_nb = 1

# Liste contenant les noms des joueurs
nom_joueur =[]

############################################################################
def joueur():
    global nom_joueur
    
    for i in range (len(Fen_nom.list_joueur)):
        nom_joueur.append(Fen_nom.list_joueur[i].get())
    print ("nom_joueur", nom_joueur)
    
############################################################################
def strat():
    global strat_joueur_nb
    global nom_strat

    ## Le bouton : "Les autres joueurs souhaitent avoir les memes strategies" n'a pas ete selectionne
    if Bouton.valeur_bouton_strat.get() == False :
        if strat_joueur_nb <= Nb_joueur.nb_joueurs :
            # Stock le nom des strategies dans des sous-listes independantes selon les joueurs a chaque fois que l'un d'eux a fini de les rentrer
            for i in range (len(Fen_strat.list_strat[strat_joueur_nb-1])):
                Fen_strat.nom_strat[strat_joueur_nb-1].append(Fen_strat.list_strat[strat_joueur_nb-1][i].get())
            print ("nom_strat", Fen_strat.nom_strat)

        if strat_joueur_nb < Nb_joueur.nb_joueurs :
            ## Augmente le numero du joueur dont on recupere les noms des strategies
            strat_joueur_nb +=1
        
            Nb_strat.nb_strat = 2
            Fen_strat.height = 290
            Fen_strat.fenetre_strat.destroy()
            Fen_strat.fen_strategie()

        ## Toutes les strategies ont ete rentrees, on change de page
        if strat_joueur_nb == Nb_joueur.nb_joueurs :
            Changer_page.changer_strat_tableau()

    ## Tous les joueurs souhaitent avoir les memes noms de strategies
    else :
        for j in range (len(Fen_strat.list_strat)):
            # Recupere que les noms des strategies du premier joueur
            for i in range (len(Fen_strat.list_strat[0])):
                Fen_strat.nom_strat[j].append(Fen_strat.list_strat[0][i].get())
        print ("nom_strat", Fen_strat.nom_strat)
        Changer_page.changer_strat_tableau()


    

#### mettre tablo de nom
#### mettre tablo complet de max ??


# nom des strat --> Fen_strat.nom_strat
# nom des joueurs --> Recup_valeur.nom_joueur
# nb de strat par joueur --> Changer_page.nb_strategie
