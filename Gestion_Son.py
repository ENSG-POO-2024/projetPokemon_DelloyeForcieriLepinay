from PyQt5.QtMultimedia import QSound

class Jukebox():
    def __init__(self, MusicPath):
        self.Musique = QSound(MusicPath)
        self.Musique.setLoops(100000)
        self.Musique.play()
    
    def ChangeDeMusique(self,MusicPath):
        self.Musique.stop()
        self.Musique = QSound(MusicPath)
        self.Musique.setLoops(100000)
        self.Musique.play()