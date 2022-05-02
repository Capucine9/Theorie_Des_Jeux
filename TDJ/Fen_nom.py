from tkinter import *
from tkinter.ttk import *

# Importation d'autres fichiers Python
import Main
import Bouton
import Changer_page

## Initialisation des variables
# Taille de la fenetre
SIZE = "340x300"
height = 300

# Liste contenant les noms des joueurs
list_joueur = []

############################################################################
## Creation de la fenetre d'inscription des noms
def fen_nom():
    global fenetre_nom_joueur
    global list_joueur
    
    fenetre_nom_joueur = Tk()
    fenetre_nom_joueur.title("Nom des joueurs")
    fenetre_nom_joueur.geometry(SIZE)

    ## Titre
    text_nom_titre = Label ( fenetre_nom_joueur, text = "Choix des noms des joueurs", font='Helvetica 13 bold underline')
    text_nom_titre.pack(pady = 10)

    ## Permet aux joueurs de choisir un nom
    text_nom_1 = Label ( fenetre_nom_joueur, text = "Nom du joueur 1 : ")
    text_nom_1.pack(pady = 5)
    nom_entry_1 = Entry(fenetre_nom_joueur)
    nom_entry_1.insert(0, "Joueur 1")
    list_joueur.append(nom_entry_1)
    list_joueur[0].pack(pady = 5)

    text_nom_2 = Label ( fenetre_nom_joueur, text = "Nom du joueur 2 : ")
    text_nom_2.pack()
    nom_entry_2 = Entry(fenetre_nom_joueur)
    nom_entry_2.insert(0, "Joueur 2")
    list_joueur.append(nom_entry_2)
    list_joueur[1].pack(pady = 5)
    

    ## Boutons
    Bouton.bouton (fenetre_nom_joueur, Changer_page.changer_nom_strat)
    
    ## Lance la fenetre
    fenetre_nom_joueur.mainloop()
