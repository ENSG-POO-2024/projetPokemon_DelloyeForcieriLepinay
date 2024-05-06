from PyQt5 import QtCore, QtGui, QtWidgets

class InterfaceCombat:
    def __init__(self,UICombat):
        
        self.Zone_Combat = QtWidgets.QFrame(UICombat)
        self.Zone_Combat.setGeometry(QtCore.QRect(10, 10, 480, 320))
        self.Zone_Combat.setFrameShape(QtWidgets.QFrame.Box)
        self.Zone_Combat.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Zone_Combat.setObjectName("Zone_Combat")
from PyQt5 import QtCore, QtGui, QtWidgets


class InterfaceCombat(object):
    def __init__(self, UICombat):
        self.Zone_Combat = QtWidgets.QFrame(UICombat)
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
        self.Choix_Attaque = QtWidgets.QFrame(UICombat)
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
        self.BoiteDialogue = QtWidgets.QTextBrowser(UICombat)
        self.BoiteDialogue.setGeometry(QtCore.QRect(10, 340, 481, 41))
        self.BoiteDialogue.setObjectName("BoiteDialogue")

        self.retranslateUi(UICombat)

    def retranslateUi(self, UICombat):
        _translate = QtCore.QCoreApplication.translate
        self.Nom_PokeAllie.setText(_translate("UICombat", "Caratroc"))
        self.Nom_PokeEnnemi.setText(_translate("UICombat", "Caratroc"))
        self.Choix_1.setText(_translate("UICombat", "Attaque"))
        self.Choix_2.setText(_translate("UICombat", "Switch"))
        self.Choix_3.setText(_translate("UICombat", ""))
        self.Choix_4.setText(_translate("UICombat", "Fuite"))
        
    def show(self):
        self.Zone_Combat.show()
        self.Sprite_Dos.show()
        self.Sprite_Face.show()
        self.Choix_Attaque.show()
        self.Choix_1.show()
        self.Choix_2.show()
        self.Choix_3.show()
        self.Choix_4.show()
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
        self.BoiteDialogue.hide()
        
        