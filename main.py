#Import externe
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.Qt import Qt
import sys
from datetime import datetime
from datetime import timedelta

#Import Interne
from Deplacement import Deplacement
from CarteEtSprite import Carte,Sprite
from CombatUI import InterfaceCombat
from Mecaniques import Pokemon, Attaque
from GestionCombat import Equipe
from Gestion_Son import Jukebox


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.KeyTime = datetime.now()
        self.KeyTime_Delta = timedelta(seconds=0.075)
        
    def keyPressEvent(self, event):   
        #Lorsqu'une touche est pressée, on déclenche l'animation de marche et on déplace la carte.
        #Note : C'est la carte qui bouge et non le joueur (Effet tapis roulant)
        if not self.battle:
            if event.key() == Qt.Key_Up and datetime.now() - self.KeyTime > self.KeyTime_Delta:
                self.KeyTime, self.battle = self.Deplacement.move("Derriere")
            if event.key() == Qt.Key_Down and datetime.now() - self.KeyTime > self.KeyTime_Delta:
                self.KeyTime, self.battle = self.Deplacement.move("Devant")
            if event.key() == Qt.Key_Right and datetime.now() - self.KeyTime > self.KeyTime_Delta:
                self.KeyTime, self.battle = self.Deplacement.move("Droite")
            if event.key() == Qt.Key_Left and datetime.now() - self.KeyTime > self.KeyTime_Delta:
                self.KeyTime, self.battle = self.Deplacement.move("Gauche")
                
        else:
            if event.key() == Qt.Key_Escape:
                self.UICombat.hide()
                self.battle = False
                self.Deplacement.battle = False
                self.map.show()
                self.SpritePerso.show()
                self.Jukebox.ChangeDeMusique("./Son/Route1.wav")
            if not self.UICombat.MenuSwitch and not self.UICombat.MenuAttaque:
                if event.key() == Qt.Key_Up:
                    self.UICombat.deplacement_fleche_menu("Haut")
                if event.key() == Qt.Key_Down:
                    self.UICombat.deplacement_fleche_menu("Bas")
                if event.key() == Qt.Key_Right:
                    self.UICombat.deplacement_fleche_menu("Droite")
                if event.key() == Qt.Key_Left:
                    self.UICombat.deplacement_fleche_menu("Gauche")
            if event.key() == Qt.Key_Space:
                self.UICombat.valide()
                
    
    #Lorsqu'on relâche une touche, il faut arrêter l'animation de marche.
    def keyReleaseEvent(self, event):
        if not self.battle:
            if event.key() == Qt.Key_Left and not event.isAutoRepeat():
                self.Deplacement.end_move("Gauche")
            if event.key() == Qt.Key_Right and not event.isAutoRepeat():
                self.Deplacement.end_move("Droite")
            if event.key() == Qt.Key_Up and not event.isAutoRepeat():
                self.Deplacement.end_move("Derriere")
            if event.key() == Qt.Key_Down and not event.isAutoRepeat():
                self.Deplacement.end_move("Devant")      
            
    def setupUi(self):
        
        #On initialise la fenêtre de jeu
        self.setObjectName("Dialog")
        self.resize(500, 500)
        self.setWindowTitle("PyQTmon")
        
        #Définition du Jukebox
        self.Jukebox = Jukebox("./Son/Route1.wav")
        
        #Création de la carte et du sprite du personnage principal
        self.map = Carte(self,"./Carte.png")
        self.SpritePerso = Sprite(self,"./Animation/Marche/Devant_repos.png", 243, 240, 45, 57, "Perso_Principal")
        
        
        #Création de l'équipe initiale du joueur
        Attaque1 = Attaque("Jet de Pierre", "Physique", 80, "Roche", 100)
        Attaque2 = Attaque("Plaie-Croix", "Physique", 80, "Insecte", 100)
        Attaque3 = Attaque("Charge", "Physique", 80, "Normal", 100)
        Pokemon1 = Pokemon(213,"Caratroc pas shiny","Roche","Insecte",[20,10,230,10,230,5], [Attaque1,Attaque2,Attaque3])
        Pokemon2 = Pokemon(1, "Bulbizarre", "Plante", "Poison", [45,49,49,65,65,45], [Attaque2,Attaque3])
        Pokemon3 = Pokemon(213,"Caratroc shiny","Roche","Insecte",[20,10,230,10,230,5], [Attaque1,Attaque2,Attaque3])
        
        self.Equipe = Equipe(Pokemon2, Pokemon1)
        self.WildPoke = Pokemon3
        
        self.battle = False
        self.UICombat = InterfaceCombat(self)
        self.UICombat.hide()
        self.Deplacement = Deplacement(self)
        
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
        