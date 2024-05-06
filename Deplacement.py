from datetime import datetime
from PyQt5.QtMultimedia import QSound
import random as r

class Deplacement():
    def __init__(self, MainWindow):
        self.Sprite = MainWindow.SpritePerso
        self.Carte = MainWindow.map
        self.Jukebox = MainWindow.Jukebox
        self.battle = MainWindow.battle
        self.UICombat = MainWindow.UICombat
        
    
    def move(self,Direction):
        #On regarde si une animation n'est pas déjà en cours s'il n'y en a pas. On remplace le jpg par un gif.
        if not self.Sprite.IsAnimated:
            self.Sprite.Animation(f"./Animation/Marche/{Direction}.gif")
        self.Carte.Glissement(Direction,self.Sprite)
        
        #Rencontre_Aleatoire
        if self.Carte.matrice_dalle[self.Sprite.y, self.Sprite.x] >= 2:
            rencontre = r.randint(1,20)
            if rencontre == 1:
                self.Jukebox.ChangeDeMusique("./Son/Battle.wav")
                self.battle = True
                self.Carte.hide()
                self.Sprite.Changement_Sprite(f"./Animation/Marche/{Direction}_repos.png")
                self.Sprite.hide()
                self.UICombat.show()
        
        #On récupère le temps de fin, pour pas avoir une commande qui s'execute pendant l'animation en cours.
        KeyTime = datetime.now()
        return KeyTime, self.battle
        
    def end_move(self,Direction):
        #On arrête l'animation et place le personnage dans la position de repos de sa direction.
        self.Sprite.Changement_Sprite(f"./Animation/Marche/{Direction}_repos.png")