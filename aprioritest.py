import numpy as np
import pandas as pd
#from mlxtend.frequent_patterns import apriori, association_rules
from apyori import apriori

#file for debugging the apriori algorithm
pokemon_list = pd.read_csv(r'pokemon.csv')
pokemon_teams = pd.read_csv(r'pokemon_teams.csv')

names = pokemon_list['Name'].tolist()
hp = pokemon_list['HP'].tolist()
at = pokemon_list['Attack'].tolist()
defe = pokemon_list['Defense'].tolist()
spAt = pokemon_list['Sp. Atk'].tolist()
spDef = pokemon_list['Sp. Def'].tolist()
sd = pokemon_list['Speed'].tolist()

entries = pokemon_teams['Entry'].tolist()
pokemon1 = pokemon_teams['Pokemon1'].tolist()
pokemon2 = pokemon_teams['Pokemon2'].tolist()
pokemon3 = pokemon_teams['Pokemon3'].tolist()
pokemon4 = pokemon_teams['Pokemon4'].tolist()
pokemon5 = pokemon_teams['Pokemon5'].tolist()
pokemon6 = pokemon_teams['Pokemon6'].tolist()

unique_pokemon = pd.unique(pokemon_teams[['Pokemon1','Pokemon2','Pokemon3','Pokemon4','Pokemon5','Pokemon6']].values.ravel('K'))

# putting output into a pandas dataframe
def inspect(output):
    lhs         = [tuple(result[2][0][0])[0] for result in output]
    rhs         = [tuple(result[2][0][1])[0] for result in output]
    support    = [result[1] for result in output]
    confidence = [result[2][0][2] for result in output]
    lift       = [result[2][0][3] for result in output]
    return list(zip(lhs, rhs, support, confidence, lift))

pokemon_values_1_2 = []

for i in range(0, len(entries)):
    #pokemon_values_1_2.append([str(pokemon1[i]), str(pokemon2[i])])
    pokemon_values_1_2.append([str(pokemon_teams.values[i,j]) for j in range(1, 7)])
    #print([pokemon1[i], pokemon2[i]])

#print(pokemon_values_1_2)

rule1 = apriori(transactions= pokemon_values_1_2, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 100)
#print(rule1)

output1 = list(rule1) # returns a non-tabular output

#print(output1)
output_DataFrame1 = pd.DataFrame(inspect(output1), columns = ['Left_Hand_Side', 'Right_Hand_Side', 'Support', 'Confidence', 'Lift'])

#print(output_DataFrame1)
print(output_DataFrame1.sort_values(by=['Support'],ascending=False))

