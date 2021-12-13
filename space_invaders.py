"""
Weber Thibaut
Gagnepain Quentin
13/12/2001
Realisation space_invaders
A faire : 
"""

#Importation des bibliothèques 
from tkinter import Tk, Button, Canvas, Label


#Programme Principale 

#Creation de la fenetre principale
Fenetre = Tk()
Fenetre.title("Space_invaders")
Fenetre.geometry('1200x900+250+100')

#Creation Canvas (zone de jeu)
l=500
h=500
Zone_jeu=Canvas(Fenetre,width=l,height=h,bg='white')
Zone_jeu.grid(row=1,column=1, padx=15, pady=20)


#Balle qui se deplace
x=0
y=50
r = 10
dx = 10 #vitesse
def deplacement():
    """ Déplacement de la balle """
    global x,y,dx,r,l,h
    
    # rebond à droite
    if x+r+dx > l:
        x = 2*(l-r)-x
        dx = -dx
    
    # rebond à gauche
    if x-r+dx < 0:
        x = 2*r-x
        dx = -dx
    
    x = x+dx
    
    # affichage
    
    Zone_jeu.coords(Balle,x-r,y-r,x+r,y+r)

    # mise à jour toutes les 50 ms
    Fenetre.after(50,deplacement)


def Clavier(event):
    """ Gestion de l'événement Appui sur une touche du clavier """
    global PosX,PosY
    touche = event.keysym
    print(touche)
    # déplacement vers le haut
    if touche == 'Up':
        PosY -= 20
    # déplacement vers le bas
    if touche == 'Down':
        PosY += 20
    # déplacement vers la droite
    if touche == 'Right':
        PosX += 20
    # déplacement vers la gauche
    if touche == 'Left':
        PosX -= 20
    # on dessine le pion à sa nouvelle position
    Canevas.coords(Pion,PosX -10, PosY -10, PosX +10, PosY +10)


# position initiale du pion
PosX = 230
PosY = 150

# Création d'un widget Canvas (zone graphique)
Largeur = 480
Hauteur = 320
Canevas = Canvas(Fenetre, width = Largeur, height =Hauteur, bg ='white')
Pion = Canevas.create_oval(PosX-10,PosY-10,PosX+10,PosY+10,width=2,outline='black',fill='red')
Clavier(Pion)

#Creation Label score 
score=10
Label_score=Label(Fenetre,textvariable=score,bg='white')
Label_score.grid(row=1,column=2)

#Creation du bouton lancer la partie
Balle = Zone_jeu.create_oval(x-r,y-r,x+r,y+r,width=1,fill='green')
BoutonGo = Button(Fenetre, text ='Démarrer', command = deplacement)
BoutonGo.grid(row=3,column=1)

#Creation du bouton quitter 
buttonQuitt = Button(Fenetre, text="Quitter", command=Fenetre.destroy)
buttonQuitt.grid(row=2,column=1)

Fenetre.mainloop()