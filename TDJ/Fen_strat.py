from tkinter import *
from tkinter.ttk import *
import copy

# Importation d'autres fichiers Python
import Main
import Nb_joueur
import Bouton
import Changer_page
import Recup_valeur

## Initialisation des variables
# Taille de la fenetre
SIZE = "340x290"
height = 290

# Liste contenant les noms des strategies
list_strat = []

def len_list_strat():
    global nom_strat
    
    ##Creer autant de sous-listes de strategies que de joueur
    for i in range (Nb_joueur.nb_joueurs):
        list_strat.append([])
    nom_strat = copy.deepcopy(list_strat)

############################################################################
## Creation de la fenetre d'inscription des strategies
def fen_strategie():
    global fenetre_strat
    global list_joueur
    global list_strat
    global strat_joueur_nb

    ##Creer les sous-listes de strategies
    if Recup_valeur.strat_joueur_nb == 1 :
        len_list_strat()
    
    fenetre_strat = Tk()
    fenetre_strat.title("Nom des statégies")
    fenetre_strat.geometry(SIZE)

    ## Titre
    text_strat_titre = Label ( fenetre_strat, text = ("Stratégie du joueur " + str(Recup_valeur.strat_joueur_nb) + " :") , font='Helvetica 13 bold underline')
    text_strat_titre.pack(pady = 10)

    ## Permet aux joueurs de choisir un nom de strategie
    text_strat_1 = Label ( fenetre_strat, text = "Stratégie 1 : ")
    text_strat_1.pack(pady = 5)
    strat_entry_1 = Entry(fenetre_strat)
    strat_entry_1.insert(0, "Strategie 1")
    list_strat[Recup_valeur.strat_joueur_nb-1].append(strat_entry_1)
    list_strat[Recup_valeur.strat_joueur_nb-1][0].pack(pady = 5)

    text_strat_2 = Label ( fenetre_strat, text = "Stratégie 2 : ")
    text_strat_2.pack()
    strat_entry_2 = Entry(fenetre_strat)
    strat_entry_2.insert(0, "Strategie 2")
    list_strat[Recup_valeur.strat_joueur_nb-1].append(strat_entry_2)
    list_strat[Recup_valeur.strat_joueur_nb-1][1].pack(pady = 5)

    
    ## Boutons
    Bouton.bouton (fenetre_strat, Recup_valeur.strat)
        

    ## Lance la fenetre
    fenetre_strat.mainloop()
