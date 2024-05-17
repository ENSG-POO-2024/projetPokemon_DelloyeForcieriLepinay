# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'intro.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Interface import Interface


class Intro(Interface):
    """Interface d'intro où on montre le professeur Chen qui nous présente nos pokémons de départ.
    Basiquement c'est une image."""
    def __init__(self, MainWindow):
        super().__init__(MainWindow)
        
        self.Professeur = QtWidgets.QLabel(MainWindow)
        self.Professeur.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.Professeur.setText("")
        self.Professeur.setPixmap(QtGui.QPixmap("images/Professeur2.png"))
        self.Professeur.setScaledContents(True)
        self.Professeur.setObjectName("Professeur")
        
        self.Text_box = QtWidgets.QLabel(MainWindow)
        self.Text_box.setGeometry(QtCore.QRect(20, 380, 460, 84))
        self.Text_box.setText("")
        self.Text_box.setPixmap(QtGui.QPixmap("images/Text_box.png"))
        self.Text_box.setScaledContents(False)
        self.Text_box.setObjectName("Text_box")
        
        self.Salameche = QtWidgets.QLabel(MainWindow)
        self.Salameche.setGeometry(QtCore.QRect(218, 300, 64, 64))
        self.Salameche.setText("")
        self.Salameche.setPixmap(QtGui.QPixmap("images/faceS.png"))
        self.Salameche.setObjectName("Salameche")
        self.Bulbizarre = QtWidgets.QLabel(MainWindow)
        self.Bulbizarre.setGeometry(QtCore.QRect(100, 300, 64, 64))
        self.Bulbizarre.setText("")
        self.Bulbizarre.setPixmap(QtGui.QPixmap("images/faceB.png"))
        self.Bulbizarre.setObjectName("Bulbizarre")
        
        self.Carapuce = QtWidgets.QLabel(MainWindow)
        self.Carapuce.setGeometry(QtCore.QRect(336, 300, 64, 64))
        self.Carapuce.setText("")
        self.Carapuce.setPixmap(QtGui.QPixmap("images/faceC.png"))
        self.Carapuce.setObjectName("Carapuce")
        
        self.Parole = QtWidgets.QLabel(MainWindow)
        self.Parole.setGeometry(QtCore.QRect(30, 380, 460, 84))
        self.Parole.setText(" Bien le bonjour !\n Voici tes trois premiers POKÉMON !")
        font = self.font
        font.setPointSize(8)
        self.Parole.setFont(font)
        self.Parole.setObjectName("Soin_PC_texte")
    
    #Surcharge des méthodes hide et show de la méthode abstraite interface pour facilement (dés)afficher l'interface.
    def show(self):
        self.Professeur.show()
        self.Text_box.show()
        self.Salameche.show()
        self.Bulbizarre.show()
        self.Carapuce.show()
        self.Parole.show()
        
    def hide(self):
        #On cache tout et on affiche la carte
        self.Professeur.hide()
        self.Text_box.hide()
        self.Salameche.hide()
        self.Bulbizarre.hide()
        self.Carapuce.hide()
        self.Parole.hide()
        self.MainWindow.Menu = "Carte"
        self.MainWindow.map.show()