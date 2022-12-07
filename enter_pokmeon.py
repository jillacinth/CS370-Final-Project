import pandas as pd

class Check_Pokemon:
    def __init__(self, pokemon, data):
        self.pokemon = pokemon
        self.data = data

    def loadstats(self, name):
        id_num = self.data.index(name)
        hp = self.data['HP']


