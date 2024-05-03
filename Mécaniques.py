import numpy as np
import random as rd

Type = ["Normal", "Combat", "Vol", "Poison", "Sol", "Roche", "Insecte", "Spectre", "Acier", "Feu", "Eau", "Plante", "Électrik", "Psy","Glace", "Dragon", "Ténèbres", "Fée"]

class Pokemon():
    def __init__(self,Nom,Type1, Type2, Stats, Movepool):
        self.nom = Nom
        self.Type1 = Type1
        self.Type2 = Type2
        self.Stats = Stats
        self.Movepool = Movepool


class Table_Type():
    def __init__(self):
        self.Table = np.genfromtxt("TableType.csv", delimiter=";")
    def Resistance(self,Pokemon):
        Type1, Type2 = Pokemon.Type1, Pokemon.Type2
        Index_Type1 = Type.index(Type1)
        Resistance = self.Table[:,Index_Type1]
        
        if Type2 != None:
            Index_Type2 = Type.index(Type2)
            Resistance2 = self.Table[:,Index_Type2]
            Resistance = Resistance * Resistance2
            
        return Resistance
    
class Attaque():
    def __init__(self, Nom, PhyOuSpe, Puissance, Type, Precision, Effet_Secondaire=None):
        self.Nom = Nom
        self.PhyOuSpe = PhyOuSpe
        self.Puissance = Puissance
        self.Type = Type
        self.Precision = Precision
    
    def Degats(self,Pokemon1, Pokemon2, Table):
        Pui = self.Puissance
        if rd.randint(0,100) > self.Precision:
            print("L'attaque a échoué.")
            return 0
        
        else:
            #L'attaque est-elle physique ou spéciale ?
            if self.PhyOuSpe == "Physique":
                Atq1 = Pokemon1.Stats[1]
                Def2 = Pokemon2.Stats[2]
            else:
                Atq1 = Pokemon1.Stats[3]
                Def2 = Pokemon2.Stats[4]
        
            CM = 1
            #Gestion du Same Type Attack Bonus (STAB)
            if self.Type == Pokemon1.Type1 or self.Type == Pokemon2.Type2:
                CM = CM*1.5
                
            #Gestion des faiblesses
            Index_Type_Attaque = Type.index(self.Type)
            Multiplicateur = Table.Resistance(Pokemon2)[Index_Type_Attaque]
            
            if Multiplicateur == 0:
                print("Ça n'a pas d'effet.")
            elif Multiplicateur > 1:
                print("C'est super efficace.")
            elif Multiplicateur < 1:
                print("Ce n'est pas très efficace.")
                
            CM = CM*Multiplicateur
            
            #Gestion des coups critiques
            if rd.randint(1,16) == 16:
                print("Coup critique")
                CM = CM*1.5
            
            print(Atq1, Def2)
            Degats = (42*(Atq1/Def2)*Pui/50 + 2)
            
            return int(Degats*CM)
        
      
if __name__ == "__main__":
    Bulbizarre = Pokemon("Bulbizarre","Plante","Poison",[364,263,265,299,299,259], ["Tranch'Herbe", "Bomb'Beurk", "Charge"])
    Carapuce = Pokemon("Carapuce","Eau", None, [292,175,229,218,227,185], ["Pistolet à Ô", "Charge"])
    Fantominus = Pokemon("Fantominus","Spectre", "Poison", [282,190,224,194,222,180], ["Ball'Ombre", "Charge"])
    Table = Table_Type()
    
    TH = Attaque("Tranch'Herbe", "Physique", 80, "Plante", 100)
    Ch = Attaque("Charge", "Physique", 40, "Normal", 100)
    
    print(TH.Degats(Bulbizarre, Carapuce, Table))
