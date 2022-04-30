from tkinter import *
import Changer_page
import fonctionalites
import Fen_tableau
import Fen_strat
import Recup_valeur

# Importation d'autres fichiers Python


############################################################################
## Creation de la fenetre des resultats mathématiques
def fen_resultat():
    global fenetre_resultat
    
    fenetre_resultat = Tk()
    fenetre_resultat.title("Resultat")
    fenetre_resultat.geometry("1200x1000")
    
    JOUEURS = Recup_valeur.nom_joueur
    STRATS = Fen_strat.nom_strat
    STRATS_INT = []
    for i in range(len(STRATS)):
        STRATS_INT.append(len(STRATS[i]))
    
    tab_trie = fonctionalites.GenPosStrat(Fen_tableau.VALEURS, STRATS_INT)
        
    ## Titre
    text_result_titre = Label ( fenetre_resultat, text = "Resultat", font='Helvetica 13 bold underline')
    text_result_titre.pack(pady = 10)
    
    
    
    # ======================================================================================================
    # LABELS
    frame_bout = Frame(fenetre_resultat)
    frame_bout.pack(anchor=CENTER, pady=(50,50))
    
    lab = Label ( frame_bout, text = "Somme nulle :", font='Helvetica 11 underline')
    lab.grid(row=0, column=0)
    lab = Label ( frame_bout, text = fonctionalites.somNul(Fen_tableau.VALEURS), font='Helvetica 11')
    lab.grid(row=0, column=1)
    
    # STRAT DOMI
    strats_domi = fonctionalites.domi(tab_trie, STRATS_INT)
    lab = Label ( frame_bout, text = "Strategies strictement dominees : ", font='Helvetica 11 underline')
    lab.grid(row=1, column=0, pady=(50,0))
    level_row = 2
    # strats_domi = strats domi et strictement domi des joueurs
    # strats_domi[i] = strats domi et strictement domi du joueurs i
    # strats_domi[i][0] = strats domi du joueurs i
    # strats_domi[i][1] = strats strictement domi du joueurs i
    # strats_domi[i][0][j] = strats dominant la strat j du joueurs i
    # strats_domi[i][0][j][x] = 1 strat dominant la strat j du joueurs i
    
    # pour chaque joueur
    for i in range(len(strats_domi)):
        lab = Label ( frame_bout, text = JOUEURS[i] + " :", font='Helvetica 11')
        lab.grid(row=level_row, column=1, pady=(0,30))
        is_domi = False
        # pour chaque strat du joueur i
        for s in range(len(strats_domi[i][0])):
            # si le joueur la strat s qui se fait dominer
            if len(strats_domi[i][0][s]) >= 1:
                is_domi = True
                dominance = "\"" + STRATS[0][strats_domi[i][0][s][0]]
                for j in range(1, len(strats_domi[i][0][s])):
                    dominance += " / " + STRATS[i][strats_domi[i][0][s][j]]
                lab = Label ( frame_bout, text = "La strategie \"" + STRATS[i][s] +"\" est strictement dominee par la/les strategies " + dominance +"\"", font='Helvetica 11')
                if s == len(strats_domi[i][0])-1:
                    lab.grid(row=level_row, column=2, pady=(0,30))
                else:
                    lab.grid(row=level_row, column=2)
                level_row += 1
        if not is_domi:
            lab = Label ( frame_bout, text = "Rien", font='Helvetica 11')
            lab.grid(row=level_row, column=2, pady=(0,30))
            level_row += 1
            
            
    # STRAT STRICTEMENT DOMI
    lab = Label ( frame_bout, text = "Strategies dominees : ", font='Helvetica 11 underline')
    lab.grid(row=level_row, column=0, pady=(50,0))
    level_row += 1
    
    # pour chaque joueur
    for i in range(len(strats_domi)):
        lab = Label ( frame_bout, text = JOUEURS[i] + " :", font='Helvetica 11')
        lab.grid(row=level_row, column=1, pady=(0,30))
        is_domi = False
        # pour chaque strat du joueur i
        for s in range(len(strats_domi[i][1])):
            # si le joueur la strat s qui se fait dominer
            if len(strats_domi[i][1][s]) >= 1:
                is_domi = True
                dominance = "\"" + STRATS[0][strats_domi[i][1][s][0]]
                for j in range(1, len(strats_domi[i][1][s])):
                    dominance += " / " + STRATS[i][strats_domi[i][1][s][j]]
                lab = Label ( frame_bout, text = "La strategie \"" + STRATS[i][s] +"\" est dominee par la/les strategies " + dominance +"\"", font='Helvetica 11')
                if s == len(strats_domi[i][1])-1:
                    lab.grid(row=level_row, column=2, pady=(0,30))
                else:
                    lab.grid(row=level_row, column=2)
                level_row += 1
        if not is_domi:
            lab = Label ( frame_bout, text = "Rien", font='Helvetica 11')
            lab.grid(row=level_row, column=2, pady=(0,30))
            level_row += 1
       
       
         
    # EQUILIBRES DE NASH
    equi = fonctionalites.nashPur(tab_trie, STRATS_INT)
    lab = Label ( frame_bout, text = "Equilibre de nash : ", font='Helvetica 11 underline')
    lab.grid(row=level_row, column=0, pady=(50,0))
    level_row += 1
    # pour chauqe equilibre
    print("->",equi)
    for i in range(len(equi)):
        txt_list = '(' + str(equi[i][1][0])
        for v in range(1, len(equi[i][1])):
            txt_list += "," + str(equi[i][1][v])
        txt_list += ')'
        lab = Label ( frame_bout, text = "La strategie \"" + txt_list +"\" est un equilibre de nash", font='Helvetica 11')
        if i == len(equi)-1:
            lab.grid(row=level_row, column=1, pady=(0,30))
        else:
            lab.grid(row=level_row, column=1)
            level_row += 1
    
    
    
    
    # Bouton quitter
    def get_back():
        Changer_page.quitter_resultat()
    bout_quit = Button(fenetre_resultat, text='Quitter', command=get_back)
    bout_quit.pack(side=BOTTOM, pady=20)
    
        
    
    fenetre_resultat.mainloop()
