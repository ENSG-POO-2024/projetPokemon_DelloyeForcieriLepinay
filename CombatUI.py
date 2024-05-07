from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtTest


#Définit tous les composants de l'interface de combat (Assez indigeste) ...
class InterfaceCombat(object):
    def __init__(self, MainWindow):
        
        #Définition de quelques booléens pour savoir dans quel menu on se situe
        self.position_fleche = "Haut","Gauche" 
        self.MenuSwitch = False
        self.MenuAttaque = False
        
        #On récupère le nom 
        self.MainWindow = MainWindow
        
        #On crée une zone de combat (Sprite des pokémons + Barre de PVs + Nom des pokémons)
        self.Zone_Combat = QtWidgets.QFrame(MainWindow)
        self.Zone_Combat.setGeometry(QtCore.QRect(10, 10, 480, 320))
        self.Zone_Combat.setFrameShape(QtWidgets.QFrame.Box)
        self.Zone_Combat.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Zone_Combat.setObjectName("Zone_Combat")
        self.Sprite_Dos = QtWidgets.QLabel(self.Zone_Combat)
        self.Sprite_Dos.setGeometry(QtCore.QRect(40, 210, 128, 128))
        self.Sprite_Dos.setText("")
        self.Sprite_Dos.setPixmap(QtGui.QPixmap("1.png"))
        self.Sprite_Dos.setScaledContents(True)
        self.Sprite_Dos.setObjectName("Sprite_Dos")
        self.Sprite_Face = QtWidgets.QLabel(self.Zone_Combat)
        self.Sprite_Face.setGeometry(QtCore.QRect(310, 20, 128, 128))
        self.Sprite_Face.setText("")
        self.Sprite_Face.setPixmap(QtGui.QPixmap("2.png"))
        self.Sprite_Face.setScaledContents(True)
        self.Sprite_Face.setObjectName("Sprite_Face")
        self.PV_Ennemi = QtWidgets.QLabel(self.Zone_Combat)
        self.PV_Ennemi.setGeometry(QtCore.QRect(10, 10, 300, 90))
        self.PV_Ennemi.setText("")
        self.PV_Ennemi.setPixmap(QtGui.QPixmap("../Projet_Pokemon/BarreEnnemie.png"))
        self.PV_Ennemi.setScaledContents(True)
        self.PV_Ennemi.setObjectName("PV_Ennemi")
        self.PV_Allie = QtWidgets.QLabel(self.Zone_Combat)
        self.PV_Allie.setGeometry(QtCore.QRect(160, 200, 315, 120))
        self.PV_Allie.setText("")
        self.PV_Allie.setPixmap(QtGui.QPixmap("../Projet_Pokemon/BarreAlliee.png"))
        self.PV_Allie.setScaledContents(True)
        self.PV_Allie.setObjectName("PV_Allie")
        self.Nom_PokeAllie = QtWidgets.QLabel(self.Zone_Combat)
        self.Nom_PokeAllie.setGeometry(QtCore.QRect(205, 217, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Nom_PokeAllie.setFont(font)
        self.Nom_PokeAllie.setObjectName("Nom_PokeAllie")
        self.Nom_PokeEnnemi = QtWidgets.QLabel(self.Zone_Combat)
        self.Nom_PokeEnnemi.setGeometry(QtCore.QRect(30, 23, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Nom_PokeEnnemi.setFont(font)
        self.Nom_PokeEnnemi.setObjectName("Nom_PokeEnnemi")
        self.PVBarre_Allie = QtWidgets.QProgressBar(self.Zone_Combat)
        self.PVBarre_Allie.setGeometry(QtCore.QRect(300, 242, 151, 31))
        self.PVBarre_Allie.setProperty("value", 50)
        self.PVBarre_Allie.setTextVisible(False)
        self.PVBarre_Allie.setObjectName("PVBarre_Allie")
        self.PVBarre_Ennemi = QtWidgets.QProgressBar(self.Zone_Combat)
        self.PVBarre_Ennemi.setGeometry(QtCore.QRect(120, 50, 161, 31))
        self.PVBarre_Ennemi.setProperty("value", 100)
        self.PVBarre_Ennemi.setTextVisible(False)
        self.PVBarre_Ennemi.setObjectName("PVBarre_Ennemi")
        self.PVBarre_Allie.raise_()
        self.PVBarre_Ennemi.raise_()
        self.Sprite_Dos.raise_()
        self.Sprite_Face.raise_()
        self.PV_Ennemi.raise_()
        self.PV_Allie.raise_()
        self.Nom_PokeAllie.raise_()
        self.Nom_PokeEnnemi.raise_()
        self.PV_Ennemi = QtWidgets.QLabel(self.Zone_Combat)
        self.PV_Ennemi.setGeometry(QtCore.QRect(10, 10, 300, 90))
        self.PV_Ennemi.setText("")
        self.PV_Ennemi.setPixmap(QtGui.QPixmap("./BarreEnnemie.png"))
        self.PV_Ennemi.setScaledContents(True)
        self.PV_Ennemi.setObjectName("PV_Ennemi")
        self.PV_Allie = QtWidgets.QLabel(self.Zone_Combat)
        self.PV_Allie.setGeometry(QtCore.QRect(160, 200, 315, 120))
        self.PV_Allie.setText("")
        self.PV_Allie.setPixmap(QtGui.QPixmap("./BarreAlliee.png"))
        self.PV_Allie.setScaledContents(True)
        self.PV_Allie.setObjectName("PV_Allie")
        self.Nom_PokeAllie = QtWidgets.QLabel(self.Zone_Combat)
        self.Nom_PokeAllie.setGeometry(QtCore.QRect(205, 217, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Nom_PokeAllie.setFont(font)
        self.Nom_PokeAllie.setObjectName("Nom_PokeAllie")
        self.Nom_PokeEnnemi = QtWidgets.QLabel(self.Zone_Combat)
        self.Nom_PokeEnnemi.setGeometry(QtCore.QRect(30, 23, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Nom_PokeEnnemi.setFont(font)
        self.Nom_PokeEnnemi.setObjectName("Nom_PokeEnnemi")
        
        #On définit un premier menu qui servira à choisir les actions ou les attaques.
        self.Choix_Attaque = QtWidgets.QFrame(MainWindow)
        self.Choix_Attaque.setGeometry(QtCore.QRect(10, 390, 480, 100))
        self.Choix_Attaque.setFrameShape(QtWidgets.QFrame.Box)
        self.Choix_Attaque.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Choix_Attaque.setObjectName("Choix_Attaque")
        self.Choix_1 = QtWidgets.QLabel(self.Choix_Attaque)
        self.Choix_1.setGeometry(QtCore.QRect(0, 0, 240, 50))
        self.Choix_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Choix_1.setObjectName("Choix_1")
        self.Choix_2 = QtWidgets.QLabel(self.Choix_Attaque)
        self.Choix_2.setGeometry(QtCore.QRect(240, 0, 240, 50))
        self.Choix_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Choix_2.setObjectName("Choix_2")
        self.Choix_3 = QtWidgets.QLabel(self.Choix_Attaque)
        self.Choix_3.setGeometry(QtCore.QRect(0, 50, 240, 50))
        self.Choix_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Choix_3.setObjectName("Choix_3")
        self.Choix_4 = QtWidgets.QLabel(self.Choix_Attaque)
        self.Choix_4.setGeometry(QtCore.QRect(240, 50, 240, 50))
        self.Choix_4.setAlignment(QtCore.Qt.AlignCenter)
        self.Choix_4.setObjectName("Choix_4")
        self.Fleche_1 = QtWidgets.QLabel(self.Choix_Attaque)
        self.Fleche_1.setGeometry(QtCore.QRect(77, 16, 16, 20))
        self.Fleche_1.setObjectName("Fleche_1")
        self.Fleche_2 = QtWidgets.QLabel(self.Choix_Attaque)
        self.Fleche_2.setGeometry(QtCore.QRect(320, 16, 16, 20))
        self.Fleche_2.setObjectName("Fleche_2")
        self.Fleche_3 = QtWidgets.QLabel(self.Choix_Attaque)
        self.Fleche_3.setGeometry(QtCore.QRect(77, 65, 16, 20))
        self.Fleche_3.setObjectName("Fleche_3")
        self.Fleche_4 = QtWidgets.QLabel(self.Choix_Attaque)
        self.Fleche_4.setGeometry(QtCore.QRect(320, 65, 16, 20))
        self.Fleche_4.setObjectName("Fleche_4")
        
        #Puis une boîte de dialogue qui servira à donner des informations au joueur (Efficacité de l'attaque...etc)
        self.BoiteDialogue = QtWidgets.QTextBrowser(MainWindow)
        self.BoiteDialogue.setGeometry(QtCore.QRect(10, 340, 481, 41))
        self.BoiteDialogue.setObjectName("BoiteDialogue")
        
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.Nom_PokeAllie.setText(_translate("UICombat", "Caratroc"))
        self.Nom_PokeEnnemi.setText(_translate("UICombat", "Caratroc"))
        self.Choix_1.setText(_translate("UICombat", "Attaque"))
        self.Choix_2.setText(_translate("UICombat", "Switch"))
        self.Choix_3.setText(_translate("UICombat", "Capture"))
        self.Choix_4.setText(_translate("UICombat", "Fuite"))
        self.Fleche_1.setText(_translate("UICombat", "▶"))
        self.Fleche_2.setText(_translate("UICombat", "▶"))
        self.Fleche_3.setText(_translate("UICombat", "▶"))
        self.Fleche_4.setText(_translate("UICombat", "▶"))
        
    def show(self):
        self.Zone_Combat.show()
        self.Sprite_Dos.show()
        self.Sprite_Face.show()
        self.Choix_Attaque.show()
        self.Choix_1.show()
        self.Choix_2.show()
        self.Choix_3.show()
        self.Choix_4.show()
        self.Fleche_1.show()
        self.PVBarre_Allie.show()
        self.PVBarre_Ennemi.show()
        
        self.BoiteDialogue.show()
        
    def hide(self):
        self.Zone_Combat.hide()
        self.Sprite_Dos.hide()
        self.Sprite_Face.hide()
        self.Choix_Attaque.hide()
        self.Choix_1.hide()
        self.Choix_2.hide()
        self.Choix_3.hide()
        self.Choix_4.hide()
        self.Fleche_1.hide()
        self.Fleche_2.hide()
        self.Fleche_3.hide()
        self.Fleche_4.hide()
        self.PVBarre_Allie.hide()
        self.PVBarre_Ennemi.hide()
        self.BoiteDialogue.hide()
        
    def deplacement_fleche_menu(self, Direction):
        if self.position_fleche == ("Haut","Gauche"):
            if Direction == "Droite":
                self.Fleche_1.hide()
                self.Fleche_2.show()
                self.position_fleche = ("Haut","Droite")
            elif Direction == "Bas":
                self.Fleche_1.hide()
                self.Fleche_3.show()
                self.position_fleche = ("Bas","Gauche")
                
        elif self.position_fleche == ("Bas","Gauche"):
            if Direction == "Droite":
                self.Fleche_3.hide()
                self.Fleche_4.show()
                self.position_fleche = ("Bas","Droite")
            elif Direction == "Haut":
                self.Fleche_3.hide()
                self.Fleche_1.show()
                self.position_fleche = ("Haut","Gauche")
                
        if self.position_fleche == ("Haut","Droite"):
            if Direction == "Gauche":
                self.Fleche_2.hide()
                self.Fleche_1.show()
                self.position_fleche = ("Haut","Gauche")
            elif Direction == "Bas":
                self.Fleche_2.hide()
                self.Fleche_4.show()
                self.position_fleche = ("Bas","Droite")
                    
        if self.position_fleche == ("Bas","Droite"):
            if Direction == "Gauche":
                self.Fleche_4.hide()
                self.Fleche_3.show()
                self.position_fleche = ("Bas","Gauche")
            elif Direction == "Haut":
                self.Fleche_4.hide()
                self.Fleche_2.show()
                self.position_fleche = ("Haut","Droite")
        
    def deplacement_fleche_switch(self, Direction):
        pass
    
    def valide(self):
        pass


class Combat:
    def __init__(self,Equipe, Pokemon_Sauvage, CombatUI):
        self.Equipe = Equipe
        self.Pokemon_Adverse = Pokemon_Sauvage
        self.UI = CombatUI
    
    
    def Init_Combat(self):
        self.UI.Sprite_Dos
        self.UI.show()
        
        Pokemon1 = self.Equipe.pokemons[0]
        self.UI.Nom_PokeAllie.setText(Pokemon1.nom)
        self.UI.Nom_PokeEnnemi.setText(self.Pokemon_Adverse.nom)
        
        self.UI.PVBarre_Allie.setProperty("value", (Pokemon1.PV_actuel/Pokemon1.Stats[0])*100)
        self.UI.PVBarre_Ennemi.setProperty("value", 100)
        
        return True
            
    def actualisation_PV(self):
        self.UI.PVBarre_Allie = self.Equipe[0].PV_actuel
        self.UI.PVBarre_Allie = self.Pokemon_Adverse.PV_actuel
        
    
    def Tour_de_jeu(self, Choix):
        if Choix == "Fuite":
            self.UI.hide()
            self.UI.MainWindow.battle = False
        
        