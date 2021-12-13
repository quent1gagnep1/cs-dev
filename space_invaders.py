"""
Weber Thibaut
Gagnepain Quentin
13/12/2001
Realisation space_invaders
A faire : 
"""

#Importation des bibliothèques 
from tkinter import Tk, Button


#Programme Principale 

#Creation de la fenetre principale
Fenetre = Tk()
Fenetre.title("Space_invaders")
Fenetre.geometry('1200x900+250+100')

#Creation du bouton quitter 
buttonQuitt = Button(Fenetre, text="Quitter", command=Fenetre.destroy)
buttonQuitt.pack()

Fenetre.mainloop()