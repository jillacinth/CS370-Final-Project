import numpy as np
import pandas as pd
#from mlxtend.frequent_patterns import apriori, association_rules
from apyori import apriori

pokemon_list = pd.read_csv(r'pokemon.csv')
pokemon_teams = pd.read_csv(r'pokemon_teams.csv')

unique_pokemon = pd.unique(pokemon_teams[['Pokemon1','Pokemon2','Pokemon3','Pokemon4','Pokemon5','Pokemon6']].values.ravel('K'))
entry_list = pokemon_teams['Entry'].tolist()
pokemon_values = []
for i in range(0, len(entry_list)):
    pokemon_values.append([str(pokemon_teams.values[i, j]) for j in range(1,6)])

rule = apriori(transactions= pokemon_values, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)

output = list(rule) # returns a non-tabular output
# putting output into a pandas dataframe
def inspect(output):
    lhs         = [tuple(result[2][0][0])[0] for result in output]
    rhs         = [tuple(result[2][0][1])[0] for result in output]
    support    = [result[1] for result in output]
    confidence = [result[2][0][2] for result in output]
    lift       = [result[2][0][3] for result in output]
    return list(zip(lhs, rhs, support, confidence, lift))
output_DataFrame = pd.DataFrame(inspect(output), columns = ['Left_Hand_Side', 'Right_Hand_Side', 'Support', 'Confidence', 'Lift'])

print(output_DataFrame.nlargest(n = 10, columns= 'Lift'))

