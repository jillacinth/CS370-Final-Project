import numpy as np
import pandas as pd
#from mlxtend.frequent_patterns import apriori, association_rules
from apyori import apriori

pokemon_list = pd.read_csv(r'pokemon.csv')
pokemon_teams = pd.read_csv(r'pokemon_teams.csv')

names = pokemon_list['Name'].tolist()
hp = pokemon_list['HP'].tolist()
at = pokemon_list['Attack'].tolist()
defe = pokemon_list['Defense'].tolist()
spAt = pokemon_list['Sp. Atk'].tolist()
spDef = pokemon_list['Sp. Def'].tolist()
sd = pokemon_list['Speed'].tolist()

av_hp = (sum(hp))/1190
av_at = (sum(at))/1190
av_def = (sum(defe))/1190
av_spAt = (sum(spAt))/1190
av_spDef = (sum(spDef))/1190
av_sd = (sum(sd))/1190
#av_score = (sum(hp)+sum(at)+sum(defe)+sum(spAt)+sum(spDef)+sum(sd))/1190

unique_pokemon = pd.unique(pokemon_teams[['Pokemon1','Pokemon2','Pokemon3','Pokemon4','Pokemon5','Pokemon6']].values.ravel('K'))

entries = pokemon_teams['Entry'].tolist()
pokemon1 = pokemon_teams['Pokemon1'].tolist()
pokemon2 = pokemon_teams['Pokemon2'].tolist()
pokemon3 = pokemon_teams['Pokemon3'].tolist()
pokemon4 = pokemon_teams['Pokemon4'].tolist()
pokemon5 = pokemon_teams['Pokemon5'].tolist()
pokemon6 = pokemon_teams['Pokemon6'].tolist()

pokemon_values = []
for i in range(0, 50):
    pokemon_values.append([str(pokemon_teams.values[i,j]) for j in range(1, 7)])

rule = apriori(transactions= pokemon_values, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 100)

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
left_side_pk = output_DataFrame['Left_Hand_Side'].tolist()
right_side_pk = output_DataFrame['Right_Hand_Side'].tolist()
support_pk = output_DataFrame['Support'].tolist()
confid_pk = output_DataFrame['Confidence'].tolist()
lift_pk = output_DataFrame['Lift'].tolist()

def expect_partner(opponent):
    possible_partners = []

    for i in range(0,len(left_side_pk)):
        if left_side_pk[i] == opponent:
            if right_side_pk[i] not in possible_partners:
                possible_partners.append(right_side_pk[i])
        if right_side_pk[i] == opponent:
            if left_side_pk[i] not in possible_partners:
                possible_partners.append(left_side_pk[i])
    return possible_partners

def find_opponent(pokemon1):
    advantage_index = 0
    highest_adv = 0

    for pokemon2 in unique_pokemon:
        temp_adv = 0
        type_compare(pokemon1, pokemon2, temp_adv)
        stats_compare(pokemon1, pokemon2, temp_adv)
        if temp_adv > highest_adv:
            advantage_index = unique_pokemon.index(pokemon2)
            highest_adv = temp_adv
    
    return unique_pokemon[advantage_index]

def find_your_teammates(team):
    possible_team = []
    for pokemon in team:
        if find_opponent(pokemon) not in possible_team:
            possible_team.append(find_opponent(pokemon))
    return possible_team


def stats_compare(pokemon1, pokemon2, advantage_index):
    pokemon_index1 = names.index(pokemon1)
    pokemon_index2 = names.index(pokemon2)

    if at[pokemon_index1] < av_at:
        if defe[pokemon_index2] > av_def:
            advantage_index += 1
    elif defe[pokemon_index1] < av_def:
        if at[pokemon_index2] > av_at:
            advantage_index += 1
    elif spAt[pokemon_index1] < av_spAt:
        if spDef[pokemon_index2] > av_spDef:
            advantage_index += 1
    elif spDef[pokemon_index1] < av_spDef:
        if spAt[pokemon_index2] > av_spAt:
            advantage_index += 1


def type_compare(pokemon1, pokemon2, advantage_index):
    pokemon_index1 = names.index(pokemon1)
    pokemon_index2 = names.index(pokemon2)

    pk_type1 = pokemon_list['Type1'].tolist()
    pk_type2 = pokemon_list['Type2'].tolist()

    #if normal type
    if pk_type1[pokemon_index1] =='Normal' or pk_type2[pokemon_index1]=='Normal':
        if pk_type1[pokemon_index2]=='Fighting' or pk_type2[pokemon_index2]=='Fighting':
            if pk_type1[pokemon_index1] != 'Psychic' or pk_type2[pokemon_index1]!= 'Psychic' or pk_type1[pokemon_index1] != 'Flying' or pk_type2[pokemon_index1]!= 'Flying' or pk_type1[pokemon_index1] != 'Fairy' or pk_type2[pokemon_index1]!= 'Fairy':
                advantage_index += 1
    #if fighting type
    if pk_type1[pokemon_index1] =='Fighting' or pk_type2[pokemon_index1]=='Fighting':
        if pk_type1[pokemon_index2]=='Flying' or pk_type2[pokemon_index2]=='Flying':
            if pk_type1[pokemon_index1] != 'Rock' or pk_type2[pokemon_index1]!= 'Rock' or pk_type1[pokemon_index1] != 'Electric' or pk_type2[pokemon_index1]!= 'Electric' or pk_type1[pokemon_index1] != 'Ice' or pk_type2[pokemon_index1]!= 'Ice':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Psychic' or pk_type2[pokemon_index2]=='Psychic':
            if pk_type1[pokemon_index1] != 'Bug' or pk_type2[pokemon_index1]!= 'Bug' or pk_type1[pokemon_index1] != 'Ghost' or pk_type2[pokemon_index1]!= 'Ghost' or pk_type1[pokemon_index1] != 'Dark' or pk_type2[pokemon_index1]!= 'Dark':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Fairy' or pk_type2[pokemon_index2]=='Fairy':
            if pk_type1[pokemon_index1] != 'Poison' or pk_type2[pokemon_index1]!= 'Poison' or pk_type1[pokemon_index1] != 'Steel' or pk_type2[pokemon_index1]!= 'Steel':
                advantage_index += 1
    #if flying type
    if pk_type1[pokemon_index1] =='Flying' or pk_type2[pokemon_index1]=='Flying':
        if pk_type1[pokemon_index2]=='Rock' or pk_type2[pokemon_index2]=='Rock':
            if pk_type1[pokemon_index1] != 'Fighting' or pk_type2[pokemon_index1]!= 'Fighting' or pk_type1[pokemon_index1] != 'Ground' or pk_type2[pokemon_index1]!= 'Ground' or pk_type1[pokemon_index1] != 'Steel' or pk_type2[pokemon_index1]!= 'Steel' or pk_type1[pokemon_index1] != 'Water' or pk_type2[pokemon_index1]!= 'Water' or pk_type1[pokemon_index1] != 'Grass' or pk_type2[pokemon_index1]!= 'Grass':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Ice' or pk_type2[pokemon_index2]=='Ice':
            if pk_type1[pokemon_index1] != 'Fighting' or pk_type2[pokemon_index1]!= 'Fighting' or pk_type1[pokemon_index1] != 'Rock' or pk_type2[pokemon_index1]!= 'Rock' or pk_type1[pokemon_index1] != 'Steel' or pk_type2[pokemon_index1]!= 'Steel' or pk_type1[pokemon_index1] != 'Fire' or pk_type2[pokemon_index1]!= 'Fire':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Electric' or pk_type2[pokemon_index2]=='Electric':
            if pk_type1[pokemon_index1] != 'Ground' or pk_type2[pokemon_index1]!= 'Ground':
                advantage_index += 1
    #if Poison Type
    if pk_type1[pokemon_index1] =='Poison' or pk_type2[pokemon_index1]=='Poison':
        if pk_type1[pokemon_index2]=='Ground' or pk_type2[pokemon_index2]=='Ground':
            if pk_type1[pokemon_index1] != 'Ice' or pk_type2[pokemon_index1]!= 'Ice' or pk_type1[pokemon_index1] != 'Water' or pk_type2[pokemon_index1]!= 'Water' or pk_type1[pokemon_index1] != 'Grass' or pk_type2[pokemon_index1]!= 'Grass':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Psychic' or pk_type2[pokemon_index2]=='Psychic':
            if pk_type1[pokemon_index1] != 'Bug' or pk_type2[pokemon_index1]!= 'Bug' or pk_type1[pokemon_index1] != 'Ghost' or pk_type2[pokemon_index1]!= 'Ghost' or pk_type1[pokemon_index1] != 'Dark' or pk_type2[pokemon_index1]!= 'Dark':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Steel' or pk_type2[pokemon_index2]=='Steel':
            if pk_type1[pokemon_index1] != 'Fighting' or pk_type2[pokemon_index1]!= 'Fighting' or pk_type1[pokemon_index1] != 'Ground' or pk_type2[pokemon_index1]!= 'Ground' or pk_type1[pokemon_index1] != 'Fire' or pk_type2[pokemon_index1]!= 'Fire':
                advantage_index += 1
    #if ground type
    if pk_type1[pokemon_index1] =='Ground' or pk_type2[pokemon_index1]=='Ground':
        if pk_type1[pokemon_index2]=='Water' or pk_type2[pokemon_index2]=='Water':
            if pk_type1[pokemon_index1] != 'Electric' or pk_type2[pokemon_index1]!= 'Electric' or pk_type1[pokemon_index1] != 'Water' or pk_type2[pokemon_index1]!= 'Water' or pk_type1[pokemon_index1] != 'Grass' or pk_type2[pokemon_index1]!= 'Grass':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Grass' or pk_type2[pokemon_index2]=='Grass':
            if pk_type1[pokemon_index1] != 'Bug' or pk_type2[pokemon_index1]!= 'Bug' or pk_type1[pokemon_index1] != 'Ice' or pk_type2[pokemon_index1]!= 'Ice' or pk_type1[pokemon_index1] != 'Flying' or pk_type2[pokemon_index1]!= 'Flying' or pk_type1[pokemon_index1] != 'Poison' or pk_type2[pokemon_index1]!= 'Poison'or pk_type1[pokemon_index1] != 'Grass' or pk_type2[pokemon_index1]!= 'Grass' or pk_type1[pokemon_index1] != 'Fire' or pk_type2[pokemon_index1]!= 'Fire':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Ice' or pk_type2[pokemon_index2]=='Ice':
            if pk_type1[pokemon_index1] != 'Fighting' or pk_type2[pokemon_index1]!= 'Fighting' or pk_type1[pokemon_index1] != 'Rock' or pk_type2[pokemon_index1]!= 'Rock' or pk_type1[pokemon_index1] != 'Steel' or pk_type2[pokemon_index1]!= 'Steel' or pk_type1[pokemon_index1] != 'Fire' or pk_type2[pokemon_index1]!= 'Fire':
                advantage_index += 1
    #if rock type
    if pk_type1[pokemon_index1] =='Rock' or pk_type2[pokemon_index1]=='Rock':
        if pk_type1[pokemon_index2]=='Water' or pk_type2[pokemon_index2]=='Water':
            if pk_type1[pokemon_index1] != 'Electric' or pk_type2[pokemon_index1]!= 'Electric' or pk_type1[pokemon_index1] != 'Water' or pk_type2[pokemon_index1]!= 'Water' or pk_type1[pokemon_index1] != 'Grass' or pk_type2[pokemon_index1]!= 'Grass':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Grass' or pk_type2[pokemon_index2]=='Grass':
            if pk_type1[pokemon_index1] != 'Bug' or pk_type2[pokemon_index1]!= 'Bug' or pk_type1[pokemon_index1] != 'Ice' or pk_type2[pokemon_index1]!= 'Ice' or pk_type1[pokemon_index1] != 'Flying' or pk_type2[pokemon_index1]!= 'Flying' or pk_type1[pokemon_index1] != 'Poison' or pk_type2[pokemon_index1]!= 'Poison'or pk_type1[pokemon_index1] != 'Grass' or pk_type2[pokemon_index1]!= 'Grass' or pk_type1[pokemon_index1] != 'Fire' or pk_type2[pokemon_index1]!= 'Fire':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Fighting' or pk_type2[pokemon_index2]=='Fighting':
            if pk_type1[pokemon_index1] != 'Psychic' or pk_type2[pokemon_index1]!= 'Psychic' or pk_type1[pokemon_index1] != 'Flying' or pk_type2[pokemon_index1]!= 'Flying' or pk_type1[pokemon_index1] != 'Fairy' or pk_type2[pokemon_index1]!= 'Fairy':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Ground' or pk_type2[pokemon_index2]=='Ground':
            if pk_type1[pokemon_index1] != 'Ice' or pk_type2[pokemon_index1]!= 'Ice' or pk_type1[pokemon_index1] != 'Water' or pk_type2[pokemon_index1]!= 'Water' or pk_type1[pokemon_index1] != 'Grass' or pk_type2[pokemon_index1]!= 'Grass':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Steel' or pk_type2[pokemon_index2]=='Steel':
            if pk_type1[pokemon_index1] != 'Fighting' or pk_type2[pokemon_index1]!= 'Fighting' or pk_type1[pokemon_index1] != 'Ground' or pk_type2[pokemon_index1]!= 'Ground' or pk_type1[pokemon_index1] != 'Fire' or pk_type2[pokemon_index1]!= 'Fire':
                advantage_index += 1
    #if bug type
    if pk_type1[pokemon_index1] =='Bug' or pk_type2[pokemon_index1]=='Bug':
        if pk_type1[pokemon_index2]=='Flying' or pk_type2[pokemon_index2]=='Flying':
            if pk_type1[pokemon_index1] != 'Rock' or pk_type2[pokemon_index1]!= 'Rock' or pk_type1[pokemon_index1] != 'Electric' or pk_type2[pokemon_index1]!= 'Electric' or pk_type1[pokemon_index1] != 'Ice' or pk_type2[pokemon_index1]!= 'Ice':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Rock' or pk_type2[pokemon_index2]=='Rock':
            if pk_type1[pokemon_index1] != 'Fighting' or pk_type2[pokemon_index1]!= 'Fighting' or pk_type1[pokemon_index1] != 'Ground' or pk_type2[pokemon_index1]!= 'Ground' or pk_type1[pokemon_index1] != 'Steel' or pk_type2[pokemon_index1]!= 'Steel' or pk_type1[pokemon_index1] != 'Water' or pk_type2[pokemon_index1]!= 'Water' or pk_type1[pokemon_index1] != 'Grass' or pk_type2[pokemon_index1]!= 'Grass':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Fire' or pk_type2[pokemon_index2]=='Fire':
            if pk_type1[pokemon_index1] != 'Rock' or pk_type2[pokemon_index1]!= 'Rock' or pk_type1[pokemon_index1] != 'Ground' or pk_type1[pokemon_index1] != 'Water' or pk_type2[pokemon_index1]!= 'Water' or pk_type1[pokemon_index1] != 'Grass' or pk_type2[pokemon_index1]!= 'Grass':
                advantage_index += 1
    #if ghost type
    if pk_type1[pokemon_index1] =='Ghost' or pk_type2[pokemon_index1]=='Ghost':
        if pk_type1[pokemon_index2]=='Ghost' or pk_type2[pokemon_index2]=='Ghost':
            if pk_type1[pokemon_index1] != 'Dark' or pk_type2[pokemon_index1]!= 'Dark':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Dark' or pk_type2[pokemon_index2]=='Dark':
            if pk_type1[pokemon_index1] != 'Fighting' or pk_type2[pokemon_index1]!= 'Fighting' or pk_type1[pokemon_index1] != 'Bug' or pk_type2[pokemon_index1]!= 'Bug' or pk_type1[pokemon_index1] != 'Fairy' or pk_type2[pokemon_index1]!= 'Fairy':
                advantage_index += 1
    #if steel type
    if pk_type1[pokemon_index1] =='Steel' or pk_type2[pokemon_index1]=='Steel':
        if pk_type1[pokemon_index2]=='Fighting' or pk_type2[pokemon_index2]=='Fighting':
            if pk_type1[pokemon_index1] != 'Psychic' or pk_type2[pokemon_index1]!= 'Psychic' or pk_type1[pokemon_index1] != 'Flying' or pk_type2[pokemon_index1]!= 'Flying' or pk_type1[pokemon_index1] != 'Fairy' or pk_type2[pokemon_index1]!= 'Fairy':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Ground' or pk_type2[pokemon_index2]=='Ground':
            if pk_type1[pokemon_index1] != 'Ice' or pk_type2[pokemon_index1]!= 'Ice' or pk_type1[pokemon_index1] != 'Water' or pk_type2[pokemon_index1]!= 'Water' or pk_type1[pokemon_index1] != 'Grass' or pk_type2[pokemon_index1]!= 'Grass':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Fire' or pk_type2[pokemon_index2]=='Fire':
            if pk_type1[pokemon_index1] != 'Rock' or pk_type2[pokemon_index1]!= 'Rock' or pk_type1[pokemon_index1] != 'Ground' or pk_type1[pokemon_index1] != 'Water' or pk_type2[pokemon_index1]!= 'Water' or pk_type1[pokemon_index1] != 'Grass' or pk_type2[pokemon_index1]!= 'Grass':
                advantage_index += 1
    #if fire type
    if pk_type1[pokemon_index1] =='Fire' or pk_type2[pokemon_index1]=='Fire':
        if pk_type1[pokemon_index2]=='Ground' or pk_type2[pokemon_index2]=='Ground':
            if pk_type1[pokemon_index1] != 'Ice' or pk_type2[pokemon_index1]!= 'Ice' or pk_type1[pokemon_index1] != 'Water' or pk_type2[pokemon_index1]!= 'Water' or pk_type1[pokemon_index1] != 'Grass' or pk_type2[pokemon_index1]!= 'Grass':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Rock' or pk_type2[pokemon_index2]=='Rock':
            if pk_type1[pokemon_index1] != 'Fighting' or pk_type2[pokemon_index1]!= 'Fighting' or pk_type1[pokemon_index1] != 'Ground' or pk_type2[pokemon_index1]!= 'Ground' or pk_type1[pokemon_index1] != 'Steel' or pk_type2[pokemon_index1]!= 'Steel' or pk_type1[pokemon_index1] != 'Water' or pk_type2[pokemon_index1]!= 'Water' or pk_type1[pokemon_index1] != 'Grass' or pk_type2[pokemon_index1]!= 'Grass':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Water' or pk_type2[pokemon_index2]=='Water':
            if pk_type1[pokemon_index1] != 'Electric' or pk_type2[pokemon_index1]!= 'Electric' or pk_type1[pokemon_index1] != 'Water' or pk_type2[pokemon_index1]!= 'Water' or pk_type1[pokemon_index1] != 'Grass' or pk_type2[pokemon_index1]!= 'Grass':
                advantage_index += 1
    #if water type
    if pk_type1[pokemon_index1] =='Water' or pk_type2[pokemon_index1]=='Water':
        if pk_type1[pokemon_index2]=='Grass' or pk_type2[pokemon_index2]=='Grass':
            if pk_type1[pokemon_index1] != 'Bug' or pk_type2[pokemon_index1]!= 'Bug' or pk_type1[pokemon_index1] != 'Ice' or pk_type2[pokemon_index1]!= 'Ice' or pk_type1[pokemon_index1] != 'Flying' or pk_type2[pokemon_index1]!= 'Flying' or pk_type1[pokemon_index1] != 'Poison' or pk_type2[pokemon_index1]!= 'Poison'or pk_type1[pokemon_index1] != 'Grass' or pk_type2[pokemon_index1]!= 'Grass' or pk_type1[pokemon_index1] != 'Fire' or pk_type2[pokemon_index1]!= 'Fire':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Electric' or pk_type2[pokemon_index2]=='Electric':
            if pk_type1[pokemon_index1] != 'Ground' or pk_type2[pokemon_index1]!= 'Ground':
                advantage_index += 1
    #if grass type
    if pk_type1[pokemon_index1] =='Grass' or pk_type2[pokemon_index1]=='Grass':
        if pk_type1[pokemon_index2]=='Fire' or pk_type2[pokemon_index2]=='Fire':
            if pk_type1[pokemon_index1] != 'Rock' or pk_type2[pokemon_index1]!= 'Rock' or pk_type1[pokemon_index1] != 'Ground' or pk_type1[pokemon_index1] != 'Water' or pk_type2[pokemon_index1]!= 'Water' or pk_type1[pokemon_index1] != 'Grass' or pk_type2[pokemon_index1]!= 'Grass':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Ice' or pk_type2[pokemon_index2]=='Ice':
            if pk_type1[pokemon_index1] != 'Fighting' or pk_type2[pokemon_index1]!= 'Fighting' or pk_type1[pokemon_index1] != 'Rock' or pk_type2[pokemon_index1]!= 'Rock' or pk_type1[pokemon_index1] != 'Steel' or pk_type2[pokemon_index1]!= 'Steel' or pk_type1[pokemon_index1] != 'Fire' or pk_type2[pokemon_index1]!= 'Fire':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Flying' or pk_type2[pokemon_index2]=='Flying':
            if pk_type1[pokemon_index1] != 'Rock' or pk_type2[pokemon_index1]!= 'Rock' or pk_type1[pokemon_index1] != 'Electric' or pk_type2[pokemon_index1]!= 'Electric' or pk_type1[pokemon_index1] != 'Ice' or pk_type2[pokemon_index1]!= 'Ice':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Poison' or pk_type2[pokemon_index2]=='Poison':
            if pk_type1[pokemon_index1] != 'Ground' or pk_type2[pokemon_index1]!= 'Ground' or pk_type1[pokemon_index1] != 'Psychic' or pk_type2[pokemon_index1]!= 'Psychic':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Bug' or pk_type2[pokemon_index2]=='Bug':
            if pk_type1[pokemon_index1] != 'Rock' or pk_type2[pokemon_index1]!= 'Rock' or pk_type1[pokemon_index1] != 'Fire' or pk_type2[pokemon_index1]!= 'Fire' or pk_type1[pokemon_index1] != 'Flying' or pk_type2[pokemon_index1]!= 'Flying':
                advantage_index += 1
    #if Electric type
    if pk_type1[pokemon_index1] =='Electric' or pk_type2[pokemon_index1] =='Electric':
        if pk_type1[pokemon_index2]=='Ground' or pk_type2[pokemon_index2]=='Ground':
            if pk_type1[pokemon_index1] != 'Ice' or pk_type2[pokemon_index1]!= 'Ice' or pk_type1[pokemon_index1] != 'Water' or pk_type2[pokemon_index1]!= 'Water' or pk_type1[pokemon_index1] != 'Grass' or pk_type2[pokemon_index1]!= 'Grass':
                advantage_index += 1
    #if Psychic type
    if pk_type1[pokemon_index1] =='Psychic' or pk_type2[pokemon_index1] =='Psychic':
        if pk_type1[pokemon_index2]=='Bug' or pk_type2[pokemon_index2]=='Bug':
            if pk_type1[pokemon_index1] != 'Rock' or pk_type2[pokemon_index1]!= 'Rock' or pk_type1[pokemon_index1] != 'Fire' or pk_type2[pokemon_index1]!= 'Fire' or pk_type1[pokemon_index1] != 'Flying' or pk_type2[pokemon_index1]!= 'Flying':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Ghost' or pk_type2[pokemon_index2]=='Ghost':
            if pk_type1[pokemon_index1] != 'Dark' or pk_type2[pokemon_index1]!= 'Dark':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Dark' or pk_type2[pokemon_index2]=='Dark':
            if pk_type1[pokemon_index1] != 'Fighting' or pk_type2[pokemon_index1]!= 'Fighting' or pk_type1[pokemon_index1] != 'Bug' or pk_type2[pokemon_index1]!= 'Bug' or pk_type1[pokemon_index1] != 'Fairy' or pk_type2[pokemon_index1]!= 'Fairy':
                advantage_index += 1
    #if ice type
    if pk_type1[pokemon_index1] =='Ice' or pk_type2[pokemon_index1] =='Ice':
        if pk_type1[pokemon_index2]=='Fire' or pk_type2[pokemon_index2]=='Fire':
            if pk_type1[pokemon_index1] != 'Rock' or pk_type2[pokemon_index1]!= 'Rock' or pk_type1[pokemon_index1] != 'Ground' or pk_type1[pokemon_index1] != 'Water' or pk_type2[pokemon_index1]!= 'Water' or pk_type1[pokemon_index1] != 'Grass' or pk_type2[pokemon_index1]!= 'Grass':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Rock' or pk_type2[pokemon_index2]=='Rock':
            if pk_type1[pokemon_index1] != 'Fighting' or pk_type2[pokemon_index1]!= 'Fighting' or pk_type1[pokemon_index1] != 'Ground' or pk_type2[pokemon_index1]!= 'Ground' or pk_type1[pokemon_index1] != 'Steel' or pk_type2[pokemon_index1]!= 'Steel' or pk_type1[pokemon_index1] != 'Water' or pk_type2[pokemon_index1]!= 'Water' or pk_type1[pokemon_index1] != 'Grass' or pk_type2[pokemon_index1]!= 'Grass':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Fighting' or pk_type2[pokemon_index2]=='Fighting':
            if pk_type1[pokemon_index1] != 'Psychic' or pk_type2[pokemon_index1]!= 'Psychic' or pk_type1[pokemon_index1] != 'Flying' or pk_type2[pokemon_index1]!= 'Flying' or pk_type1[pokemon_index1] != 'Fairy' or pk_type2[pokemon_index1]!= 'Fairy':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Steel' or pk_type2[pokemon_index2]=='Steel':
            if pk_type1[pokemon_index1] != 'Fighting' or pk_type2[pokemon_index1]!= 'Fighting' or pk_type1[pokemon_index1] != 'Ground' or pk_type2[pokemon_index1]!= 'Ground' or pk_type1[pokemon_index1] != 'Fire' or pk_type2[pokemon_index1]!= 'Fire':
                advantage_index += 1
    #if dragon type
    if pk_type1[pokemon_index1] =='Dragon' or pk_type2[pokemon_index1] =='Dragon':
        if pk_type1[pokemon_index2]=='Dragon' or pk_type2[pokemon_index2]=='Dragon':
            if pk_type1[pokemon_index1] != 'Ice' or pk_type2[pokemon_index1]!= 'Ice' or pk_type1[pokemon_index1] != 'Fairy' or pk_type2[pokemon_index1]!= 'Fairy':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Ice' or pk_type2[pokemon_index2]=='Ice':
            if pk_type1[pokemon_index1] != 'Fighting' or pk_type2[pokemon_index1]!= 'Fighting' or pk_type1[pokemon_index1] != 'Rock' or pk_type2[pokemon_index1]!= 'Rock' or pk_type1[pokemon_index1] != 'Steel' or pk_type2[pokemon_index1]!= 'Steel' or pk_type1[pokemon_index1] != 'Fire' or pk_type2[pokemon_index1]!= 'Fire':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Fairy' or pk_type2[pokemon_index2]=='Fairy':
            if pk_type1[pokemon_index1] != 'Poison' or pk_type2[pokemon_index1]!= 'Poison' or pk_type1[pokemon_index1] != 'Steel' or pk_type2[pokemon_index1]!= 'Steel':
                advantage_index += 1
    #if Dark Type
    if pk_type1[pokemon_index1] =='Dark' or pk_type2[pokemon_index1] =='Dark':
        if pk_type1[pokemon_index2]=='Fairy' or pk_type2[pokemon_index2]=='Fairy':
            if pk_type1[pokemon_index1] != 'Poison' or pk_type2[pokemon_index1]!= 'Poison' or pk_type1[pokemon_index1] != 'Steel' or pk_type2[pokemon_index1]!= 'Steel':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Fighting' or pk_type2[pokemon_index2]=='Fighting':
            if pk_type1[pokemon_index1] != 'Psychic' or pk_type2[pokemon_index1]!= 'Psychic' or pk_type1[pokemon_index1] != 'Flying' or pk_type2[pokemon_index1]!= 'Flying' or pk_type1[pokemon_index1] != 'Fairy' or pk_type2[pokemon_index1]!= 'Fairy':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Bug' or pk_type2[pokemon_index2]=='Bug':
            if pk_type1[pokemon_index1] != 'Rock' or pk_type2[pokemon_index1]!= 'Rock' or pk_type1[pokemon_index1] != 'Fire' or pk_type2[pokemon_index1]!= 'Fire' or pk_type1[pokemon_index1] != 'Flying' or pk_type2[pokemon_index1]!= 'Flying':
                advantage_index += 1
    #if fairy type
    if pk_type1[pokemon_index1] =='Fairy' or pk_type2[pokemon_index1] =='Fairy':
        if pk_type1[pokemon_index2]=='Steel' or pk_type2[pokemon_index2]=='Steel':
            if pk_type1[pokemon_index1] != 'Fighting' or pk_type2[pokemon_index1]!= 'Fighting' or pk_type1[pokemon_index1] != 'Ground' or pk_type2[pokemon_index1]!= 'Ground' or pk_type1[pokemon_index1] != 'Fire' or pk_type2[pokemon_index1]!= 'Fire':
                advantage_index += 1
        if pk_type1[pokemon_index2]=='Steel' or pk_type2[pokemon_index2]=='Steel':
            if pk_type1[pokemon_index1] != 'Fighting' or pk_type2[pokemon_index1]!= 'Fighting' or pk_type1[pokemon_index1] != 'Ground' or pk_type2[pokemon_index1]!= 'Ground' or pk_type1[pokemon_index1] != 'Fire' or pk_type2[pokemon_index1]!= 'Fire':
                advantage_index += 1


your_pokemon = str(input("Enter what Pokemon you'd like to use: "))
print("Your best opponent would be a " + find_opponent(your_pokemon) + ", which is likely to be paired with the following \n" + str(expect_partner(find_opponent(your_pokemon))))
print("You should pick from the following to combat these Pokemon: \n" + str(find_your_teammates(expect_partner(find_opponent(your_pokemon)))))
