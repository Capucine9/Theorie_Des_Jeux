from tkinter import *
import Changer_page
import fonctionalites
import Fen_tableau
import Fen_strat
import Recup_valeur
from TDJ.Fen_tableau import fen_tableau

# Importation d'autres fichiers Python


############################################################################
## Creation de la fenetre des resultats mathématiques
def fen_resultat():
    global fenetre_resultat
    fenetre_resultat = Tk()
    fenetre_resultat.title("Resultat")
    fenetre_resultat.geometry("1500x800")
    
    JOUEURS = Recup_valeur.nom_joueur
    STRATS = Fen_strat.nom_strat
    STRATS_INT = []
    for i in range(len(STRATS)):
        STRATS_INT.append(len(STRATS[i]))
    
    tab_trie = fonctionalites.GenPosStrat(Fen_tableau.VALEURS, STRATS_INT)
        
    ## Titre
    text_result_titre = Label ( fenetre_resultat, text = "Resultat", font='Helvetica 13 bold underline')
    text_result_titre.pack(pady = 5)
    
    
    
    # ======================================================================================================
    # LABELS
    frame_bout = Frame(fenetre_resultat)
    frame_bout.pack(anchor=CENTER, pady=(30,30))
    
    lab = Label ( frame_bout, text = "Somme nulle :", font='Helvetica 11 underline')
    lab.grid(row=0, column=0)
    lab = Label ( frame_bout, text = fonctionalites.somNul(Fen_tableau.VALEURS), font='Helvetica 11')
    lab.grid(row=0, column=1)
    
    # STRAT DOMINEE
    strats_domi = fonctionalites.domi(tab_trie, STRATS_INT)
    lab = Label ( frame_bout, text = "Strategies strictement dominees : ", font='Helvetica 11 underline')
    lab.grid(row=1, column=0, pady=(30,0))
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
        lab.grid(row=level_row, column=1, pady=(0,20))
        is_domi = False
        # pour chaque strat du joueur i
        for s in range(len(strats_domi[i][0])):
            # si le joueur la strat s qui se fait dominer
            if len(strats_domi[i][0][s]) >= 1:
                is_domi = True
                dominance = "\"" + STRATS[i][strats_domi[i][0][s][0]]
                for j in range(1, len(strats_domi[i][0][s])):
                    dominance += " / " + STRATS[i][strats_domi[i][0][s][j]]
                lab = Label ( frame_bout, text = "La strategie \"" + STRATS[i][s] +"\" est strictement dominee par la/les strategies " + dominance +"\"", font='Helvetica 11')
                if s == len(strats_domi[i][0])-1:
                    lab.grid(row=level_row, column=2, pady=(0,20))
                else:
                    lab.grid(row=level_row, column=2)
                level_row += 1
        if not is_domi:
            lab = Label ( frame_bout, text = "Rien", font='Helvetica 11')
            lab.grid(row=level_row, column=2, pady=(0,20))
            level_row += 1
            
            
    # STRAT STRICTEMENT DOMINEE
    lab = Label ( frame_bout, text = "Strategies dominees : ", font='Helvetica 11 underline')
    lab.grid(row=level_row, column=0, pady=(30,0))
    level_row += 1
    
    # pour chaque joueur
    for i in range(len(strats_domi)):
        lab = Label ( frame_bout, text = JOUEURS[i] + " :", font='Helvetica 11')
        lab.grid(row=level_row, column=1, pady=(0,20))
        is_domi = False
        # pour chaque strat du joueur i
        for s in range(len(strats_domi[i][1])):
            # si le joueur la strat s qui se fait dominer
            if len(strats_domi[i][1][s]) >= 1:
                is_domi = True
                dominance = "\"" + STRATS[i][strats_domi[i][1][s][0]]
                for j in range(1, len(strats_domi[i][1][s])):
                    dominance += " / " + STRATS[i][strats_domi[i][1][s][j]]
                lab = Label ( frame_bout, text = "La strategie \"" + STRATS[i][s] +"\" est dominee par la/les strategies " + dominance +"\"", font='Helvetica 11')
                if s == len(strats_domi[i][1])-1:
                    lab.grid(row=level_row, column=2, pady=(0,20))
                else:
                    lab.grid(row=level_row, column=2)
                level_row += 1
        if not is_domi:
            lab = Label ( frame_bout, text = "Rien", font='Helvetica 11')
            lab.grid(row=level_row, column=2, pady=(0,20))
            level_row += 1
            
            
    
    
    # STRAT DOMINANTE
    lab = Label ( frame_bout, text = "Strategies strictement dominante : ", font='Helvetica 11 underline')
    lab.grid(row=level_row, column=0, pady=(30,0))
    level_row += 1
    
    # pour chaque joueur
    for i in range(len(strats_domi)):
        lab = Label ( frame_bout, text = JOUEURS[i] + " :", font='Helvetica 11')
        lab.grid(row=level_row, column=1, pady=(0,20))
        is_domi = False
        # pour chaque strat du joueur i
        for s in range(len(strats_domi[i][2])):
            # si le joueur la strat s qui se fait dominer
            if len(strats_domi[i][2][s]) >= 1:
                is_domi = True
                dominance = "\"" + STRATS[i][strats_domi[i][2][s][0]]
                for j in range(1, len(strats_domi[i][2][s])):
                    dominance += " / " + STRATS[i][strats_domi[i][2][s][j]]
                lab = Label ( frame_bout, text = "La strategie \"" + STRATS[i][s] +"\" est strictement dominante", font='Helvetica 11')
                if s == len(strats_domi[i][2])-1:
                    lab.grid(row=level_row, column=2, pady=(0,20))
                else:
                    lab.grid(row=level_row, column=2)
                level_row += 1
        if not is_domi:
            lab = Label ( frame_bout, text = "Rien", font='Helvetica 11')
            lab.grid(row=level_row, column=2, pady=(0,20))
            level_row += 1
            
            
    
       
       
         
    # EQUILIBRES DE NASH
    equi = fonctionalites.nashPur(tab_trie, STRATS_INT)
    print("equi",equi)
    lab = Label ( frame_bout, text = "Equilibre de nash : ", font='Helvetica 11 underline')
    lab.grid(row=level_row, column=0, pady=(30,0))
    level_row += 1
    # pour chauqe equilibre
    for i in range(len(equi)):
        txt_list = '(' + str(equi[i][1][0])
        for v in range(1, len(equi[i][1])):
            txt_list += "," + str(equi[i][1][v])
        txt_list += ')'
        txt_coup = '[' + str(equi[i][0][0])
        for v in range(1, len(equi[i][0])):
            txt_coup += "," + str(equi[i][0][v])
        txt_coup += ']'
        lab = Label ( frame_bout, text = "La strategie \"" + txt_list +"\" est un equilibre de nash (dans le cas ou les joueurs joue : " + txt_coup + ")", font='Helvetica 11')
        if i == len(equi)-1:
            lab.grid(row=level_row, column=1, pady=(0,20))
        else:
            lab.grid(row=level_row, column=1)
            level_row += 1
    if len(equi) == 0:
        lab = Label ( frame_bout, text = "Aucun equilibre", font='Helvetica 11')
        lab.grid(row=level_row, column=1, pady=(0,20))
    
    
    # EQUILIBRES DE NASH MIXTE
    if len(STRATS_INT) == 2 and STRATS_INT[0] == 2 and STRATS_INT[1] == 2:
        lab = Label ( frame_bout, text = "Equilibre de nash mixte: ", font='Helvetica 11 underline')
        lab.grid(row=level_row, column=0, pady=(30,0))
        level_row += 1
        
        lab = Label ( frame_bout, text = "Probabilite que \"" + JOUEURS[0] +"\" joue la strategie \"" + STRATS[0][0] + "\" :", font='Helvetica 11')
        lab.grid(row=level_row, column=1, pady=(10,0))
        
        Entry1 = Entry(frame_bout, width=20)
        Entry1.grid(row=level_row, column=2, pady=(10,0))
        level_row += 1
        
        lab = Label ( frame_bout, text = "Probabilite que \"" + JOUEURS[0] +"\" joue la strategie \"" + STRATS[0][1] + "\"", font='Helvetica 11')
        lab.grid(row=level_row, column=1, pady=(10,0))        
        
        Entry2 = Entry(frame_bout, width=20)
        Entry2.grid(row=level_row, column=2, pady=(10,0))
        level_row += 1
        
        LabRes = Label ( frame_bout, text = "En attente...", font='Helvetica 11')
        LabRes.grid(row=level_row, column=2, pady=(10,0))        
        
        def search_equi_mixte():
            proba1 = float(Entry1.get())
            proba2 = float(Entry2.get())
            moy = fonctionalites.nashMixte(tab_trie, [proba1, proba2])
            LabRes.config(text = "Utilite moyenne du joueur \"" + JOUEURS[0] +"\" : " + str(moy) +" (100 cas)")
        but = Button(frame_bout, text='Chercher un equilibre mixte', command=search_equi_mixte)
        but.grid(row=level_row, column=1, pady=(10,0))
        level_row += 1
    
    
    # Bouton quitter
    def get_back():
        Changer_page.quitter_resultat()
    bout_quit = Button(fenetre_resultat, text='Fermer les resultats', command=get_back)
    bout_quit.pack(side=BOTTOM, pady=10)
    
        
    
    fenetre_resultat.mainloop()
