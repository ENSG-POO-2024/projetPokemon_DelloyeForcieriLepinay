from abc import abstractmethod, ABCMeta
from PyQt5.QtGui import QFontDatabase, QFont

#Metaclasse permettant la création d'interface servant à transmettre des attributs utiles 
#Et à forcer la création de méthodes show et hide pour chacune d'entre elles, permettant de facilement basculer de l'une vers l'autre.
class Interface(metaclass=ABCMeta):
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        self.Jukebox = MainWindow.Jukebox
        self.Equipe = MainWindow.Equipe
        self.PC = MainWindow.PC
        self.Sprite = MainWindow.SpritePerso
        self.SpriteLegendaire = MainWindow.SpriteLegend
        id_ = QFontDatabase.addApplicationFont("./data/PokemonGb-RAeo.ttf")
        families = QFontDatabase.applicationFontFamilies(id_)
        self.font = QFont(families[0],16) # police venant du jeu Pokémon FireRed & LeafGreen
        
    @abstractmethod
    def show():
        pass
    
    @abstractmethod
    def hide():
        pass