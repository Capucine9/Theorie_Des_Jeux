from tkinter import *

fenetre=Tk()
fenetre.title("Nom des joueurs")
#LARGEUR = 400
HAUTEUR = 0

#couleur='silver'
can=Canvas(fenetre, height=HAUTEUR) #, bg=couleur, height=HAUTEUR, width=LARGEUR)
can.pack()#side=RIGHT)
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.destroy)



## Permet aux joueurs de choisir un nom
text_1 = Label ( fenetre, text = "Nom du joueur 1 : ")
text_1.pack()
saisie_1 = Entry ()
saisie_1.pack()
joueur_1 = saisie_1.get ()

espace_blanc = Label ( fenetre, text = " ")
espace_blanc.pack()

text_2 = Label ( fenetre, text = "Nom du joueur 2 : ")
text_2.pack()
saisie_2 = Entry ()
saisie_2.pack()
joueur_2 = saisie_2.get ()
espace_blanc1 = Label ( fenetre, text = " ")
espace_blanc1.pack()


# Bouton de saisie si les utilisateurs ne veulent pas rentrer de nom
valeur_bouton_nom = IntVar ()
case = Checkbutton (variable = valeur_bouton_nom)
case.config (text = "Nous ne souhaitons pas choisir de nom de joueur ")
valeur_bouton_nom.get () # égal à 1 si la case est cochée, 0 sinon
case.pack()

# Bouton de validation des noms de joueurs
bouton = Button (fenetre, text = "Suivant")
bouton.pack(side=RIGHT)

#fenetre.eval('tk::PlaceWindow . center')
bouton_quitter.pack(side=LEFT)
fenetre.mainloop()
