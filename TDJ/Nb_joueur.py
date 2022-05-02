from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

# Importation d'autres fichiers Python
import Fen_nom
import Bouton

## Initialisation des variables
# Nombre de joueurs
nb_joueurs = 2
nb_joueurs_max = 5
nb_joueurs_min = 2


############################################################################
## Permet le rajout de nouveaux joueurs + agrandissement de la fenetre    
def rajout_joueur():
    global nb_joueurs
    global list_joueur
    global nb_joueurs_max

    if nb_joueurs < nb_joueurs_max :
        # Agrandissement de la fenetre
        Fen_nom.height +=50
        TAILLE = "340x" + str(Fen_nom.height)
        Fen_nom.fenetre_nom_joueur.geometry(TAILLE)

        # Rajout d'un joueur
        nb_joueurs += 1
        globals()["text_nom_" + str(nb_joueurs)] = Label ( Fen_nom.fenetre_nom_joueur, text = "Nom du joueur " + str(nb_joueurs) + " : ")
        globals()["text_nom_" + str(nb_joueurs)].pack()
        globals()["nom_entry" + str(nb_joueurs)] = Entry (Fen_nom.fenetre_nom_joueur)
        globals()["nom_entry" + str(nb_joueurs)].insert(0, "Joueur " + str(nb_joueurs))
        Fen_nom.list_joueur.append(globals()["nom_entry" + str(nb_joueurs)])
        Fen_nom.list_joueur[nb_joueurs - 1].pack(pady = 5)


    else :
        messagebox.showinfo("ATTENTION", "Le nombre de joueur maximum a été atteint.")

############################################################################
## Permet la suppression de joueurs + retrecissement de la fenetre
def supp_joueur():
    global nb_joueurs
    global list_joueur
    global nb_joueurs_min

    if nb_joueurs > nb_joueurs_min :
        # Retrecissement de la fenetre
        Fen_nom.height -=50
        TAILLE = "340x" + str(Fen_nom.height)
        Fen_nom.fenetre_nom_joueur.geometry(TAILLE)

        # Suppression d'un joueur
        nb_joueurs -= 1
        globals()["text_nom_" + str(nb_joueurs+1)].destroy()
        Fen_nom.list_joueur[nb_joueurs].destroy()
        del Fen_nom.list_joueur[-1]

    else :
        messagebox.showinfo("ATTENTION", "Le nombre de joueur minimum a été atteint.")
