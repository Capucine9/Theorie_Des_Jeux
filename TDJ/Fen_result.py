from tkinter import *
import tkinter.ttk as ttk

# Importation d'autres fichiers Python


############################################################################
## Creation de la fenetre des resultats mathématiques
def fen_resultat():
    global fenetre_resultat
    
    fenetre_resultat = Tk()
    fenetre_resultat.title("Resultat")
    fenetre_resultat.geometry("300x400")#SIZE)

    ## Titre
    text_result_titre = Label ( fenetre_resultat, text = "Resultat", font='Helvetica 13 bold underline')
    text_result_titre.pack(pady = 10)
    
    
        
    
    fenetre_resultat.mainloop()
