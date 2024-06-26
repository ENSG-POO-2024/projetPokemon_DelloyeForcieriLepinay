from Mecaniques import *

class Equipe:
    """Définit ce qu'est une équipe (Une liste de 6 pokémons)"""
    def __init__(self,Pokemon_1,Pokemon_2=None,Pokemon_3=None,Pokemon_4=None,Pokemon_5=None, Pokemon_6=None):
        self.pokemons = [Pokemon_1]
        if Pokemon_2 != None:
            self.pokemons.append(Pokemon_2)
        if Pokemon_3 != None:
            self.pokemons.append(Pokemon_3)
        if Pokemon_4 != None:
            self.pokemons.append(Pokemon_4)
        if Pokemon_5 != None:
            self.pokemons.append(Pokemon_5)
        if Pokemon_6 != None:
            self.pokemons.append(Pokemon_6)
            
        self.Pokemon_Lead = self.pokemons[0]
              
    def permutation(self,Pokemon1,Pokemon2):
        """Sert à permuter deux pokémons dans l'équipe"""
        i = self.pokemons.index(Pokemon1)
        j = self.pokemons.index(Pokemon2)
        
        P1 = self.pokemons[i]
        P2 = self.pokemons[j]
        
        self.pokemons[j] = P1
        self.pokemons[i] = P2
        
    def echange_pokemon(self,Pokemon1,Pokemon2):
        """Permet de substituer le pokémon2 au pokémon1"""
        i = self.pokemons.index(Pokemon1)
        self.pokemons[i] = Pokemon2
    
    def append(self,Pokemon):
        """Permet de rajouter un pokémon dans l'équipe"""
        self.pokemons.append(Pokemon)
        
    def All_KO(self):
        """Méthode qui sert à vérifier si tous les pokémons sont KO (Pour fin de combat notamment)"""
        Bool = True
        for Pokemon in self.pokemons:
            Bool = Pokemon.IsKO()
            if not Bool:
                break
        return Bool
    
    def Soin_All(self):
        """Permet de soigner facilement tous les pokémons d'une équipe"""
        for Pokemon in self:
            Pokemon.Soin()
    
    """Surcharge de méthodes pour plus de confort dans le code"""
    def __getitem__(self, items):
        return self.pokemons[items]
    
    def __setitem__(self, index, valeur):
        self.pokemons[index] = valeur
    
    def __iter__(self):
        return iter(self.pokemons)
    
    def __len__(self):
        return len(self.pokemons)

    def remove(self,value):
        self.pokemons.remove(value)
    
class PC:
    """Définit ce qu'est un PC (basiquement une liste de pokémon)"""
    def __init__(self,Liste_Pokemon_PC=[]):
        self.Boite = Liste_Pokemon_PC
    
    """Surcharge de méthodes pour plus de confort dans le code"""
    def append(self,Pokemon):
        self.Boite.append(Pokemon)
        
    def __getitem__(self, item):
        return self.Boite[item]
    
    def __setitem__(self, index, valeur):
        self.Boite[index] = valeur
        
    def remove(self,value):
        self.Boite.remove(value)
    
if __name__ == '__main__':
    E = Equipe(Pokemon())
    print(E[0])