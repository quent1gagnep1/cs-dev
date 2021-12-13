"""
Weber Thibaut
Gagnepain Quentin
13/12/2001
Realisation space_invaders
Librairie des fonctions
A faire : 
"""


#Importation des bibliothèques 
from tkinter import Tk, Button, Canvas, Label


#Creation de la class Alien
#class Alien:

 #   def __init__(self):
  #      self.x = 0
   #     self.y = 0
    #    self.v = 0

#    a1=Alien(400,300,10)
#    print(a1.x)
#    def deplace(self,a1.v):
#        self.x = self.x + a1.v

#    a1.deplace(300)


def Cercle():
    """ Dessine un cercle de centre (x,y) et de rayon r """
    x = random.randint(0,Largeur)
    y = random.randint(0,Hauteur)
    r = 10
    Canevas.create_oval(x-r, y-r, x+r, y+r, outline='red', fill='red')
    Fenetre.after(50,Cercle)
