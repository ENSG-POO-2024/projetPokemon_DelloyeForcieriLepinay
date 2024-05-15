from PyQt5.QtMultimedia import QSound

class Jukebox():
    def __init__(self, MusicPath):
        #Sert à se rappeler dans quelle zone on était avant un combat par exemple. 
        self.MusiqueDeZone = "./Son/Route1.wav"
        
        #Joue la première musique
        self.Musique = QSound(MusicPath)
        self.Musique.setLoops(100000)
        self.Musique.play()
    
    def ChangeDeMusique(self,MusicPath):
        self.Musique.stop()
        self.Musique = QSound(MusicPath)
        self.Musique.setLoops(100000)
        self.Musique.play()