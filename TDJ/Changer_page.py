from tkinter import *
from tkinter.ttk import *

# Importation d'autres fichiers Python
import Main
import Fen_nom
import Fen_result
#import Bouton
#import Nb_joueurs
import Fen_strat
import Recup_valeur
import Fen_tableau

# nombre de strategie par joueur
nb_strategie = []

############################################################################
## Permet de changer de page (inscription des noms --> saisie des strategies)
def changer_nom_strat():
    Recup_valeur.joueur()
    Fen_nom.fenetre_nom_joueur.destroy()
    Fen_strat.fen_strategie()

def changer_strat_tableau():
    global nb_strategie

    for i in range (len(Fen_strat.list_strat)):
        nb_strategie.append(len(Fen_strat.nom_strat[i]))
    print ("nb_strategie",nb_strategie)
    
    Fen_strat.fenetre_strat.destroy()
    Fen_tableau.fen_tableau()
    
def changer_tableau_resultat():
    Fen_tableau.app.destroy()
    Fen_result.fen_resultat()
    

