from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

# Importation d'autres fichiers Python
import Main
import Fen_strat
import Recup_valeur

## Initialisation des variables
# Nombre de strategies
nb_strat = 2
nb_strat_max = 5
nb_strat_min = 2

############################################################################
## Permet le rajout de nouvelles strategies + agrandissement de la fenetre    
def rajout_strat():
    global nb_strat
    global list_strat
    global nb_strat_max
    global strat_joueur_nb

    if nb_strat < nb_strat_max :
        # Agrandissement de la fenetre
        Fen_strat.height +=50
        TAILLE = "360x" + str(Fen_strat.height)
        Fen_strat.fenetre_strat.geometry(TAILLE)

        # Rajout d'une strategie
        nb_strat += 1
        globals()["text_strat_" + str(nb_strat)] = Label ( Fen_strat.fenetre_strat, text = "Stratégie " + str(nb_strat) + " : ")
        globals()["text_strat_" + str(nb_strat)].pack()
        globals()["strat_entry_" + str(nb_strat)] = Entry(Fen_strat.fenetre_strat)
        globals()["strat_entry_" + str(nb_strat)].insert(0, "Stratégie " + str(nb_strat))
        Fen_strat.list_strat[Recup_valeur.strat_joueur_nb-1].append(globals()["strat_entry_" + str(nb_strat)])
        Fen_strat.list_strat[Recup_valeur.strat_joueur_nb-1][nb_strat - 1].pack(pady = 5)

    else :
        messagebox.showinfo("ATTENTION", "Le nombre de stratégie maximum par joueur a été atteint.")

############################################################################
## Permet la suppression de strategies + retrecissement de la fenetre
def supp_strat():
    global nb_strat
    global list_strat
    global nb_strat_min

    if nb_strat > nb_strat_min :
        # Retrecissement de la fenetre
        Fen_strat.height -=50
        TAILLE = "360x" + str(Fen_strat.height)
        Fen_strat.fenetre_strat.geometry(TAILLE)

        # Suppression d'une strategie
        nb_strat -= 1
        globals()["text_strat_" + str(nb_strat+1)].destroy()
        Fen_strat.list_strat[Recup_valeur.strat_joueur_nb-1][nb_strat].destroy()
        del Fen_strat.list_strat[Recup_valeur.strat_joueur_nb-1][-1]

    else :
        messagebox.showinfo("ATTENTION", "Le nombre de stratégie minimum par joueur a été atteint.")
