from tkinter import *
from tkinter.ttk import *

# Importation d'autres fichiers Python
import Main
import Fen_nom
import Fen_strat
import Nb_strat
import Nb_joueur
import Recup_valeur


############################################################################
## Creation des boutons de bas de pages
def bouton (fenetre, commande):
    global valeur_bouton_nom
    global valeur_bouton_strat
    global chem_plus
    global chem_moins
    
    ## Zone des boutons de validation et de suppression de la fenetre
    zone_bouton = Frame(fenetre)
    zone_bouton.pack(side=BOTTOM , pady =10)

    ## Zone des radio boutons
    zone_checkbouton = Frame(fenetre)
    zone_checkbouton.pack(side=BOTTOM , pady =10)

    ## Zone des boutons de rajout et de suppression de joueur
    zone_p_m = Frame(fenetre)
    zone_p_m.pack(side=BOTTOM , pady =10)


    if fenetre == Fen_nom.fenetre_nom_joueur :
        ## Bouton "+" permettant de rajouter des joueurs
        bouton_ajout = Button(zone_p_m, text="+", width = 4, command = Nb_joueur.rajout_joueur)
        bouton_ajout.pack(side=LEFT)

        
        ## Bouton "-" permettant de supprimer des joueurs
        bouton_supp = Button(zone_p_m, text="-", width = 4, command = Nb_joueur.supp_joueur)
        bouton_supp.pack(side=RIGHT)

    elif fenetre == Fen_strat.fenetre_strat :
        ## Bouton "+" permettant de rajouter des strategies
        bouton_ajout = Button(zone_p_m, text="+", width = 4, command = Nb_strat.rajout_strat)
        bouton_ajout.pack(side=LEFT)
            
        ## Bouton "-" permettant de supprimer des strategies
        bouton_supp = Button(zone_p_m, text="-", width = 4, command = Nb_strat.supp_strat)
        bouton_supp.pack(side=RIGHT)
        
        ## Bouton de saisie si les utilisateurs souhaitent avoir les mêmes strategies
        if Recup_valeur.strat_joueur_nb ==1 :
            # valeur_bouton_nom égal à True si la case est cochée, False sinon
            valeur_bouton_strat = BooleanVar ()
            case_strat = Checkbutton (zone_checkbouton, variable = valeur_bouton_strat)
            case_strat.config (text = "Les autres joueurs souhaitent avoir les mêmes stratégies")
            case_strat.pack(side=BOTTOM)
        

    ## Bouton de validation des noms de joueurs
    bouton_valider_nom = Button(zone_bouton, text="Suivant", command=commande)
    bouton_valider_nom.pack(side=RIGHT)

    ## Bouton de suppression de la fenetre
    bouton_quitter = Button(zone_bouton, text="Quitter", command=fenetre.destroy)
    bouton_quitter.pack(side=LEFT)
