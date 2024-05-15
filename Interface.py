from abc import abstractmethod, ABCMeta

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