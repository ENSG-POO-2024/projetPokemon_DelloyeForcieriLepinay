# -*- coding: utf-8 -*-
from datetime import datetime
from PyQt5.QtGui import QMovie
from PyQt5 import QtCore, QtGui, QtWidgets
import random as r
from Mecaniques import ZoneRencontre
from PyQt5 import QtTest

class Deplacement():
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        self.Sprite = MainWindow.SpritePerso
        self.Carte = MainWindow.map
        self.Legend = MainWindow.SpriteLegend
        self.Jukebox = MainWindow.Jukebox
        self.UICombat = MainWindow.UICombat
        
        #
        self.Equipe = MainWindow.Equipe
        
    
    def move(self,Direction):
        
        Menu = "Carte"
        #On regarde si une animation n'est pas déjà en cours s'il n'y en a pas. On remplace le jpg par un gif.
        if not self.Sprite.IsAnimated:
            self.Sprite.Animation(f"./Animation/Marche/{Direction}.gif")
        self.Carte.Glissement(Direction,self.Sprite,self.Legend)
        
        #Rencontre_Aleatoire
        Case_Actuelle = self.Carte.matrice_dalle[self.Sprite.y, self.Sprite.x]
        if Case_Actuelle >= 2 and Case_Actuelle < 10:
            rencontre = r.randint(1,10)
            if rencontre == 1:
                
                
                PokeRencontre = ZoneRencontre(Case_Actuelle).Random_Poke()
                #Poke_Rencontre = Zone.Random_Poke()
                self.Sprite.Changement_Sprite(f"./Animation/Marche/{Direction}_repos.png")
                self.MainWindow.Menu = "Combat"
                Tr = Transition(self.MainWindow)
                self.Jukebox.ChangeDeMusique("./Son/Battle.wav")
                Tr.start()
                Tr.show()
                #self.MainWindow.Combat = Combat(self.Equipe, PokeRencontre, self.UICombat)
                QtTest.QTest.qWait(1900)
                self.Carte.hide()
                self.Sprite.hide()
                self.Legend.hide()
                Menu = self.UICombat.Init_Combat(self.Equipe,PokeRencontre)
                QtTest.QTest.qWait(900)
                Tr.hide()
                Tr.stop()
        
        #Déplacements avec les portes
        if Case_Actuelle == 100:
            QtTest.QTest.qWait(500)
            self.Porte(self.Sprite.y, self.Sprite.x)
        
        
        #On récupère le temps de fin, pour pas avoir une commande qui s'execute pendant l'animation en cours.
        KeyTime = datetime.now()
        return KeyTime, Menu
    
    def Porte(self, y, x):
        #Dictionnaire qui asssocie à une entrée (une porte) sa sortie
        Dico_portes = {(4,7):((89,9),"Cave"),(90,9):((5,7),"Route1"),(94,45):((72,85),"Desert"),(71,85):((93,45),"Cave"),(62,50):((13,69),"Cave"),(14,69):((63,50),"Route1"),(9,19):((94,87),"Center"),(95,87):((10,19),"Route1")}    
        (Y_sortie,X_sortie),musique = Dico_portes[(y,x)][0], Dico_portes[(y,x)][1]
        deltaY = Y_sortie - y
        deltaX = X_sortie - x
        self.Carte.Warp(deltaY, deltaX, musique)
    
        
    def end_move(self,Direction):
        #On arrête l'animation et place le personnage dans la position de repos de sa direction.
        self.Sprite.Changement_Sprite(f"./Animation/Marche/{Direction}_repos.png")
        
class Transition():
    def __init__(self, MainWindow):
        self.battletr = QtWidgets.QLabel(MainWindow)
        self.battletr.hide()
        self.battletr.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.battletr.setText("")
        self.battletr.setScaledContents(True)
        self.battletr.setObjectName("Transition")
        
        self.movie = QMovie("./Animation/Combat/BattleStart.gif")
        self.battletr.setMovie(self.movie)

    def show(self):
        self.battletr.show()
    def hide(self):
        self.battletr.hide()
    def start(self):
        self.movie.start()
    def stop(self):
        self.movie.stop()
        