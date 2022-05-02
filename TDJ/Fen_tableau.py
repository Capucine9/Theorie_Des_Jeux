from tkinter import *
from tkinter.ttk import Separator, Style
from string import ascii_lowercase
import re  
from tkinter import messagebox
from fonctionalites import newListe
import Changer_page


# Importation d'autres fichiers Python
import Nb_joueur
import Recup_valeur
import Fen_strat


# ======================================================================================================
# Info general pour le programme

# Default size  
LARGEUR = 1500
HAUTEUR = 500
# Config the game

# tableau des valeurs du tableau (remplis plus tard)
VALEURS = []
txt_popup = ""
# Nom des joueurs et des strategies affiche dans le tableau (noms provisoires)
tmp_j = []
tmp_s = []



def fen_tableau():
    global LARGEUR
    global HAUTEUR
    global JOUEURS
    global tmp_j
    global tmp_s
    global txt_popup
    global app
    global inf
    global sup
    global valeur_null
    global VALEURS
    VALEURS = []

    # Recuperation de donnees precedente
    NB_joueurs = Nb_joueur.nb_joueurs
    JOUEURS = Recup_valeur.nom_joueur
    STRATS = Fen_strat.nom_strat
    
    # ======================================================================================================
    # Config de la fenetre
    
    # Create the windows
    app = Tk()
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    # Responsive size according the configuration of the game
    NB_COLONNE = len(STRATS[len(STRATS)-1])     # NB_COLONNE = nombre de strat de la deniere case de STRATS
    for i in range(0, len(STRATS)-2):           # Les strats du joueur 1 ne sont pas prises en compte
        NB_COLONNE *= len(STRATS[len(STRATS)-i-2])
    LARGEUR = NB_COLONNE * 70 + 2000 # must be size of a cell of the tab, but 70 work well
    # avoid to go out of the screen or too small
    if LARGEUR > 1200:
        LARGEUR = 1200
    if LARGEUR < 600:
        LARGEUR = 600
    # Coordinates of the upper left corner of the window to make the window appear in the center
    x_cordinate = int((screen_width/2) - (LARGEUR/2))
    y_cordinate = int((screen_height/2) - (HAUTEUR/2))
    # Set the size and the position of the windows
    app.geometry("{}x{}+{}+{}".format(LARGEUR, HAUTEUR, x_cordinate, y_cordinate))


    titre = Label ( app, text = "Remplissage des strategies", font='Helvetica 13 bold underline')
    titre.pack(pady = 50)



    # ======================================================================================================
    # BOUTTONS
    
    frame_bout = Frame(app)
    frame_bout.pack(side=TOP, pady=(0,50))
    def print_legend():
        messagebox.showinfo("ATTENTION", txt_popup)
                    
    button = Button(frame_bout, text="Infos sur la legende du tableau", command=print_legend).grid(row = 0, column = 2, columnspan=2, padx=(0, 30))
    
    def put_val_aleatoire():
        min = inf.get()
        max = sup.get()
        val = 1 if valeur_nul.get() else 0
        if min > max:
            messagebox.showinfo("ATTENTION", "La valeur minimale de l'intervale de generation de valeurs aleatoires ne peut etre superieure a la valeur maximale de l'intervale.")
            pass
        
        
        s = []
        for i in range(len(STRATS)):
            s.append(len(STRATS[i]))
        val = newListe(val, NB_joueurs, s, [min,max])
        # pour chaque case remplissable du tableau
        i = 0
        for e in tableur.children:
            v = tableur.children[e]
            match = ['a', 'b', 'c', 'd', 'e']
            # si la case n'est pas une case de label pour le tableau
            # sinon elle contient forcement une lettre pour le nom des strategies
            if not any(x in v.get() for x in match):
                v.delete(0,"end")
                txt = str(val[i][0])
                for j in range(NB_joueurs-1):
                    txt += "," + str(val[i][j+1])
                v.insert(0, txt)
                i += 1
        
    button = Button(frame_bout, text="Valeurs aleatoires", command=put_val_aleatoire).grid(row = 1, column = 5, padx=(0, 10))
    
    
    
    ## Bouton d'echelle
    # Inferieur
    lab = Label ( frame_bout, text = "Borne inferieure", font='Helvetica 11')
    lab.grid(row = 1, column = 0, padx=(10, 5))
    inf = IntVar()
    echelle_inf = Scale(frame_bout, orient='horizontal', from_=-20, to=20, length=200, variable = inf).grid(row = 1, column = 1, padx=(0, 10))
    
    
    # Superieur
    lab = Label ( frame_bout, text = "Borne superieure", font='Helvetica 11')
    lab.grid(row = 1, column = 2, padx=(10, 5))
    sup = IntVar()
    echelle_sup = Scale(frame_bout, orient='horizontal', from_=-20, to=20, length=200, variable = sup).grid(row = 1, column = 3, padx=(0, 10))
    
    
    ## Bouton de saisie si les utilisateurs souhaitent choisir un jeu a somme nul
    # valeur_nul egal a True si la case est cochee, False sinon
    valeur_nul = BooleanVar ()
    case_nul = Checkbutton (frame_bout, variable = valeur_nul)
    case_nul.config (text = "Jeu a somme nulle")
    case_nul.grid(row = 1, column = 4)
    



    # ======================================================================================================
    # LABEL pour la legende du tableau

    # Nom temporaire des joueurs pour le tableau
    for i in range(0, NB_joueurs):
        text = str(i+1)
        txt_popup += "Soit \""+ text +"\" le joueur : \""+ JOUEURS[i]+"\"\n"
        tmp_j.append(text)
            
    # Nom temporaire des strategies pour le tableau
    for i in range(0, len(STRATS)):
        txt_popup += "\n"
        tab = []
        for j in range(0 , len(STRATS[i])):
            txt_strat = str(i+1) + ascii_lowercase[j:j+1]
            txt_popup += "Soit \""+ txt_strat +"\" la strategie \"" + STRATS[i][j] + "\" du joueur \"" + JOUEURS[i] + "\"\n"
            tab.append(txt_strat)
        tmp_s.append(tab)




    """
    Format du tableau : les lignes representent les strats du joueur 1. Les colonnes representent
    toutes les combinaisons de strategies entre les joueurs restant. La premiere colonne, represente
    le cas ou les joueurs autre que le joueur 1 jouent tous leur premiere strategie (depuis leurs liste
    de strategies). La colone suivante, seul le dernier joueur joue sa strategie suivante (strategie
    suivante dans sa liste de strategies). Si le dernier joueur a joue toutes ses strategies,
    alors le joueur precedent joue sa prochaine strategie et le dernier joueur rejoue toutes ses strategies.
    Ainsi, dans l'exemple ou trois joueurs on tous les trois, deux stategies, l'ensemble des lignes dans cet
    exemple est alors {"strat1_j1", "strat2_j1"}. L'ensemble des colonnes dans cet exemple serai alors 
    {("strat1_j2", "strat1_j3"), ("strat1_j2", "strat2_j3"), ("strat2_j2", "strat1_j3"), ("strat2_j2", "strat2_j3")}
    """
    class Tableur(Frame):
        def __init__(self, master, rows, columns, width):
            super().__init__(master)

            # retiens la strategie courante du dernier joueur
            self.count = 0
            # retiens la strategie courante des joueurs (le 1e n'ai pas pris en compte)
            self.indices = [0]*(NB_joueurs-1)
            

            # Label des colonnes
            for i in range(columns):
                txt = ""
                for j in range(1, NB_joueurs):
                    txt += tmp_s[j][self.indices[j-1]]
                    if j != (NB_joueurs-1):
                        txt += "_"
                self.make_entry(0, i+1, width, txt, False) 
                self.incrementBuffer()

            # Pour chaque ligne
            for row in range(rows):
                # Label des lignes
                txt = tmp_s[0][row]
                self.make_entry(row+1, 0, 5, txt, False)
                    
                # Cellules vides
                for column in range(columns):
                    self.make_entry(row+1, column+1, width, '', True)

        def make_entry(self, row, column, width, text, state):
            e = Entry(self, width=width)
            if text: e.insert(0, text)
            e['state'] = NORMAL if state else DISABLED
            e.coords = (row-1, column-1)
            e.grid(row=row, column=column)
        
        def incrementBuffer(self):
            isNext = 0
            # increnmente le numero de strat du dernier joueur dans la variable 
            # de comptage et dans le tableau
            self.count += 1
            self.indices[len(self.indices)-1] += 1
            if self.count == len(STRATS[len(STRATS)-1]):
                self.count = 0
            
            # si le numero de strat pour un joueur a depasser son nombre de strat, alors
            # le numero reviens a 0 et incrementation du numero de la strat du joueur precedent
            for i in range(1, NB_joueurs-1):
                j = NB_joueurs-i-1 # -1 : car j -> 1:10, case -> 0:9 ET -1 car j2 = case 1 (j1 abs)
                if self.indices[j] == len(STRATS[j+1]):
                    self.indices[j] = 0 
                    isNext = 1
                    
                if isNext:
                    if j > 0:
                        self.indices[j-1] += 1
                    isNext = 0
                
            


    # ======================================================================================================
    # Config des composants de la fenetre

    grid_layout = Frame(app)
    canvas = Canvas(grid_layout)
    scrollbar = Scrollbar(grid_layout, orient="horizontal", command=canvas.xview)
    tableur = Tableur(canvas, rows=len(STRATS[0]), columns=NB_COLONNE, width=12)
    tableur.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0, 0), window=tableur, anchor="nw")
    canvas.configure(xscrollcommand=scrollbar.set)
    grid_layout.pack()
    canvas.pack(side="top", fill="both", expand=True)
    scrollbar.pack(side="bottom", fill="x")


    # ======================================================================================================
    # Ajout d'un bouton de validation

    def get_cells():
        global VALEURS
        # VALEURS = []
        # pour chaque case remplisable du tableau
        
        for e in tableur.children:
            v = tableur.children[e]
            match = ['a', 'b', 'c', 'd', 'e']
            # si la case n'est pas une case de label pour le tableau
            # sinon elle contient forcement une lettre pour le nom des strategies
            if not any(x in v.get() for x in match):
                pattern = re.compile("^-?\d+(\,-?\d+)+$")
                # si l'entree utilisateur n'est pas dans le format
                # format : "nombre,nombre,nombre"
                if not pattern.match(v.get()):
                    messagebox.showinfo("ATTENTION", "Le format de l'entree \""+ v.get() +"\" n'est pas le bon. Chaque entree doit etre un couple (sans mettre les parentheses) de n valeurs (n etant le nombre de joueurs).")
                    VALEURS= []
                    break
                else:
                    # TODO : supprimer les espaces apres le split
                    tmp = v.get().split(',')
                    for i in range(len(tmp)):
                        tmp[i] = int(tmp[i])
                    VALEURS.append(tmp)
        """
        VALEURS = [[0,0,0],[-1,-1,2],[1,1,-2],[-1,-1,2],[-1,2,-1],[-2,1,1],[0,0,0],[-2,2,0],[1,-2,1],[0,0,0],[2,-1,-1],[0,-2,2],
               [2,-1,1],[1,-2,1],[0,0,0],[2,-2,0],[1,1,-2],[0,0,0],[-1,-1,2],[1,1,-2],[0,0,0],[-1,2,-1],[-2,1,1],[0,0,0],
               [-2,1,1],[0,0,0],[-1,2,-1],[-1,-1,2],[0,0,0],[2,-1,-1],[1,-2,1],[0,0,0],[-1,-1,2],[1,1,-2],[0,0,0],[-1,-1,2]]"""
        """VALEURS = [[0,0],[-1,1],[1,-1],[-1,1],
                   [1,-1],[0,0],[-1,1],[1,-1],
                   [-1,1],[1,-1],[0,0],[-1,1]]"""
        if len(VALEURS) != 0:
            Changer_page.changer_tableau_resultat()

    bt = Button(app, text='Valider (format des entrees : \"x,x,x\")', command=get_cells)
    bt.pack(pady=20)


    canvas.config(width=(NB_COLONNE+1)*70, height=120)
    
    
    app.mainloop()
