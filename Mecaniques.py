import numpy as np
import random as rd
from PIL import Image

Type = ["Normal", "Combat", "Vol", "Poison", "Sol", "Roche", "Insecte", "Spectre", "Acier", "Feu", "Eau", "Plante", "Électrik", "Psy","Glace", "Dragon", "Ténèbres", "Fée"]


class Pokemon():
    def __init__(self,ID=0,Nom="MissingNo",Type1="", Type2="", Base_Stats=[33,136,0,1,1,29], Movepool=[]):
        #Le Movepool est une liste d'objets de classe Attaque
        self.ID = ID
        self.nom = Nom
        self.Type1 = Type1
        self.Type2 = Type2
        self.Stats = [2*Base_Stats[0]+31+252/4+5+100] + [2*Base_Stats[i]+31+252/4+5 for i in range(1,6,1)]
        self.Movepool = Movepool
        self.PV_actuel = self.Stats[0]
        self.legendaire = False
    
    def IsKO(self):
        #Vérifie si ce pokémon est KO
        return self.PV_actuel<=0
    
    def FromID(self, new_ID):
        #Règle toutes les informations d'un pokémon à partir de son ID
        dex = Pokedex()
        info = dex.pokedex[new_ID-1]
        self.ID = int(info[0])
        self.nom = info[1]
        self.Type1 = info[2]
        self.Type2 = info[3]
        self.Stats[0]=2*int(info[5])+31+252/4+5+100   #PV
        self.Stats[1]=2*int(info[6])+31+252/4+5       #Att
        self.Stats[2]=2*int(info[7])+31+252/4+5       #Def
        self.Stats[3]=2*int(info[8])+31+252/4+5       #Att Sp
        self.Stats[4]=2*int(info[9])+31+252/4+5       #Def Sp
        self.Stats[5]=2*int(info[10])+31+252/4+5      #Vitesse
        self.Movepool = []
        self.Movepool.append(info[13])                  #Move type 1
        self.Movepool.append(info[14])                  #Move normal
        if info[15] != "":
            self.Movepool.append(info[15])              #Move type 2 (si existe)
        self.PV_actuel = self.Stats[0]
        self.legendaire = (info[12] == "True")
        
    def Sprite(self, Direction):
        
        im = Image.open("./images/Sprite_Opacity.png")
        ID = self.ID-1
        left = 1 + 161*(ID//3)
        top = 1 + 65*(ID%3)
        right = left + 160
        bottom = top + 64
        poke = im.crop((left, top, right, bottom))
        face = poke.crop((0, 0, 64, 64))
        dos = poke.crop((64, 0, 128, 64))
        mini = poke.crop((128,0,160,32))
        if Direction == "Face":
            face.save('./Temp/face.png', 'png')
        elif Direction == "Dos":
            dos.save('./Temp/dos.png', 'png')
        else:
            Path = f'./Temp/mini{self.ID}.png'
            mini.save(f'./Temp/mini{self.ID}.png', "png")
            return Path
            
    def Soin(self):
        self.PV_actuel = self.Stats[0]

class Pokedex():
    def __init__(self):
        #Import du tableau
        self.pokedex = np.genfromtxt("./data/pokemon_1ere_gen.csv", delimiter=',', dtype=str, skip_header=1, encoding='latin1')
        #Initialisation de la future colonne movepool
        lon = len(self.pokedex)
        movepool=[[] for i in range(lon)]
        #Remplissage de la future colonne movepool
        for i in range(lon):
            pokemon = self.pokedex[i]
            #type 1
            type1 = pokemon[2]
            att = int(pokemon[6])
            attsp = int(pokemon[8])
            if att > attsp:
                movepool[i].append(Attaque(f"{type1} Physique", "Physique", 80, type1, 100))
            elif att <= attsp:
                movepool[i].append(Attaque(f"{type1} Spécial", "Speciale", 80, type1, 100))
            #attaque normale
            movepool[i].append(Attaque("Charge", "Physique", 80, "Normal", 100))
            #type 2
            if pokemon[3] != "":
                type2 = pokemon[3]
                if att > attsp:
                    movepool[i].append(Attaque(f"{type2} Physique", "Physique", 80, type2, 100))
                elif att <= attsp:
                    movepool[i].append(Attaque(f"{type2} Spécial", "Speciale", 80, type2, 100))
            else:
                movepool[i].append('')
        Move_Col = np.array(movepool)
        self.pokedex = np.append(self.pokedex, Move_Col, axis=1)
            



class ZoneRencontre():
    def __init__(self, ID_Zone):
        self.ID = ID_Zone
        if ID_Zone==4:
            self.nom_zone="Plaine"
            self.Liste_Poke=[16 for i in range(9)] + [17 for i in range(3)]+ [18]
            self.Liste_Poke+=[19 for i in range(9)] + [20 for i in range(3)]
            self.Liste_Poke+=[21 for i in range(9)] + [22 for i in range(3)]
            self.Liste_Poke+=[39 for i in range(9)] + [40 for i in range(3)]
            self.Liste_Poke+=[63 for i in range(9)] + [64 for i in range(3)]+[65]
            self.Liste_Poke+=[84 for i in range(9)] + [85 for i in range(3)]
            self.Liste_Poke+=[83]
            self.Liste_Poke+=[143]
            self.Liste_Poke+=[128]
        elif ID_Zone==6:
            self.nom_zone="Grotte"
            self.Liste_Poke=[29 for i in range(9)] + [30 for i in range(3)]+ [31]
            self.Liste_Poke+=[32 for i in range(9)] + [33 for i in range(3)]+[34]
            self.Liste_Poke+=[35 for i in range(9)] + [36 for i in range(3)]
            self.Liste_Poke+=[41 for i in range(9)] + [42 for i in range(3)]
            self.Liste_Poke+=[46 for i in range(9)] + [47 for i in range(3)]
            self.Liste_Poke+=[50 for i in range(9)] + [51 for i in range(3)]
            self.Liste_Poke+=[66 for i in range(9)] + [67 for i in range(3)]+[68]
            self.Liste_Poke+=[74 for i in range(9)] + [75 for i in range(3)]+[76]
            self.Liste_Poke+=[95]
        elif ID_Zone==8:
            self.nom_zone="Ville"
            self.Liste_Poke=[100 for i in range(9)] + [101 for i in range(3)]
            self.Liste_Poke+=[106] + [107] + [132]
            self.Liste_Poke+=[133 for i in range(3)] + [135] + [137]
            self.Liste_Poke+=[88 for i in range(9)] + [89 for i in range(3)]
            self.Liste_Poke+=[81 for i in range(9)] + [82 for i in range(3)]
            self.Liste_Poke+=[52 for i in range(9)] + [53 for i in range(3)]
            self.Liste_Poke+=[122] + [124]
            self.Liste_Poke+=[92 for i in range(9)] + [93 for i in range(3)]+[94]
            self.Liste_Poke+=[125]
        elif ID_Zone==51:
            self.nom_zone="Lac"
            self.Liste_Poke=[7, 7, 7] + [8, 8]+ [9]
            self.Liste_Poke+=[54 for i in range(9)] + [55 for i in range(3)]
            self.Liste_Poke+=[60 for i in range(9)] + [61 for i in range(3)]+[62]
            self.Liste_Poke+=[54 for i in range(9)] + [55 for i in range(3)]
            self.Liste_Poke+=[79 for i in range(9)] + [80 for i in range(3)]
            self.Liste_Poke+=[118 for i in range(9)] + [119 for i in range(3)]
            self.Liste_Poke+=[129 for i in range(10)] + [130 for i in range(3)]+[134]
            self.Liste_Poke+=[147 for i in range(3)] + [148 for i in range(2)]+[149]
        elif ID_Zone==52:
            self.nom_zone="Océan"
            self.Liste_Poke=[86 for i in range(9)] + [87 for i in range(3)]
            self.Liste_Poke+=[72 for i in range(9)] + [73 for i in range(3)]
            self.Liste_Poke+=[120 for i in range(9)] + [121 for i in range(3)]
            self.Liste_Poke+=[131]
            self.Liste_Poke+=[90 for i in range(9)] + [91 for i in range(3)]
            self.Liste_Poke+=[116 for i in range(9)] + [117 for i in range(3)]
            self.Liste_Poke+=[98 for i in range(9)] + [99 for i in range(3)]
            self.Liste_Poke+=[140 for i in range(3)] + [141]
            self.Liste_Poke+=[138 for i in range(3)] + [139]
        elif ID_Zone==7:
            self.nom_zone="Désert"
            self.Liste_Poke=[4, 4, 4] + [5, 5] + [6]
            self.Liste_Poke+=[27 for i in range(9)] + [28 for i in range(3)]
            self.Liste_Poke+=[37 for i in range(9)] + [38 for i in range(3)]
            self.Liste_Poke+=[58 for i in range(9)] + [59 for i in range(3)]
            self.Liste_Poke+=[77 for i in range(9)] + [78 for i in range(3)]
            self.Liste_Poke+=[104 for i in range(9)] + [105 for i in range(3)]+[115]
            self.Liste_Poke+=[109 for i in range(9)] + [110 for i in range(3)]
            self.Liste_Poke+=[111 for i in range(9)] + [112 for i in range(3)]
            self.Liste_Poke+=[27 for i in range(9)] + [28 for i in range(3)]
            self.Liste_Poke+=[126]+[136]+[142]
        elif ID_Zone==2:
            self.nom_zone="Forêt"
            self.Liste_Poke=[10 for i in range(9)] + [11 for i in range(3)]+[12]
            self.Liste_Poke+=[13 for i in range(9)] + [14 for i in range(3)]+[15]
            self.Liste_Poke+=[25 for i in range(3)] + [26]
            self.Liste_Poke+=[48 for i in range(9)] + [49 for i in range(3)]
            self.Liste_Poke+=[114]+[123]+[127]
        elif ID_Zone==3:
            self.nom_zone="Jungle"
            self.Liste_Poke=[1,1,1] + [2,2] + [3]
            self.Liste_Poke+=[69 for i in range(9)] + [70 for i in range(3)]+[71]
            self.Liste_Poke+=[102 for i in range(9)] + [103 for i in range(3)]
            self.Liste_Poke+=[113]+[108]
            self.Liste_Poke+=[23 for i in range(9)] + [24 for i in range(3)]
            self.Liste_Poke+=[43 for i in range(9)] + [44 for i in range(3)]+[45]
            self.Liste_Poke+=[56 for i in range(9)] + [57 for i in range(3)]
            
        
    def Random_Poke(self):
        #Retourne un objet de type pokémon aléatoirement
        Wild_Poke = Pokemon()
        Wild_Poke.FromID(rd.choice(self.Liste_Poke))
        return Wild_Poke
            

class Table_Type():
    def __init__(self):
        self.Table = np.genfromtxt("./data/TableType.csv", delimiter=";")
    def Resistance(self,Pokemon):
        Type1, Type2 = Pokemon.Type1, Pokemon.Type2
        Index_Type1 = Type.index(Type1)
        Resistance = self.Table[:,Index_Type1]
        
        if Type2 != "":
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
        self.Table = Table_Type()
    
    def Degats(self,Pokemon1, Pokemon2):
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
            Multiplicateur = self.Table.Resistance(Pokemon2)[Index_Type_Attaque]
            Efficace = None
            
            if Multiplicateur == 0:
                Efficace = "Ça n'a pas d'effet."
            elif Multiplicateur > 1:
                Efficace = "C'est super efficace !"
            elif Multiplicateur < 1:
                Efficace = "Ce n'est pas très efficace..."
            else:
                Efficace = ""
                
            CM = CM*Multiplicateur
            
            Critique = ""
            #Gestion des coups critiques
            if rd.randint(1,16) == 16:
                Critique = "Coup critique !"
                CM = CM*1.5
                
            
            Degats = (42*(Atq1/Def2)*Pui/50 + 2)
            
            return int(Degats*CM), Efficace, Critique
        
      
if __name__ == "__main__":
    Bulbizarre = Pokemon(1,"Bulbizarre","Plante","Poison",[364,263,265,299,299,259], ["Tranch'Herbe", "Bomb'Beurk", "Charge"])
    Carapuce = Pokemon(4,"Carapuce","Eau", "", [292,175,229,218,227,185], ["Pistolet à Ô", "Charge"])
    Fantominus = Pokemon(12,"Fantominus","Spectre", "Poison", [282,190,224,194,222,180], ["Ball'Ombre", "Charge"])
    Table = Table_Type()
    
    TH = Attaque("Tranch'Herbe", "Physique", 80, "Plante", 100)
    Ch = Attaque("Charge", "Physique", 40, "Normal", 100)
    
    print(TH.Degats(Bulbizarre, Carapuce)[0])
    
    R = ZoneRencontre(2)
    P_rand=R.Random_Poke()
    print(P_rand.nom)
    print(P_rand.Movepool[0].Nom)
    
    
    P1 = Pokemon()
    P1.FromID(1)
    print(P1.nom)
    print(P1.Movepool[0].Nom)
    print(P1.legendaire)
    Pokedex_A = Pokedex()
    print(Pokedex_A.pokedex[120][13].Nom)
    
    Carapuce.Sprite("mini")