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
from Mecaniques import Pokemon
from GestionCombat import Equipe, PC
from Gestion_Son import Jukebox
from Menus import Menu_Gestion
from PC import Menu_PC



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        #Pour gérer les 
        self.KeyTime = datetime.now()
        self.KeyTime_Delta = timedelta(seconds=0.15)
        self.setFocusPolicy(Qt.StrongFocus)
        
    def keyPressEvent(self, event):
        #Lorsqu'une touche est pressée, on déclenche l'animation de marche et on déplace la carte.
        #Note : C'est la carte qui bouge et non le joueur (Effet tapis roulant)
        if self.Menu == "Carte":
            if event.key() == Qt.Key_Up and datetime.now() - self.KeyTime > self.KeyTime_Delta:
                self.KeyTime, self.Menu = self.Deplacement.move("Derriere")
                self.SpritePerso.Orientation = "Derriere"
            if event.key() == Qt.Key_Down and datetime.now() - self.KeyTime > self.KeyTime_Delta:
                self.KeyTime, self.Menu = self.Deplacement.move("Devant")
                self.SpritePerso.Orientation = "Devant"
            if event.key() == Qt.Key_Right and datetime.now() - self.KeyTime > self.KeyTime_Delta:
                self.KeyTime, self.Menu = self.Deplacement.move("Droite")
                self.SpritePerso.Orientation = "Droite"
            if event.key() == Qt.Key_Left and datetime.now() - self.KeyTime > self.KeyTime_Delta:
                self.KeyTime, self.Menu = self.Deplacement.move("Gauche")
                self.SpritePerso.Orientation = "Gauche"
            if event.key() == Qt.Key_Enter:
                self.Menu = "Menu_Chgmt_Pokémon"
                self.Menu_Gestion.Menu_Init(self.map, "Carte", self.Equipe)
                #Entrer dans le menu pour switcher de pokemon
            if event.key() == Qt.Key_Space:
                self.map.Interaction(self.SpritePerso, self.Equipe)
                
        elif self.Menu == "Combat": 
            if self.UICombat.MenuActuel != "Switch":
                if event.key() == Qt.Key_Up:
                    self.UICombat.deplacement_fleche_menu("Haut")
                if event.key() == Qt.Key_Down:
                    self.UICombat.deplacement_fleche_menu("Bas")
                if event.key() == Qt.Key_Right:
                    self.UICombat.deplacement_fleche_menu("Droite")
                if event.key() == Qt.Key_Left:
                    self.UICombat.deplacement_fleche_menu("Gauche")
            if event.key() == Qt.Key_Space:
                self.UICombat.valide(self.Equipe)
            
            if event.key() == Qt.Key_X:
                self.UICombat.retour()
                
        elif self.Menu == "PC":
            if event.key() == Qt.Key_X:
                print(self.Menu)
                self.Menu_PC.hide()
                self.map.show()
                self.Menu = "Carte"
    
    #Lorsqu'on relâche une touche, il faut arrêter l'animation de marche.
    def keyReleaseEvent(self, event):
        if self.Menu == "Carte":
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
        
        #Création de l'équipe initiale du joueur ainsi que son PC
        Pokemon1, Pokemon2, Pokemon3 = Pokemon(), Pokemon(), Pokemon()
        Pokemon1.FromID(1), Pokemon2.FromID(4), Pokemon3.FromID(7)
        self.Equipe = Equipe(Pokemon2,Pokemon1,Pokemon3)
        self.PC = PC()
        
        #Variable utile de Gestion des menus 
        self.Menu = "Carte"
        
        #Création de la carte et du sprite du personnage principal
        self.SpritePerso = Sprite(self,"./Animation/Marche/Devant_repos.png", 243, 240, 45, 57, "Perso_Principal")
        self.map = Carte(self,"./Map/carte2.png")
        
        #On met le sprite devant la carte
        self.SpritePerso.Label.raise_()
        
        
        self.UICombat = InterfaceCombat(self,Pokemon())
        self.UICombat.hide()
        self.Deplacement = Deplacement(self)
        self.Menu_Gestion = Menu_Gestion(self)
        self.Menu_Gestion.hide()
        self.Menu_PC = Menu_PC(self)
        self.Menu_PC.hide()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
        