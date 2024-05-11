from Mecaniques import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Equipe:
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
        i = self.pokemons.index(Pokemon1)
        j = self.pokemons.index(Pokemon2)
        
        P1 = self.pokemons[i]
        P2 = self.pokemons[j]
        
        self.pokemons[j] = P1
        self.pokemons[i] = P2
        
    def echange_pokemon(self,Pokemon1,Pokemon2):
        i = self.pokemons.index(Pokemon1)
        self.pokemons[i] = Pokemon2
        
    def All_KO(self):
        Bool = True
        for Pokemon in self.pokemons:
            Bool = not Pokemon.IsKO()
            if not Bool:
                break
        return Bool
    
    def __getitem__(self, items):
        return self.pokemons[items]
    
    def __iter__(self):
        return iter(self.pokemons)
    
if __name__ == '__main__':
    E = Equipe(Pokemon())
    print(E[0])