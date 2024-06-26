# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Interface import Interface

class Menu_PC(Interface):
    """Gère l'interface du PC"""
    
    # Création des différents objets de l'interface.
    def __init__(self, MainWindow):
        super().__init__(MainWindow)
        self.MenuEquipe = QtWidgets.QListWidget(MainWindow)
        self.MenuEquipe.setGeometry(QtCore.QRect(10, 10, 181, 471))
        self.MenuEquipe.setObjectName("MenuEquipe")
        self.MenuPC = QtWidgets.QListWidget(MainWindow)
        self.MenuPC.setGeometry(QtCore.QRect(320, 10, 171, 471))
        self.MenuPC.setObjectName("MenuPC")
        self.Ajouter = QtWidgets.QPushButton(MainWindow)
        self.Ajouter.setGeometry(QtCore.QRect(210, 170, 89, 25))
        self.Ajouter.setObjectName("Ajouter")
        self.Deposer = QtWidgets.QPushButton(MainWindow)
        self.Deposer.setGeometry(QtCore.QRect(210, 220, 89, 25))
        self.Deposer.setObjectName("Deposer")
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.Ajouter.clicked.connect(self.Ajout)
        self.Deposer.clicked.connect(self.Depot)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.Ajouter.setText(_translate("PyQTmon", "Ajouter"))
        self.Deposer.setText(_translate("PyQTmon", "Déposer"))
        
        # Définition de la police d'écriture
        font = self.font # police inspiré du jeu Pokémon FireRed & LeafGreen
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setLetterSpacing(1,-3)
        self.Ajouter.setFont(font)
        self.Deposer.setFont(font)
        
    def Init_PC(self):
        # Initialise le PC avec l'équipe du joueur et les pokémons de son PC.
        self.MenuEquipe.clear()
        self.MenuPC.clear()
        for Pokemon in self.Equipe:
            item = QtWidgets.QListWidgetItem()
            font = self.font
            font.setPointSize(10)
            font.setBold(False)
            item.setFont(font)
            icon = QtGui.QIcon()
            Path_Mini = Pokemon.Sprite("mini")
            icon.addPixmap(QtGui.QPixmap(Path_Mini), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            _translate = QtCore.QCoreApplication.translate
            item.setText(_translate("PyQTmon", f"{Pokemon.nom}"))
            self.MenuEquipe.addItem(item)
        for Pokemon in self.PC:
            item = QtWidgets.QListWidgetItem()
            font = self.font
            font.setPointSize(8)
            item.setFont(font)
            icon = QtGui.QIcon()
            Path_Mini = Pokemon.Sprite("mini")
            icon.addPixmap(QtGui.QPixmap(Path_Mini), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            _translate = QtCore.QCoreApplication.translate
            item.setText(_translate("PyQTmon", f"{Pokemon.nom}"))
            self.MenuPC.addItem(item)
            
        self.show()
        
    def Ajout(self):
        # S'il n'y a qu'un pokemon sélectioné dans le PC et que l'équipe n'est 
        # pas pleine. On l'ajoute à notre équipe.
        if len(self.MenuPC.selectedItems()) == 1 and len(self.Equipe)<6:
            Index = self.MenuPC.currentRow()
            self.Equipe.append(self.PC[Index])
            self.PC.remove(self.PC[Index])
            self.Init_PC()
    
    def Depot(self):
        # Si on a plus d'un pokémon, on peut le dépose, il est alors ajouté au 
        # PC, et soigné au passage.
        if len(self.MenuEquipe.selectedItems()) and len(self.Equipe)>1:
            Index = self.MenuEquipe.currentRow()
            self.Equipe[Index].Soin()
            self.PC.append(self.Equipe[Index])
            self.Equipe.remove(self.Equipe[Index])
            self.Init_PC()
    
    # Surcharge des méthodes hide et show de la méthode abstraite interface pour 
    # facilement (dés)afficher l'interface.
    def hide(self):
        self.MenuEquipe.hide()
        self.MenuPC.hide()
        self.Ajouter.hide()
        self.Deposer.hide()
        
    def show(self):
        self.MenuEquipe.show()
        self.MenuPC.show()
        self.Ajouter.show()
        self.Deposer.show()