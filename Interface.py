from abc import abstractmethod, ABCMeta

#Metaclasse permettant la création d'interface servant à transmettre des attributs utiles 
#Et à forcer la création de méthodes show et hide pour chacune d'entre elles, permettant de facilement basculer de l'une vers l'autre.
class Interface(metaclass=ABCMeta):
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        self.Jukebox = MainWindow.Jukebox
        self.Equipe = MainWindow.Equipe
        self.PC = MainWindow.PC
        self.Sprite = MainWindow.SpritePerso
        
    @abstractmethod
    def show():
        pass
    
    @abstractmethod
    def hide():
        pass