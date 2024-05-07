from datetime import datetime
from PyQt5.QtMultimedia import QSound
import random as r
from CombatUI import Combat
from Mecaniques import ZoneRencontre
from PyQt5 import QtTest

class Deplacement():
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        self.Sprite = MainWindow.SpritePerso
        self.Carte = MainWindow.map
        self.Jukebox = MainWindow.Jukebox
        self.UICombat = MainWindow.UICombat
        
        #
        self.Equipe = MainWindow.Equipe
        
    
    def move(self,Direction):
        
        Battle = False
        #On regarde si une animation n'est pas déjà en cours s'il n'y en a pas. On remplace le jpg par un gif.
        if not self.Sprite.IsAnimated:
            self.Sprite.Animation(f"./Animation/Marche/{Direction}.gif")
        self.Carte.Glissement(Direction,self.Sprite)
        
        #Rencontre_Aleatoire
        Case_Actuelle = self.Carte.matrice_dalle[self.Sprite.y, self.Sprite.x]
        if Case_Actuelle >= 2:
            rencontre = r.randint(1,10)
            if rencontre == 1:
                
                
                PokeRencontre = ZoneRencontre(Case_Actuelle).Random_Poke()
                #Poke_Rencontre = Zone.Random_Poke()
                
                
                
                self.Sprite.Changement_Sprite(f"./Animation/Marche/{Direction}_repos.png")
                self.Jukebox.ChangeDeMusique("./Son/Battle.wav")
                self.MainWindow.battle = True
                QtTest.QTest.qWait(2000)
                self.Carte.hide()
                self.Sprite.hide()              
                Combat_Aleatoire = Combat(self.Equipe, PokeRencontre, self.UICombat)
                Battle = Combat_Aleatoire.Init_Combat()
                
                
                """PokemonSauv = Pokemon.WildPoke(Zone_rencontre)
                Combat(Equipe,PokemonSauv)"""
        
        #On récupère le temps de fin, pour pas avoir une commande qui s'execute pendant l'animation en cours.
        KeyTime = datetime.now()
        return KeyTime, Battle
        
    def end_move(self,Direction):
        #On arrête l'animation et place le personnage dans la position de repos de sa direction.
        self.Sprite.Changement_Sprite(f"./Animation/Marche/{Direction}_repos.png")