# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtMultimedia import QSound
from PyQt5 import QtTest
from Interface import Interface
from Mecaniques import ZoneRencontre
from Deplacement import Transition
import numpy as np

class Carte(Interface):
    def __init__(self,MainWindow,MapPath):
        super().__init__(MainWindow)
        
        #Initialisation de la carte d'un point de vue graphique
        self.carte = QtWidgets.QLabel(self.MainWindow)
        self.carte.setGeometry(QtCore.QRect(-670, -226, 4800, 4800))
        self.carte.setText("")
        self.carte.setScaledContents(True)
        self.carte.setObjectName("carte")
        self.carte.setPixmap(QtGui.QPixmap(MapPath))
        
        #Initialisation de la carte d'un point de vue matriciel
        self.matrice_dalle = np.genfromtxt("./data/Matrice.csv", delimiter=";")
        
        #Son
        self.BumpSound = QSound("./Son/Bump.wav")
        self.Healing = QSound("./Son/Healing.wav")
        self.PCSound = QSound("./Son/PC.wav")
        
    def Glissement(self,Direction,Sprite):
        self.anim = QtCore.QPropertyAnimation(self.carte, b'geometry')
        self.anim.setDuration(50)
        rect = self.carte.geometry()
        self.anim.setStartValue(rect)
        
        if Direction == "Derriere":
            if self.matrice_dalle[Sprite.y-1, Sprite.x] != 0 and self.matrice_dalle[Sprite.y-1, Sprite.x] not in [51,52,101,102]:
                Sprite.x, Sprite.y = Sprite.x, Sprite.y-1
                rect.translate(0,48)
            else:
                self.BumpSound.play()
        elif Direction == "Devant":
            if self.matrice_dalle[Sprite.y+1, Sprite.x] != 0 and self.matrice_dalle[Sprite.y+1, Sprite.x] not in [51,52,101,102]:
                Sprite.x, Sprite.y = Sprite.x, Sprite.y+1
                rect.translate(0,-48)
            else:
                self.BumpSound.play()
        elif Direction == "Gauche":
            if self.matrice_dalle[Sprite.y, Sprite.x-1] != 0 and self.matrice_dalle[Sprite.y, Sprite.x-1] not in [51,52,101,102]:
                Sprite.x, Sprite.y = Sprite.x-1, Sprite.y
                rect.translate(48,0)
            else:
                self.BumpSound.play()
        elif Direction == "Droite":
            if self.matrice_dalle[Sprite.y, Sprite.x+1] != 0 and self.matrice_dalle[Sprite.y, Sprite.x+1] not in [51,52,101,102]:
                Sprite.x, Sprite.y = Sprite.x+1, Sprite.y
                rect.translate(-48,0)
            else:
                self.BumpSound.play()
                
        self.anim.setEndValue(rect)
        self.anim.start()
        
    def Warp(self, deltaY, deltaX):
        self.Menu = "Dummy"
        #Translate la carte d'un point de départ à un point d'arrivée
        rect = self.carte.geometry()
        rect.translate(-deltaX*48, -deltaY*48)
        self.carte.setGeometry(rect)
        QtTest.QTest.qWait(1000)
        self.Menu = "Carte"
    
    def Interaction(self, Sprite, Equipe):
        #Vérifie si le joueur est à côté d'une case avec laquelle il peut interagir
        y = Sprite.y
        x = Sprite.x
        if (y-1,x) == (89,87) and Sprite.Orientation == "Derriere": #Soin dans le Pokémon Center
            self.Healing.play()
            self.MainWindow.Menu = "Healing"
            QtTest.QTest.qWait(4000)
            self.MainWindow.Menu = "Carte"
            Equipe.Soin_All()
            
        elif (y-1,x) == (87,91) and Sprite.Orientation == "Devant": #On parle au PC
            self.MainWindow.Menu = "PC"
            self.PCSound.play()
            QtTest.QTest.qWait(1000)
            self.hide()
            
            self.MainWindow.Menu_PC.show()
        
        #Pêche
        elif (self.matrice_dalle[Sprite.y, Sprite.x-1] == 52 or self.matrice_dalle[Sprite.y, Sprite.x-1] ==51) and Sprite.Orientation == "Gauche":
            PokeRencontre = ZoneRencontre(self.matrice_dalle[Sprite.y, Sprite.x-1]).Random_Poke()
            Direction = Sprite.Orientation
            self.Sprite.Changement_Sprite(f"./Animation/Marche/{Direction}_repos.png")
            self.MainWindow.Menu = "Combat"
            Tr = Transition(self.MainWindow)
            self.Jukebox.ChangeDeMusique("./Son/Battle.wav")
            Tr.start()
            Tr.show()
            QtTest.QTest.qWait(1900)
            self.carte.hide()
            self.Sprite.hide()
            self.MainWindow.Menu = self.MainWindow.UICombat.Init_Combat(self.Equipe,PokeRencontre)
            QtTest.QTest.qWait(900)
            Tr.hide()
            Tr.stop()
        elif (self.matrice_dalle[Sprite.y+1, Sprite.x] == 52 or self.matrice_dalle[Sprite.y+1, Sprite.x] == 51) and Sprite.Orientation == "Devant":
            PokeRencontre = ZoneRencontre(self.matrice_dalle[Sprite.y+1, Sprite.x]).Random_Poke()
            Direction = Sprite.Orientation
            self.Sprite.Changement_Sprite(f"./Animation/Marche/{Direction}_repos.png")
            self.MainWindow.Menu = "Combat"
            Tr = Transition(self.MainWindow)
            self.Jukebox.ChangeDeMusique("./Son/Battle.wav")
            Tr.start()
            Tr.show()
            QtTest.QTest.qWait(1900)
            self.carte.hide()
            self.Sprite.hide()
            self.MainWindow.Menu = self.MainWindow.UICombat.Init_Combat(self.Equipe,PokeRencontre)
            QtTest.QTest.qWait(900)
            Tr.hide()
            Tr.stop()
        elif (self.matrice_dalle[Sprite.y, Sprite.x+1] == 52 or self.matrice_dalle[Sprite.y, Sprite.x+1] == 51) and Sprite.Orientation == "Droite":
            PokeRencontre = ZoneRencontre(self.matrice_dalle[Sprite.y, Sprite.x+1]).Random_Poke()
            Direction = Sprite.Orientation
            self.Sprite.Changement_Sprite(f"./Animation/Marche/{Direction}_repos.png")
            self.MainWindow.Menu = "Combat"
            Tr = Transition(self.MainWindow)
            self.Jukebox.ChangeDeMusique("./Son/Battle.wav")
            Tr.start()
            Tr.show()
            QtTest.QTest.qWait(1900)
            self.carte.hide()
            self.Sprite.hide()
            self.MainWindow.Menu = self.MainWindow.UICombat.Init_Combat(self.Equipe,PokeRencontre)
            QtTest.QTest.qWait(900)
            Tr.hide()
            Tr.stop()
        elif (self.matrice_dalle[Sprite.y-1, Sprite.x] == 52 or self.matrice_dalle[Sprite.y-1, Sprite.x] == 51) and Sprite.Orientation == "Derriere":
            PokeRencontre = ZoneRencontre(self.matrice_dalle[Sprite.y-1, Sprite.x]).Random_Poke()
            Direction = Sprite.Orientation
            self.Sprite.Changement_Sprite(f"./Animation/Marche/{Direction}_repos.png")
            self.MainWindow.Menu = "Combat"
            Tr = Transition(self.MainWindow)
            self.Jukebox.ChangeDeMusique("./Son/Battle.wav")
            Tr.start()
            Tr.show()
            QtTest.QTest.qWait(1900)
            self.carte.hide()
            self.Sprite.hide()
            self.MainWindow.Menu = self.MainWindow.UICombat.Init_Combat(self.Equipe,PokeRencontre)
            QtTest.QTest.qWait(900)
            Tr.hide()
            Tr.stop()
            
            
    def hide(self):
        self.carte.hide()
        self.Sprite.hide()
        
    def show(self):
        self.carte.show()
        
        
class Sprite:
    def __init__(self,MainWindow,SpritePath, X, Y, larg, haut, nom):
        #Définition de l'encart contenant le sprite
        self.Label = QtWidgets.QLabel(MainWindow)
        self.Label.setGeometry(QtCore.QRect(X, Y , larg, haut))
        self.Label.setScaledContents(True)
        self.Label.setPixmap(QtGui.QPixmap(SpritePath))
        self.Label.setObjectName(nom)
        
        #Définition des coordonnées initiales du sprite (Dans la matrice)
        self.x = 19
        self.y = 10
        
        #Définition de l'animation éventuelle.
        self.IsAnimated = False
        self.movie = None
        
        #Définition de l'orientation du personnage
        self.Orientation = "Devant"
        
    def Changement_Sprite(self,Sprite):
        if self.IsAnimated:
            self.movie.stop()
            self.IsAnimated = False
        self.Label.setPixmap(QtGui.QPixmap(Sprite))
        self.Label.setScaledContents(True)
        
        
    def Animation(self, Gif):
        self.movie = QMovie(Gif)
        self.Label.setMovie(self.movie)
        self.movie.start()
        self.IsAnimated = True
        
    def hide(self):
        self.Label.hide()
            
    def show(self):
        self.Label.show()
