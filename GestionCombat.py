from Mecaniques import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Equipe:
    def __init__(self,Pokemon_1,Pokemon_2=None,Pokemon_3=None,Pokemon_4=None,Pokemon_5=None, Pokemon_6=None):
        self.pokemons = [Pokemon_1]
        Pokemon_1.allie = True
        if Pokemon_2 != None:
            self.pokemons.append(Pokemon_2)
            Pokemon_2.allie = True
        if Pokemon_3 != None:
            self.pokemons.append(Pokemon_3)
            Pokemon_3.allie = True
        if Pokemon_4 != None:
            self.pokemons.append(Pokemon_4)
            Pokemon_4.allie = True
        if Pokemon_5 != None:
            self.pokemons.append(Pokemon_5)
            Pokemon_5.allie = True
        if Pokemon_6 != None:
            self.pokemons.append(Pokemon_6)
            Pokemon_6.allie = True
            
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
        