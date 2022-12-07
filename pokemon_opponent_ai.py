import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

pokemon_list = pd.read_csv('pokemon.csv')
pokemon_teams = pd.read_csv('pokemon_teams.csv')
#print(pokemon_teams.head())


#print(pokemon_teams.columns)

unique_pokemon = pd.unique(pokemon_teams[['Pokemon1','Pokemon2','Pokemon3','Pokemon4','Pokemon5','Pokemon6']].values.ravel('K'))

#print(unique_pokemon)

pokemon_teams['Pokemon1','Pokemon2','Pokemon3','Pokemon4','Pokemon5','Pokemon6'] = pokemon_teams['Pokemon1','Pokemon2','Pokemon3','Pokemon4','Pokemon5','Pokemon6'].str.strip()
