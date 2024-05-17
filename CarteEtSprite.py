# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtMultimedia import QSound
from PyQt5 import QtTest
from Interface import Interface
from Mecaniques import ZoneRencontre, Pokemon
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
        self.matrice_dalle = np.genfromtxt("./data/Matrice2.csv", delimiter=";")
        
        #Définition bruitage qui ont lieu sur la carte
        self.BumpSound = QSound("./Son/Bump.wav")
        self.Healing = QSound("./Son/Healing.wav")
        self.PCSound = QSound("./Son/PC.wav")
        
    def Glissement(self,Direction,Sprite,Legendaire):
        #On crée une animation pour que la carte glisse sous le joueur (Et que ça soit plus fluide qu'une simple téléportation)
        #La direction est donnée par la méthode move de déplacement. 
        
        self.anim = QtCore.QPropertyAnimation(self.carte, b'geometry')
        self.anim.setDuration(50)
        rect = self.carte.geometry()
        self.anim.setStartValue(rect)
        
        #En fonction de la direction. Et si la case l'autorise, on translate la carte, et on actualise la position du joueur.
        if Direction == "Derriere":
            if self.matrice_dalle[Sprite.y-1, Sprite.x] != 0 and self.matrice_dalle[Sprite.y-1, Sprite.x] not in [51,52,101,102,144,145,146,150,151]:
                Sprite.x, Sprite.y = Sprite.x, Sprite.y-1
                rect.translate(0,48)
            else:
                #Si ce n'est pas possible, on ne fait rien et on joue un BUMP
                self.BumpSound.play()        
            
        elif Direction == "Devant":
            if self.matrice_dalle[Sprite.y+1, Sprite.x] != 0 and self.matrice_dalle[Sprite.y+1, Sprite.x] not in [51,52,101,102,144,145,146,150,151]:
                Sprite.x, Sprite.y = Sprite.x, Sprite.y+1
                rect.translate(0,-48)
            else:
                self.BumpSound.play()
            
        elif Direction == "Gauche":
            if self.matrice_dalle[Sprite.y, Sprite.x-1] != 0 and self.matrice_dalle[Sprite.y, Sprite.x-1] not in [51,52,101,102,144,145,146,150,151]:
                Sprite.x, Sprite.y = Sprite.x-1, Sprite.y
                rect.translate(48,0)
            else:
                self.BumpSound.play()
            
        elif Direction == "Droite":
            if self.matrice_dalle[Sprite.y, Sprite.x+1] != 0 and self.matrice_dalle[Sprite.y, Sprite.x+1] not in [51,52,101,102,144,145,146,150,151]:
                Sprite.x, Sprite.y = Sprite.x+1, Sprite.y
                rect.translate(-48,0)
            else:
                self.BumpSound.play()
        
        #On regarde s'il n'y a pas un légendaire dans les parages après déplacement, et on l'affiche si c'est le cas.
        self.MainWindow.SpriteLegend.show(Sprite)
            
        #On joue l'animation de glissement
        self.anim.setEndValue(rect)
        self.anim.start()
    
        
    def Warp(self, deltaY, deltaX, musique):
        """Cette méthode permet de téléporter un joueur sur la carte, ainsi qu'attribuer une nouvelle musique de zone après téléportation"""
        self.Jukebox.ChangeDeMusique(f"./Son/{musique}.wav")
        self.Jukebox.MusiqueDeZone = f"./Son/{musique}.wav"
        
        #On définit un menu virtuel pour empêcher le joueur de faire qqchose pendant la téléportation
        self.MainWindow.Menu = "Dummy"
        
        #Définition de la nouvelle position et glissement de la carte à la nouvelle position.
        rect = self.carte.geometry()
        rect.translate(-deltaX*48, -deltaY*48)
        self.Sprite.y += deltaY
        self.Sprite.x += deltaX
        self.carte.setGeometry(rect)
        
        #On attend un peu et on repasse dans le menu carte, réautorisant le joueur à se déplacer.
        QtTest.QTest.qWait(200)
        self.MainWindow.Menu = "Carte"
    
    def Interaction(self, Sprite, Equipe):
        """Vérifie si le joueur est à côté d'une case avec laquelle il peut interagir, et réalise l'interaction, cette
        méthode se lance si le joueur utilise espace sur le menu Carte."""
        
        #Récupération de la position
        y = Sprite.y
        x = Sprite.x
        
        #Définition des interactions
        if (y-1,x) == (89,87) and Sprite.Orientation == "Derriere": #Si on parle au comptoir dans le Pokémon Center
            
            #On joue une musique et bloque le personnage en le mettant dans un Menu fictif
            self.Healing.play()
            self.MainWindow.Menu = "Healing"
            
            #Affichage d'un dialogue le temps du soin
            self.Soin_PC = QtWidgets.QLabel(self.MainWindow)
            self.Soin_PC.setGeometry(QtCore.QRect(20, 385, 460, 100))
            self.Soin_PC.setPixmap(QtGui.QPixmap("./images/ecran_soin.png"))
            self.Soin_PC_texte = QtWidgets.QLabel(self.MainWindow)
            self.Soin_PC_texte.setGeometry(QtCore.QRect(40, 390, 440, 80))
            self.Soin_PC_texte.setText("Un instant, je soigne vos pokémons.")
            font = self.font # police venant du jeu Pokémon FireRed & LeafGreen
            font.setPointSize(9)
            self.Soin_PC_texte.setFont(font)
            self.Soin_PC_texte.setObjectName("Soin_PC_texte")
            self.Soin_PC.show()
            self.Soin_PC_texte.show()
            
            #On attend, la fin de la musique et on libère le joueur.
            QtTest.QTest.qWait(4000)
            self.Soin_PC.hide()
            self.Soin_PC_texte.hide()
            self.MainWindow.Menu = "Carte"
            
            #Et on soigne l'équipe
            Equipe.Soin_All()
            
        if (y-1,x) == (87,91) and Sprite.Orientation == "Derriere": #Si on parle au PC
            #On passe dans le menu PC (Avec un petit bruitage au passage), et on l'affiche.
            self.MainWindow.Menu = "PC"
            self.PCSound.play()
            QtTest.QTest.qWait(1000)
            self.hide()
            self.MainWindow.Menu_PC.Init_PC()
        
        #Pêche
        #On vérifie dans chaque direction si on n'est pas en face d'une case de pêche.
        Peche = False
        if (self.matrice_dalle[Sprite.y, Sprite.x-1] == 52 or self.matrice_dalle[Sprite.y, Sprite.x-1] ==51) and Sprite.Orientation == "Gauche":
            PokeRencontre = ZoneRencontre(self.matrice_dalle[Sprite.y, Sprite.x-1]).Random_Poke()
            Direction = Sprite.Orientation
            Peche = True
        elif (self.matrice_dalle[Sprite.y+1, Sprite.x] == 52 or self.matrice_dalle[Sprite.y+1, Sprite.x] == 51) and Sprite.Orientation == "Devant":
            PokeRencontre = ZoneRencontre(self.matrice_dalle[Sprite.y+1, Sprite.x]).Random_Poke()
            Direction = Sprite.Orientation
            Peche = True
        elif (self.matrice_dalle[Sprite.y, Sprite.x+1] == 52 or self.matrice_dalle[Sprite.y, Sprite.x+1] == 51) and Sprite.Orientation == "Droite":
            PokeRencontre = ZoneRencontre(self.matrice_dalle[Sprite.y, Sprite.x+1]).Random_Poke()
            Direction = Sprite.Orientation
            Peche = True
        elif (self.matrice_dalle[Sprite.y-1, Sprite.x] == 52 or self.matrice_dalle[Sprite.y-1, Sprite.x] == 51) and Sprite.Orientation == "Derriere":
            PokeRencontre = ZoneRencontre(self.matrice_dalle[Sprite.y-1, Sprite.x]).Random_Poke()
            Direction = Sprite.Orientation
            Peche = True
        #Si on peut pêcher, ça lance la phase de pêche
        if Peche:
            #Animation de pêche
            self.Sprite.Animation_Peche(Direction)
            
            #On bloque le joueur, avec un menu fictif et on lance la phase de combat. 
            self.MainWindow.Menu = "Dummy"
            QtTest.QTest.qWait(1000)
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
            self.Sprite.Fin_Animation_Peche(Direction)
            Tr.hide()
            Tr.stop()
            
        #Légendaire
        #On teste dans toutes les directions si on n'est pas en train de parler à un pokémon légendaire.
        Legend_Proche = False
        if self.matrice_dalle[y,x-1] >= 144 and Sprite.Orientation == "Gauche" and not self.SpriteLegendaire.dico_rencontre[self.SpriteLegendaire.ID]:
            Legend_Proche = True
        elif self.matrice_dalle[y+1,x] >= 144 and Sprite.Orientation == "Devant" and not self.SpriteLegendaire.dico_rencontre[self.SpriteLegendaire.ID]:
            Legend_Proche = True
        elif self.matrice_dalle[y,x+1] >= 144 and Sprite.Orientation == "Droite" and not self.SpriteLegendaire.dico_rencontre[self.SpriteLegendaire.ID]:
            Legend_Proche = True
        elif self.matrice_dalle[y-1,x] >= 144 and Sprite.Orientation == "Derriere" and not self.SpriteLegendaire.dico_rencontre[self.SpriteLegendaire.ID]:
            Legend_Proche = True
            
        #Si c'est le cas, on lance un combat contre lui.
        if Legend_Proche:
            Direction = Sprite.Orientation
            Pokemon_Legendaire = Pokemon()
            Pokemon_Legendaire.FromID(self.SpriteLegendaire.ID) #Création du pokémon légendaire contre qui le joueur va se battre
            self.Sprite.Changement_Sprite(f"./Animation/Marche/{Direction}_repos.png")
            self.MainWindow.Menu = "Combat"
            Tr = Transition(self.MainWindow)
            self.Jukebox.ChangeDeMusique("./Son/Legendaire.wav")
            Tr.start()
            Tr.show()
            QtTest.QTest.qWait(1900)
            self.carte.hide()
            self.Sprite.hide()
            self.SpriteLegendaire.hide()
            self.MainWindow.UICombat.Init_Combat(self.Equipe,Pokemon_Legendaire)
            QtTest.QTest.qWait(900)
            Tr.hide()
            Tr.stop()
            self.SpriteLegendaire.dico_rencontre[self.SpriteLegendaire.ID] = True #Empêcher de re-combattre ce pokémon légendaire
            
    #Surcharge des méthodes hide et show de la classe abstraite Interface, pour facilement (dés)afficher la carte.
    def hide(self):
        self.carte.hide()
        self.Sprite.hide()
        
    def show(self):
        self.carte.show()
        self.Sprite.show()
        
        
class Sprite:
    """Définit le sprite du joueur, sa position, et s'il est en cours d'animation ou non"""
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
        """Permet de lancer les animations de marche"""
        self.movie = QMovie(Gif)
        self.Label.setMovie(self.movie)
        self.movie.start()
        self.IsAnimated = True
        
    def Animation_Peche(self,Direction):
        """Les sprites de pêches ayant une taille différentes des sprites de marche, on est obligé de créer une méthode à part
        pour les animer."""
        
        self.movie = QMovie(f"./Animation/Peche/{Direction}.gif")
        rect = self.Label.geometry()
        rect.setHeight(96)
        rect.setWidth(96)
        if Direction == "Devant" or Direction == "Derriere":
            rect.translate(-25,-20)
        if Direction == "Droite" or Direction == "Gauche":
            rect.translate(-25,-40)
        self.Label.setGeometry(rect)
        self.Label.setMovie(self.movie)
        self.movie.start()
        self.IsAnimated = True
        
    def Fin_Animation_Peche(self,Direction):
        """Termine une animation de pêche"""
        self.movie.stop()
        rect = self.Label.geometry()
        rect.setHeight(57)
        rect.setWidth(45)
        self.Changement_Sprite(f"./Animation/Marche/{Direction}_repos.png")
        if Direction == "Devant" or Direction == "Derriere":
            rect.translate(25,20)
        if Direction == "Droite" or Direction == "Gauche":
            rect.translate(25,40)
        self.Label.setGeometry(rect)
        self.IsAnimated = False
    
    
    #Pour simplement (dés)afficher le sprite de la carte
    def hide(self):
        self.Label.hide()
            
    def show(self):
        self.Label.show()


class Legendaire():
    """Définit l'apparition des sprites des légendaires et leur ID associé pour les rencontrer"""
    def __init__(self,MainWindow, larg=48, haut=48):
        #Définition de l'encart contenant le sprite
        self.Label = QtWidgets.QLabel(MainWindow)
        self.Label.setGeometry(QtCore.QRect(4800, 4800 , larg, haut))
        self.Label.setScaledContents(False)
        
        self.dico_rencontre = {151:False, 150:False, 146:False, 145:False, 144:False}
        
    def hide(self):
        #Le label reste toujours présent, on affiche juste rien dedans.
        self.Label.setPixmap(QtGui.QPixmap("Dummy.JPG"))
            
    def show(self, Sprite):
        """Définit le glissement du pokémon légendaire sur la carte, pour qu'il glisse à la même vitesse que la carte"""
        
        self.anim = QtCore.QPropertyAnimation(self.Label, b'geometry')
        self.anim.setDuration(50)
        rect = self.Label.geometry()
        self.anim.setStartValue(rect)
        
        #Mew
        if abs(Sprite.y-24) <= 6 and abs(Sprite.x-33) <= 6 and not self.dico_rencontre[151]:
            self.ID = 151
            dX, dY = 33-Sprite.x, 24-Sprite.y
            self.Label.setPixmap(QtGui.QPixmap("./Legendaire/Mew.png"))
            rect.setRect(243+dX*48, 240+dY*48, 48, 48)
        #Mewtwo
        elif abs(Sprite.y-8) <= 6 and abs(Sprite.x-70) <= 6 and not self.dico_rencontre[150]:
            self.ID = 150
            dX, dY = 70-Sprite.x, 8-Sprite.y
            self.Label.setPixmap(QtGui.QPixmap("./Legendaire/Mewtwo.png"))
            rect.setRect(243+dX*48, 240+dY*48, 48, 48)
        #Sulfura
        elif abs(Sprite.y-57) <= 6 and abs(Sprite.x-86) <= 6 and not self.dico_rencontre[146]:
            self.ID = 146
            dX, dY = 86-Sprite.x, 57-Sprite.y
            self.Label.setPixmap(QtGui.QPixmap("./Legendaire/Sulfura.png"))
            rect.setRect(243+dX*48, 240+dY*48, 48, 48)
        #Electhor
        elif abs(Sprite.y-12) <= 6 and abs(Sprite.x-89) <= 6 and not self.dico_rencontre[145]:
            self.ID = 145
            dX, dY = 89-Sprite.x, 12-Sprite.y
            self.Label.setPixmap(QtGui.QPixmap("./Legendaire/Electhor.png"))
            rect.setRect(243+dX*48, 240+dY*48, 48, 48)
        #Artikodin
        elif abs(Sprite.y-64) <= 6 and abs(Sprite.x-12) <= 6 and not self.dico_rencontre[144]:
            self.ID = 144
            dX, dY = 12-Sprite.x, 64-Sprite.y
            self.Label.setPixmap(QtGui.QPixmap("./Legendaire/Artikodin.png"))
            rect.setRect(243+dX*48, 240+dY*48, 48, 48)
            
        self.anim.setEndValue(rect)
        self.anim.start()