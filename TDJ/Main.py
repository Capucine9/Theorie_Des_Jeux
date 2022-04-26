from tkinter import *
from tkinter.ttk import *

# Importation d'autres fichiers Python
#import Nb_joueur
import Fen_nom
#import Bouton
#import Changer_page
import Fen_strat
#import Fen_tableau


# Valeurs des radio-boutons
global valeur_bouton_nom
global valeur_bouton_strat

# Noms des fenetres
global fenetre_nom_joueur, fenetre_strat #'''rajouter nom fenetre maxime'''

    
############################################################################
## Execute la premiere page d'inscription des noms
if __name__ == '__main__':
    Fen_nom.fen_nom()


#### fonction qui rentre les valeurs automatiquement : newList()
