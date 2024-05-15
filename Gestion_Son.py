from PyQt5.QtMultimedia import QSound

class Jukebox():
    def __init__(self, MusicPath):
        self.Musique = QSound(MusicPath)
        self.Musique.setLoops(1000)
        self.Musique.play()
    
    def ChangeDeMusique(self,MusicPath):
        self.Musique.stop()
        self.Musique = QSound(MusicPath)
        self.Musique.setLoops(1000)
        self.Musique.play()
        
    def JoueBruitage(self,BruitagePath):
        Bruitage = QSound(BruitagePath)
        return Bruitage