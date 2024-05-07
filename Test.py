from PIL import Image
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
            
    def setupUi(self):
        
        #On initialise la fenêtre de jeu
        self.setObjectName("Dialog")
        self.resize(500, 500)
        self.setWindowTitle("PyQTmon")
        
        #Définition du Jukebox
        self.Jukebox = Jukebox("./Son/Route1.wav")
        
        #Création de la carte et du sprite du personnage principal
        self.map = Carte(self,"./Carte.png")
        
        im = Image.open("./Animation/Marche/Devant_repos.png")
        im1 = im.crop((0,0,5,5))
        im1.save("./Temp/Test.png")
        self.SpritePerso = Sprite(self,"./Temp/Test.png", 243, 240, 15, 19, "Perso_Principal")
        
    
        
        
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())