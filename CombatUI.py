from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtTest
from Mecaniques import *
from Interface import Interface
from PyQt5.QtMultimedia import QSound
import copy
from PyQt5.QtGui import QFontDatabase


class InterfaceCombat(Interface):
    """Interface de combat pour gérer un combat contre un pokémon sauvage"""
    def __init__(self, MainWindow,Pokemon_Sauvage):
        # Définit tous les composants de l'interface de combat (Assez indigeste) ...
        super().__init__(MainWindow)
        
        # On définit les informations relatives au combat
        self.Pokemon_Adverse = Pokemon_Sauvage
        
        # Définition de quelques booléens pour savoir dans quel menu on se situe
        self.position_fleche = "Haut","Gauche" 
        self.MenuActuel = "Choix"
        
        # Création d'une zone de combat (Sprite des pokémons + Barre de PVs + Nom des pokémons)
        self.Zone_Combat = QtWidgets.QFrame(MainWindow)
        self.Zone_Combat.setGeometry(QtCore.QRect(10, 10, 480, 320))
        self.Zone_Combat.setFrameShape(QtWidgets.QFrame.Box)
        self.Zone_Combat.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Zone_Combat.setObjectName("Zone_Combat")
        
        # Création du fond de la zone de combat 
        self.Fond_Zone = QtWidgets.QLabel(self.Zone_Combat)
        self.Fond_Zone.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.Fond_Zone.setText("")
        self.Fond_Zone.setPixmap(QtGui.QPixmap("./images/plaine.png"))
        self.Fond_Zone.setScaledContents(True)
        self.Fond_Zone.setObjectName("Fond_Zone")
        self.Fond_Zone.raise_()
        
        # On superpose sur le fond de la zone de combat les sprites de dos, face, 
        # les barres de PV de notre pokémon et celle du pokémon adverse
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
        self.PV_Ennemi.setPixmap(QtGui.QPixmap("./images/BarreEnnemie.png"))
        self.PV_Ennemi.setScaledContents(True)
        self.PV_Ennemi.setObjectName("PV_Ennemi")
        self.PV_Allie = QtWidgets.QLabel(self.Zone_Combat)
        self.PV_Allie.setGeometry(QtCore.QRect(160, 200, 315, 120))
        self.PV_Allie.setText("")
        self.PV_Allie.setPixmap(QtGui.QPixmap("./images/BarreAlliee.png"))
        self.PV_Allie.setScaledContents(True)
        self.PV_Allie.setObjectName("PV_Allie")
        self.Nom_PokeAllie = QtWidgets.QLabel(self.Zone_Combat)
        self.Nom_PokeAllie.setGeometry(QtCore.QRect(205, 217, 181, 21))
        
        # Définition de la police d'écriture
        font = self.font # police inspiré du jeu Pokémon FireRed & LeafGreen
        font.setPointSize(10) 
        font.setBold(False)
        font.setWeight(50)
        font.setLetterSpacing(1,-2) 
        
        self.Nom_PokeAllie.setFont(font)
        self.Nom_PokeAllie.setObjectName("Nom_PokeAllie")
        self.Nom_PokeEnnemi = QtWidgets.QLabel(self.Zone_Combat)
        self.Nom_PokeEnnemi.setGeometry(QtCore.QRect(30, 23, 181, 21))
        font.setPointSize(10)
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
        
        self.PV_Ennemi = QtWidgets.QLabel(self.Zone_Combat)
        self.PV_Ennemi.setGeometry(QtCore.QRect(10, 10, 300, 90))
        self.PV_Ennemi.setText("")
        self.PV_Ennemi.setPixmap(QtGui.QPixmap("./images/BarreEnnemie.png"))
        self.PV_Ennemi.setScaledContents(True)
        self.PV_Ennemi.setObjectName("PV_Ennemi")
        self.PV_Allie = QtWidgets.QLabel(self.Zone_Combat)
        self.PV_Allie.setGeometry(QtCore.QRect(160, 200, 315, 120))
        self.PV_Allie.setText("")
        self.PV_Allie.setPixmap(QtGui.QPixmap("./images/BarreAlliee.png"))
        self.PV_Allie.setScaledContents(True)
        self.PV_Allie.setObjectName("PV_Allie")
        self.Nom_PokeAllie.raise_()
        self.Nom_PokeEnnemi.raise_()
                
        #On définit un premier menu qui servira à choisir les actions ou les attaques.
        self.Choix_Attaque = QtWidgets.QFrame(MainWindow)
        self.Choix_Attaque.setGeometry(QtCore.QRect(10, 390, 480, 100))
        self.Choix_Attaque.setFrameShape(QtWidgets.QFrame.Box)
        self.Choix_Attaque.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Choix_Attaque.setObjectName("Choix_Attaque")
        font.setPointSize(10)
        self.Choix_Attaque.setFont(font)
        self.Choix_Attaque.raise_()
        
        self.Fond_Zone_3 = QtWidgets.QLabel(self.Choix_Attaque)
        self.Fond_Zone_3.setGeometry(QtCore.QRect(0, 0, 480, 100))
        self.Fond_Zone_3.setText("")
        self.Fond_Zone_3.setPixmap(QtGui.QPixmap("./images/ecran_combat_choix.png"))
        self.Fond_Zone_3.setScaledContents(True)
        self.Fond_Zone_3.setObjectName("Fond_Zone_3")
        
        self.Choix_1 = QtWidgets.QLabel(self.Choix_Attaque)
        self.Choix_1.setGeometry(QtCore.QRect(50, 0, 240, 50))
        self.Choix_1.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Choix_1.setObjectName("Choix_1")
        font.setPointSize(10)
        self.Choix_1.setFont(font)
        
        self.Choix_2 = QtWidgets.QLabel(self.Choix_Attaque)
        self.Choix_2.setGeometry(QtCore.QRect(300, 0, 240, 50))
        self.Choix_2.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Choix_2.setObjectName("Choix_2")
        font.setPointSize(10)
        self.Choix_2.setFont(font)
        
        self.Choix_3 = QtWidgets.QLabel(self.Choix_Attaque)
        self.Choix_3.setGeometry(QtCore.QRect(50, 50, 240, 50))
        self.Choix_3.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Choix_3.setObjectName("Choix_3")
        font.setPointSize(10)
        self.Choix_3.setFont(font)
        
        self.Choix_4 = QtWidgets.QLabel(self.Choix_Attaque)
        self.Choix_4.setGeometry(QtCore.QRect(300, 50, 240, 50))
        self.Choix_4.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Choix_4.setObjectName("Choix_4")
        font.setPointSize(10)
        self.Choix_4.setFont(font)
        
        self.Fleche_1 = QtWidgets.QLabel(self.Choix_Attaque)
        self.Fleche_1.setGeometry(QtCore.QRect(17, 16, 16, 20))
        self.Fleche_1.setObjectName("Fleche_1")
        self.Fleche_2 = QtWidgets.QLabel(self.Choix_Attaque)
        self.Fleche_2.setGeometry(QtCore.QRect(270, 16, 16, 20))
        self.Fleche_2.setObjectName("Fleche_2")
        self.Fleche_3 = QtWidgets.QLabel(self.Choix_Attaque)
        self.Fleche_3.setGeometry(QtCore.QRect(17, 65, 16, 20))
        self.Fleche_3.setObjectName("Fleche_3")
        self.Fleche_4 = QtWidgets.QLabel(self.Choix_Attaque)
        self.Fleche_4.setGeometry(QtCore.QRect(270, 65, 16, 20))
        self.Fleche_4.setObjectName("Fleche_4")
    
        
        #Puis une boîte de dialogue qui servira à donner des informations au joueur (Efficacité de l'attaque...etc)
        self.Fond_Zone_2 = QtWidgets.QLabel(MainWindow)
        self.Fond_Zone_2.setGeometry(QtCore.QRect(10, 330, 480, 60))
        self.Fond_Zone_2.setText("")
        self.Fond_Zone_2.setPixmap(QtGui.QPixmap("./images/ecran_combat_texte.png"))
        self.Fond_Zone_2.setScaledContents(True)
        self.Fond_Zone_2.setObjectName("Fond_Zone_2")
        
        self.BoiteDialogue = QtWidgets.QLabel(MainWindow)
        self.BoiteDialogue.setGeometry(QtCore.QRect(20, 330, 480, 60))
        self.BoiteDialogue.setObjectName("BoiteDialogue")
        font.setPointSize(10)
        self.BoiteDialogue.setFont(font)
        self.BoiteDialogue.setStyleSheet("color: white")
        
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.Nom_PokeAllie.setText(_translate("UICombat", ""))
        self.Nom_PokeEnnemi.setText(_translate("UICombat", ""))
        self.Choix_1.setText(_translate("UICombat", "Attaque"))
        self.Choix_2.setText(_translate("UICombat", "Changement"))
        self.Choix_3.setText(_translate("UICombat", "Potion"))
        self.Choix_4.setText(_translate("UICombat", "Fuite"))
        self.Fleche_1.setText(_translate("UICombat", "▶"))
        self.Fleche_2.setText(_translate("UICombat", "▶"))
        self.Fleche_3.setText(_translate("UICombat", "▶"))
        self.Fleche_4.setText(_translate("UICombat", "▶"))
    
    #Surcharge des méthodes hide et show de la méthode abstraite interface pour facilement (dés)afficher l'interface.
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
        self.Fond_Zone_2.show()
        
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
        self.Fond_Zone_2.hide()
    
    
    def deplacement_fleche_menu(self, Direction):
        """Permet de déplacer la fléche pour sélectionner un élément du menu"""
        if self.MenuActuel != "Switch":
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
    
    def valide(self,Equipe):
        """Cette fonction se lance en combat lorsque la touche espace est utilisée"""
        
        #Si on est dans le menu des choix (Attaque/Switch/Fuite)
        if self.MenuActuel == "Choix":
            #Bas droite = Fuite -> On sort du combat (On estime que cette action est garantie.)
            if self.position_fleche == ("Bas", "Droite"):
                self.hide()
                self.MainWindow.Menu = "Carte"
                self.MainWindow.map.show()
                self.Sprite.show()
                self.Jukebox.ChangeDeMusique(self.Jukebox.MusiqueDeZone)
            
            
            #Haut-Gauche = Menu d'attaque -> On réinitialise chaque choix avec le nom des attaques, s'il existe (Sinon on laisse vide)
            if self.position_fleche == ("Haut","Gauche"):
                self.Choix_1.setText("")
                self.Choix_2.setText("")
                self.Choix_3.setText("")
                self.Choix_4.setText("")
                
                try:
                    self.Choix_1.setText(Equipe.pokemons[0].Movepool[0].Nom)
                except:
                    pass
                try:
                    self.Choix_2.setText(Equipe.pokemons[0].Movepool[1].Nom)
                except:
                    pass
                try:
                    self.Choix_3.setText(Equipe.pokemons[0].Movepool[2].Nom)
                except:
                    pass
                try: 
                    self.Choix_4.setText(Equipe.pokemons[0].Movepool[3].Nom)
                except:
                    pass
                
                self.MenuActuel = "Attaque"
                return 0
            
            #Si on sélectionne l'option Changement, on affiche le menu de gestion d'équipe
            if self.position_fleche == ("Haut","Droite"):
                self.MainWindow.Menu_Gestion.Menu_Init(self, "Combat", self.Equipe)
                
            #Si on sélectionne l'option Potion, soigne 150PV au pokémon actif mais le pokémon adverse joue
            if self.position_fleche == ("Bas", "Gauche"):
                self.Equipe[0].PV_actuel += 150
                if self.Equipe[0].PV_actuel > self.Equipe[0].Stats[0]:
                    self.Equipe[0].PV_actuel = self.Equipe[0].Stats[0]
                self.actualisation_PV("Allie")
                self.BoiteDialogue.setText("Le dresseur utilise une hyper potion.")
                QtTest.QTest.qWait(2000)
                self.Tour_de_jeu(-1)
                
                
        #Si on est dans le menu attaque, on lance un Tour de jeu avec comme argument le numéro de l'attaque choisie. 
        if self.MenuActuel == "Attaque":
            if self.position_fleche == ("Haut","Gauche"):
                self.Tour_de_jeu(0)
            if self.position_fleche == ("Haut","Droite"):
                self.Tour_de_jeu(1)
            if self.position_fleche == ("Bas", "Gauche"):
                self.Tour_de_jeu(2)
            elif self.position_fleche == ("Bas","Droite"):
                self.Tour_de_jeu(3)
                
    def retour(self):
        """Cette fonction se lance lorsque qu'on appuie sur "X", elle sert essentiellement à revenir au menu précédent en cas de missclick.
        Elle sert également en fin de tour, pour revenir à l'écran de choix"""
        
        #Si on est dans le menu attaque, on revient au menu choix. 
        if self.MenuActuel == "Attaque":
            self.Choix_1.setText("Attaque")
            self.Choix_2.setText("Changement")
            self.Choix_3.setText("Potion")
            self.Choix_4.setText("Fuite")
            self.MenuActuel = "Choix"

    def Init_Combat(self,Equipe,PokeRencontre):
        
        """Cette méthode sert à initialiser un combat. On récupère l'interface et on initialise le combat avec les deux équipes qui se font face.
        L'équipe du joueur contre le Pokémon rencontré.
        
        Elle charge l'UI, les sprites des deux pokémons qui se font fassent initialement ainsi que leur PV"""
        
        self.Equipe = Equipe
        self.Pokemon_Adverse = PokeRencontre
        self.show()  
        self.Fleche_1.show()
        self.Fleche_2.hide()
        self.Fleche_3.hide()
        self.Fleche_4.hide()
        self.position_fleche = "Haut","Gauche" 
        self.Choix_1.setText("Attaque")
        self.Choix_2.setText("Changement")
        self.Choix_3.setText("Potion")
        self.Choix_4.setText("Fuite")
        self.BoiteDialogue.setText("")
        self.MenuActuel = "Choix"
        self.BoiteDialogue.setText(f"Un {self.Pokemon_Adverse.nom} sauvage apparaît !")    
        
        Pokemon1 = self.Equipe[0]
        
        self.PVBarre_Allie.setProperty("value", (Pokemon1.PV_actuel/Pokemon1.Stats[0])*100)
        self.PVBarre_Ennemi.setProperty("value", (PokeRencontre.PV_actuel/PokeRencontre.Stats[0])*100)
        
        self.Nom_PokeAllie.setText(Pokemon1.nom)
        self.Nom_PokeEnnemi.setText(self.Pokemon_Adverse.nom)
        
        Pokemon1.Sprite("Dos")
        self.Pokemon_Adverse.Sprite("Face")
        self.Sprite_Dos.setPixmap(QtGui.QPixmap("Temp/dos.png"))
        self.Sprite_Face.setPixmap(QtGui.QPixmap("Temp/face.png"))
        
        return "Combat"
            
    def actualisation_PV(self, AllieOuEnnemi):
        """Sert juste à actualiser les PVs du pokémon allié ou du pokémon ennemi et à actualiser la barre de PV en conséquence"""
        if AllieOuEnnemi == "Allie":
            self.PVBarre_Allie.setProperty("value", (self.Equipe[0].PV_actuel/self.Equipe[0].Stats[0])*100)
        else:
            self.PVBarre_Ennemi.setProperty("value", (self.Pokemon_Adverse.PV_actuel/self.Pokemon_Adverse.Stats[0])*100)
        
    
    def Tour_de_jeu(self, Num_Attaque):
        """Cette méthode sert à enclencher un tour de jeu.
        
        Elle marche comme ceci :
            - Si le Num_Attaque est strictement inférieur à 0 -> C'est un changement de pokémon. La phase se produit alors ainsi :
                - Le pokémon allié est échangé avec le pokémon (-1)*Num_Attaque.
                - Le pokémon ennemi attaque
                - On contrôle que le pokémon allié envoyé au combat n'a pas été KO à l'issue de ce changement.
                - On demande à l'utilisateur de renvoyer un autre pokémon si c'est le cas, sinon le combat suit son cours.
            
            - Si le Num_Attaque est supérieur à 0, c'est que l'utilisateur a utilisé l'attaque numéro Num_Attaque. La phase se produit alors ainsi :
                - Le pokémon le plus rapide attaque (On contrôle si KO)
                - Le pokémon le moins rapide attaque (On contrôle si KO)
                - En cas d'égalité de vitesse, le plus rapide est tiré aléatoirement"""
                
        # Pour empêcher le joueur d'effecteur des actions au milieu de la résolution du tour -> Menu Fictif
        self.MainWindow.Menu = "Dummy"
        
        #Si l'utilisateur a décidé d'attaquer
        if Num_Attaque >= 0:
            Pokemon_Allie = self.Equipe[0]
            #On compare les vitesses des deux pokémons.
            Vitesse_Allie, Vitesse_Ennemi = Pokemon_Allie.Stats[5], self.Pokemon_Adverse.Stats[5]
            
            if Vitesse_Allie > Vitesse_Ennemi:
                #Le if est là pour ne pas réaliser l'attaque ennemie si le pokémon a été mis KO
                if self.Attaque_Allie(Num_Attaque):
                    self.Attaque_Ennemie()
                
            elif Vitesse_Ennemi > Vitesse_Allie:
                #Le if est là pour ne pas réaliser l'attaque alliée si le pokémon a été mis KO
                if self.Attaque_Ennemie():
                    self.Attaque_Allie(Num_Attaque)
        
        if Num_Attaque < 0 :
            self.Attaque_Ennemie()
            
        if self.MainWindow.Menu == "Dummy":
            self.MainWindow.Menu = "Combat"
        
        
        
    def Attaque_Allie(self,Num_Attaque):
        """Réalise l'attaque d'un allié sur un ennemi.
        Return True si le combat continue, False sinon (Pour ne pas continuer inutilement le tour de jeu)"""
        
        #On calcule les dégats de l'attaque du pokemon allié sur l'adversaire
        Pokemon_Allie = self.Equipe[0]
        Attaque = Pokemon_Allie.Movepool[Num_Attaque]
        Degats, Efficacite, Critique = Attaque.Degats(Pokemon_Allie,self.Pokemon_Adverse)
        self.BoiteDialogue.setText(f"{Pokemon_Allie.nom} utilise {Attaque.Nom}.\n"+ Efficacite + " " + Critique)
        QtTest.QTest.qWait(2000)
        print(f"{Pokemon_Allie.nom} utilise {Attaque.Nom}")
        print(Degats, Efficacite)
        
        #On actualise les PVs de l'adversaire 
        self.Pokemon_Adverse.PV_actuel = self.Pokemon_Adverse.PV_actuel - Degats
        
        #Si il est mort, on le capture et le combat se termine
        if self.Pokemon_Adverse.PV_actuel < 0:
            self.Pokemon_Adverse.PV_actuel = 0
            self.actualisation_PV("Ennemi")
            self.Sprite_Face.hide()
            #On le capture s'il y a de la place dans l'équipe, on le rajoute
            if len(self.Equipe)<6:
                self.Equipe.append(copy.copy(self.Pokemon_Adverse))
                self.BoiteDialogue.setText(f"Bravo ! Vous avez capturé un {self.Pokemon_Adverse.nom} sauvage ! \nIl a été envoyé dans votre équipe.")
            #S'il n'y en a pas, on le stocke dans le PC.
            else:
                #On soigne tout pokémon envoyé au PC
                self.Pokemon_Adverse.Soin()
                #Puis on l'envoie au PC
                self.PC.append(copy.copy(self.Pokemon_Adverse))
                self.BoiteDialogue.setText(f"Bravo ! Vous avez capturé un {self.Pokemon_Adverse.nom} sauvage ! \nIl a été envoyé dans votre PC.")
            #Fin du combat
            QtTest.QTest.qWait(3000)
            self.hide()
            self.MainWindow.Menu = "Carte"
            self.MainWindow.map.show()
            self.Sprite.show()
            self.Jukebox.ChangeDeMusique(self.Jukebox.MusiqueDeZone)
            
            return False
        
        else:
            self.actualisation_PV("Ennemi")
            return True
        
    def Attaque_Ennemie(self):
        Pokemon_Allie = self.Equipe[0]
        
        #Le pokémon adverse choisit intelligemment son attaque :
        Attaques_Ennemies = self.Pokemon_Adverse.Movepool
        #On calcule quelle attaque ferait le plus de dégâts
        Liste_Dgt = [Attaques_Ennemies[i].Degats(self.Pokemon_Adverse, Pokemon_Allie) for i in range(len(Attaques_Ennemies))]
        Attq_Select = Liste_Dgt.index(max(Liste_Dgt))
        
        #On calcule les dégats de l'attaque du pokemon ennemi sur le pokemon allié
        Attaque = Attaques_Ennemies[Attq_Select]
        Degats, Efficacite, Critique = Attaque.Degats(self.Pokemon_Adverse,Pokemon_Allie)
        self.BoiteDialogue.setText(f"{self.Pokemon_Adverse.nom} utilise {Attaques_Ennemies[Attq_Select].Nom}.\n"+ Efficacite + " " + Critique)
        QtTest.QTest.qWait(2000)
        print(f"{self.Pokemon_Adverse.nom} utilise {Attaques_Ennemies[Attq_Select].Nom}.")
        print(Degats, Efficacite)
        
        #On actualise les PVs de l'adversaire 
        Pokemon_Allie.PV_actuel = Pokemon_Allie.PV_actuel - Degats
        #S'il est KO on propose le menu de sélection des Pokémons, s'ils sont tous KO -> Fin du combat
        if Pokemon_Allie.PV_actuel < 0:
            Pokemon_Allie.PV_actuel = 0
            self.actualisation_PV("Allie")
            
            #Le pokemon est KO, on doit tester s'il existe encore un membre de l'équipe encore vivant :
            if self.Equipe.All_KO():
                #GameOver
                self.BoiteDialogue.setText("Tous vos pokémons sont hors d'état de combattre ! \nVous fuyez vers le centre Pokémon le plus proche")
                QtTest.QTest.qWait(2000)
                
                #On cherche le delta avec le centre pokémon, on téléporte là-bas, et on soigne l'équipe
                X_PC, Y_PC = (87,90)
                delta_x, delta_y = X_PC - self.Sprite.x, Y_PC - self.Sprite.y
                self.MainWindow.map.Warp(delta_y, delta_x, "Center")
                self.MainWindow.Menu = "Dummy"
                self.hide()
                self.MainWindow.map.show()
                self.Equipe.Soin_All()
                self.Jukebox.ChangeDeMusique(self.Jukebox.MusiqueDeZone)
                self.MainWindow.map.Healing.play()
                self.Sprite.Changement_Sprite("./Animation/Marche/Derriere_repos.png")
                QtTest.QTest.qWait(4000)
                self.MainWindow.Menu = "Carte"
                
            else:
                #Proposition de Switch
                self.MainWindow.Menu_Gestion.Menu_Init(self, "KO_Switch", self.Equipe)
                self.MenuActuel = "Choix"
                
            return False
            
        else:
            self.actualisation_PV("Allie")
            return True
