import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

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

#print(pokemon_teams.columns)

unique_pokemon = pd.unique(pokemon_teams[['Pokemon1','Pokemon2','Pokemon3','Pokemon4','Pokemon5','Pokemon6']].values.ravel('K'))

#print(unique_pokemon)

pokemon_teams['Pokemon1','Pokemon2','Pokemon3','Pokemon4','Pokemon5','Pokemon6'] = pokemon_teams['Pokemon1','Pokemon2','Pokemon3','Pokemon4','Pokemon5','Pokemon6'].str.strip()

def find_opponent(pokemon, pokemon_list)



def type_compare(pokemon1, pokemon2, pokemon_list, advantageIndex):
    pokemon_index1 = pokemon_list['Name'].index(pokemon1)
    pokemon_index2 = pokemon_list['Name'].index(pokemon2)

    pk_type1 = pokemon_list['Type1'].tolist()
    pk_type2 = pokemon_list['Type2'].tolist()


    #if normal type
    if pk_type1[pokemon_index1] is 'Normal' or pk_type2[pokemon_index1]is 'Normal':
        if pk_type1[pokemon_index2]is 'Fighting' or pk_type2[pokemon_index2]is 'Fighting':
            if pk_type1[pokemon_index1] is not 'Psychic' or pk_type2[pokemon_index1]is not 'Psychic' or pk_type1[pokemon_index1] is not 'Flying' or pk_type2[pokemon_index1]is not 'Flying' or pk_type1[pokemon_index1] is not 'Fairy' or pk_type2[pokemon_index1]is not 'Fairy':
                advantageIndex += 1
    #if fighting type
    if pk_type1[pokemon_index1] is 'Fighting' or pk_type2[pokemon_index1]is 'Fighting':
        if pk_type1[pokemon_index2]is 'Flying' or pk_type2[pokemon_index2]is 'Flying':
            if pk_type1[pokemon_index1] is not 'Rock' or pk_type2[pokemon_index1]is not 'Rock' or pk_type1[pokemon_index1] is not 'Electric' or pk_type2[pokemon_index1]is not 'Electric' or pk_type1[pokemon_index1] is not 'Ice' or pk_type2[pokemon_index1]is not 'Ice':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Psychic' or pk_type2[pokemon_index2]is 'Psychic':
            if pk_type1[pokemon_index1] is not 'Bug' or pk_type2[pokemon_index1]is not 'Bug' or pk_type1[pokemon_index1] is not 'Ghost' or pk_type2[pokemon_index1]is not 'Ghost' or pk_type1[pokemon_index1] is not 'Dark' or pk_type2[pokemon_index1]is not 'Dark':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Fairy' or pk_type2[pokemon_index2]is 'Fairy':
            if pk_type1[pokemon_index1] is not 'Poison' or pk_type2[pokemon_index1]is not 'Poison' or pk_type1[pokemon_index1] is not 'Steel' or pk_type2[pokemon_index1]is not 'Steel':
                advantageIndex += 1
    #if flying type
    if pk_type1[pokemon_index1] is 'Flying' or pk_type2[pokemon_index1]is 'Flying':
        if pk_type1[pokemon_index2]is 'Rock' or pk_type2[pokemon_index2]is 'Rock':
            if pk_type1[pokemon_index1] is not 'Fighting' or pk_type2[pokemon_index1]is not 'Fighting' or pk_type1[pokemon_index1] is not 'Ground' or pk_type2[pokemon_index1]is not 'Ground' or pk_type1[pokemon_index1] is not 'Steel' or pk_type2[pokemon_index1]is not 'Steel' or pk_type1[pokemon_index1] is not 'Water' or pk_type2[pokemon_index1]is not 'Water' or pk_type1[pokemon_index1] is not 'Grass' or pk_type2[pokemon_index1]is not 'Grass':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Ice' or pk_type2[pokemon_index2]is 'Ice':
            if pk_type1[pokemon_index1] is not 'Fighting' or pk_type2[pokemon_index1]is not 'Fighting' or pk_type1[pokemon_index1] is not 'Rock' or pk_type2[pokemon_index1]is not 'Rock' or pk_type1[pokemon_index1] is not 'Steel' or pk_type2[pokemon_index1]is not 'Steel' or pk_type1[pokemon_index1] is not 'Fire' or pk_type2[pokemon_index1]is not 'Fire':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Electric' or pk_type2[pokemon_index2]is 'Electric':
            if pk_type1[pokemon_index1] is not 'Ground' or pk_type2[pokemon_index1]is not 'Ground':
                advantageIndex += 1
    #if Poison Type
    if pk_type1[pokemon_index1] is 'Poison' or pk_type2[pokemon_index1]is 'Poison':
        if pk_type1[pokemon_index2]is 'Ground' or pk_type2[pokemon_index2]is 'Ground':
            if pk_type1[pokemon_index1] is not 'Ice' or pk_type2[pokemon_index1]is not 'Ice' or pk_type1[pokemon_index1] is not 'Water' or pk_type2[pokemon_index1]is not 'Water' or pk_type1[pokemon_index1] is not 'Grass' or pk_type2[pokemon_index1]is not 'Grass':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Psychic' or pk_type2[pokemon_index2]is 'Psychic':
            if pk_type1[pokemon_index1] is not 'Bug' or pk_type2[pokemon_index1]is not 'Bug' or pk_type1[pokemon_index1] is not 'Ghost' or pk_type2[pokemon_index1]is not 'Ghost' or pk_type1[pokemon_index1] is not 'Dark' or pk_type2[pokemon_index1]is not 'Dark':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Steel' or pk_type2[pokemon_index2]is 'Steel':
            if pk_type1[pokemon_index1] is not 'Fighting' or pk_type2[pokemon_index1]is not 'Fighting' or pk_type1[pokemon_index1] is not 'Ground' or pk_type2[pokemon_index1]is not 'Ground' or pk_type1[pokemon_index1] is not 'Fire' or pk_type2[pokemon_index1]is not 'Fire':
                advantageIndex += 1
    #if ground type
    if pk_type1[pokemon_index1] is 'Ground' or pk_type2[pokemon_index1]is 'Ground':
        if pk_type1[pokemon_index2]is 'Water' or pk_type2[pokemon_index2]is 'Water':
            if pk_type1[pokemon_index1] is not 'Electric' or pk_type2[pokemon_index1]is not 'Electric' or pk_type1[pokemon_index1] is not 'Water' or pk_type2[pokemon_index1]is not 'Water' or pk_type1[pokemon_index1] is not 'Grass' or pk_type2[pokemon_index1]is not 'Grass':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Grass' or pk_type2[pokemon_index2]is 'Grass':
            if pk_type1[pokemon_index1] is not 'Bug' or pk_type2[pokemon_index1]is not 'Bug' or pk_type1[pokemon_index1] is not 'Ice' or pk_type2[pokemon_index1]is not 'Ice' or pk_type1[pokemon_index1] is not 'Flying' or pk_type2[pokemon_index1]is not 'Flying' or pk_type1[pokemon_index1] is not 'Poison' or pk_type2[pokemon_index1]is not 'Poison'or pk_type1[pokemon_index1] is not 'Grass' or pk_type2[pokemon_index1]is not 'Grass' or pk_type1[pokemon_index1] is not 'Fire' or pk_type2[pokemon_index1]is not 'Fire':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Ice' or pk_type2[pokemon_index2]is 'Ice':
            if pk_type1[pokemon_index1] is not 'Fighting' or pk_type2[pokemon_index1]is not 'Fighting' or pk_type1[pokemon_index1] is not 'Rock' or pk_type2[pokemon_index1]is not 'Rock' or pk_type1[pokemon_index1] is not 'Steel' or pk_type2[pokemon_index1]is not 'Steel' or pk_type1[pokemon_index1] is not 'Fire' or pk_type2[pokemon_index1]is not 'Fire':
                advantageIndex += 1
    #if rock type
    if pk_type1[pokemon_index1] is 'Rock' or pk_type2[pokemon_index1]is 'Rock':
        if pk_type1[pokemon_index2]is 'Water' or pk_type2[pokemon_index2]is 'Water':
            if pk_type1[pokemon_index1] is not 'Electric' or pk_type2[pokemon_index1]is not 'Electric' or pk_type1[pokemon_index1] is not 'Water' or pk_type2[pokemon_index1]is not 'Water' or pk_type1[pokemon_index1] is not 'Grass' or pk_type2[pokemon_index1]is not 'Grass':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Grass' or pk_type2[pokemon_index2]is 'Grass':
            if pk_type1[pokemon_index1] is not 'Bug' or pk_type2[pokemon_index1]is not 'Bug' or pk_type1[pokemon_index1] is not 'Ice' or pk_type2[pokemon_index1]is not 'Ice' or pk_type1[pokemon_index1] is not 'Flying' or pk_type2[pokemon_index1]is not 'Flying' or pk_type1[pokemon_index1] is not 'Poison' or pk_type2[pokemon_index1]is not 'Poison'or pk_type1[pokemon_index1] is not 'Grass' or pk_type2[pokemon_index1]is not 'Grass' or pk_type1[pokemon_index1] is not 'Fire' or pk_type2[pokemon_index1]is not 'Fire':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Fighting' or pk_type2[pokemon_index2]is 'Fighting':
            if pk_type1[pokemon_index1] is not 'Psychic' or pk_type2[pokemon_index1]is not 'Psychic' or pk_type1[pokemon_index1] is not 'Flying' or pk_type2[pokemon_index1]is not 'Flying' or pk_type1[pokemon_index1] is not 'Fairy' or pk_type2[pokemon_index1]is not 'Fairy':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Ground' or pk_type2[pokemon_index2]is 'Ground':
            if pk_type1[pokemon_index1] is not 'Ice' or pk_type2[pokemon_index1]is not 'Ice' or pk_type1[pokemon_index1] is not 'Water' or pk_type2[pokemon_index1]is not 'Water' or pk_type1[pokemon_index1] is not 'Grass' or pk_type2[pokemon_index1]is not 'Grass':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Steel' or pk_type2[pokemon_index2]is 'Steel':
            if pk_type1[pokemon_index1] is not 'Fighting' or pk_type2[pokemon_index1]is not 'Fighting' or pk_type1[pokemon_index1] is not 'Ground' or pk_type2[pokemon_index1]is not 'Ground' or pk_type1[pokemon_index1] is not 'Fire' or pk_type2[pokemon_index1]is not 'Fire':
                advantageIndex += 1
    #if bug type
    if pk_type1[pokemon_index1] is 'Bug' or pk_type2[pokemon_index1]is 'Bug':
        if pk_type1[pokemon_index2]is 'Flying' or pk_type2[pokemon_index2]is 'Flying':
            if pk_type1[pokemon_index1] is not 'Rock' or pk_type2[pokemon_index1]is not 'Rock' or pk_type1[pokemon_index1] is not 'Electric' or pk_type2[pokemon_index1]is not 'Electric' or pk_type1[pokemon_index1] is not 'Ice' or pk_type2[pokemon_index1]is not 'Ice':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Rock' or pk_type2[pokemon_index2]is 'Rock':
            if pk_type1[pokemon_index1] is not 'Fighting' or pk_type2[pokemon_index1]is not 'Fighting' or pk_type1[pokemon_index1] is not 'Ground' or pk_type2[pokemon_index1]is not 'Ground' or pk_type1[pokemon_index1] is not 'Steel' or pk_type2[pokemon_index1]is not 'Steel' or pk_type1[pokemon_index1] is not 'Water' or pk_type2[pokemon_index1]is not 'Water' or pk_type1[pokemon_index1] is not 'Grass' or pk_type2[pokemon_index1]is not 'Grass':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Fire' or pk_type2[pokemon_index2]is 'Fire':
            if pk_type1[pokemon_index1] is not 'Rock' or pk_type2[pokemon_index1]is not 'Rock' or pk_type1[pokemon_index1] is not 'Ground' or pk_type1[pokemon_index1] is not 'Water' or pk_type2[pokemon_index1]is not 'Water' or pk_type1[pokemon_index1] is not 'Grass' or pk_type2[pokemon_index1]is not 'Grass':
                advantageIndex += 1
    #if ghost type
    if pk_type1[pokemon_index1] is 'Ghost' or pk_type2[pokemon_index1]is 'Ghost':
        if pk_type1[pokemon_index2]is 'Ghost' or pk_type2[pokemon_index2]is 'Ghost':
            if pk_type1[pokemon_index1] is not 'Dark' or pk_type2[pokemon_index1]is not 'Dark':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Dark' or pk_type2[pokemon_index2]is 'Dark':
            if pk_type1[pokemon_index1] is not 'Fighting' or pk_type2[pokemon_index1]is not 'Fighting' or pk_type1[pokemon_index1] is not 'Bug' or pk_type2[pokemon_index1]is not 'Bug' or pk_type1[pokemon_index1] is not 'Fairy' or pk_type2[pokemon_index1]is not 'Fairy':
                advantageIndex += 1
    #if steel type
    if pk_type1[pokemon_index1] is 'Steel' or pk_type2[pokemon_index1]is 'Steel':
        if pk_type1[pokemon_index2]is 'Fighting' or pk_type2[pokemon_index2]is 'Fighting':
            if pk_type1[pokemon_index1] is not 'Psychic' or pk_type2[pokemon_index1]is not 'Psychic' or pk_type1[pokemon_index1] is not 'Flying' or pk_type2[pokemon_index1]is not 'Flying' or pk_type1[pokemon_index1] is not 'Fairy' or pk_type2[pokemon_index1]is not 'Fairy':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Ground' or pk_type2[pokemon_index2]is 'Ground':
            if pk_type1[pokemon_index1] is not 'Ice' or pk_type2[pokemon_index1]is not 'Ice' or pk_type1[pokemon_index1] is not 'Water' or pk_type2[pokemon_index1]is not 'Water' or pk_type1[pokemon_index1] is not 'Grass' or pk_type2[pokemon_index1]is not 'Grass':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Fire' or pk_type2[pokemon_index2]is 'Fire':
            if pk_type1[pokemon_index1] is not 'Rock' or pk_type2[pokemon_index1]is not 'Rock' or pk_type1[pokemon_index1] is not 'Ground' or pk_type1[pokemon_index1] is not 'Water' or pk_type2[pokemon_index1]is not 'Water' or pk_type1[pokemon_index1] is not 'Grass' or pk_type2[pokemon_index1]is not 'Grass':
                advantageIndex += 1
    #if fire type
    if pk_type1[pokemon_index1] is 'Fire' or pk_type2[pokemon_index1]is 'Fire':
        if pk_type1[pokemon_index2]is 'Ground' or pk_type2[pokemon_index2]is 'Ground':
            if pk_type1[pokemon_index1] is not 'Ice' or pk_type2[pokemon_index1]is not 'Ice' or pk_type1[pokemon_index1] is not 'Water' or pk_type2[pokemon_index1]is not 'Water' or pk_type1[pokemon_index1] is not 'Grass' or pk_type2[pokemon_index1]is not 'Grass':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Rock' or pk_type2[pokemon_index2]is 'Rock':
            if pk_type1[pokemon_index1] is not 'Fighting' or pk_type2[pokemon_index1]is not 'Fighting' or pk_type1[pokemon_index1] is not 'Ground' or pk_type2[pokemon_index1]is not 'Ground' or pk_type1[pokemon_index1] is not 'Steel' or pk_type2[pokemon_index1]is not 'Steel' or pk_type1[pokemon_index1] is not 'Water' or pk_type2[pokemon_index1]is not 'Water' or pk_type1[pokemon_index1] is not 'Grass' or pk_type2[pokemon_index1]is not 'Grass':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Water' or pk_type2[pokemon_index2]is 'Water':
            if pk_type1[pokemon_index1] is not 'Electric' or pk_type2[pokemon_index1]is not 'Electric' or pk_type1[pokemon_index1] is not 'Water' or pk_type2[pokemon_index1]is not 'Water' or pk_type1[pokemon_index1] is not 'Grass' or pk_type2[pokemon_index1]is not 'Grass':
                advantageIndex += 1
    #if water type
    if pk_type1[pokemon_index1] is 'Water' or pk_type2[pokemon_index1]is 'Water':
        if pk_type1[pokemon_index2]is 'Grass' or pk_type2[pokemon_index2]is 'Grass':
            if pk_type1[pokemon_index1] is not 'Bug' or pk_type2[pokemon_index1]is not 'Bug' or pk_type1[pokemon_index1] is not 'Ice' or pk_type2[pokemon_index1]is not 'Ice' or pk_type1[pokemon_index1] is not 'Flying' or pk_type2[pokemon_index1]is not 'Flying' or pk_type1[pokemon_index1] is not 'Poison' or pk_type2[pokemon_index1]is not 'Poison'or pk_type1[pokemon_index1] is not 'Grass' or pk_type2[pokemon_index1]is not 'Grass' or pk_type1[pokemon_index1] is not 'Fire' or pk_type2[pokemon_index1]is not 'Fire':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Electric' or pk_type2[pokemon_index2]is 'Electric':
            if pk_type1[pokemon_index1] is not 'Ground' or pk_type2[pokemon_index1]is not 'Ground':
                advantageIndex += 1
    #if grass type
    if pk_type1[pokemon_index1] is 'Grass' or pk_type2[pokemon_index1]is 'Grass':
        if pk_type1[pokemon_index2]is 'Fire' or pk_type2[pokemon_index2]is 'Fire':
            if pk_type1[pokemon_index1] is not 'Rock' or pk_type2[pokemon_index1]is not 'Rock' or pk_type1[pokemon_index1] is not 'Ground' or pk_type1[pokemon_index1] is not 'Water' or pk_type2[pokemon_index1]is not 'Water' or pk_type1[pokemon_index1] is not 'Grass' or pk_type2[pokemon_index1]is not 'Grass':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Ice' or pk_type2[pokemon_index2]is 'Ice':
            if pk_type1[pokemon_index1] is not 'Fighting' or pk_type2[pokemon_index1]is not 'Fighting' or pk_type1[pokemon_index1] is not 'Rock' or pk_type2[pokemon_index1]is not 'Rock' or pk_type1[pokemon_index1] is not 'Steel' or pk_type2[pokemon_index1]is not 'Steel' or pk_type1[pokemon_index1] is not 'Fire' or pk_type2[pokemon_index1]is not 'Fire':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Flying' or pk_type2[pokemon_index2]is 'Flying':
            if pk_type1[pokemon_index1] is not 'Rock' or pk_type2[pokemon_index1]is not 'Rock' or pk_type1[pokemon_index1] is not 'Electric' or pk_type2[pokemon_index1]is not 'Electric' or pk_type1[pokemon_index1] is not 'Ice' or pk_type2[pokemon_index1]is not 'Ice':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Poison' or pk_type2[pokemon_index2]is 'Poison':
            if pk_type1[pokemon_index1] is not 'Ground' or pk_type2[pokemon_index1]is not 'Ground' or pk_type1[pokemon_index1] is not 'Psychic' or pk_type2[pokemon_index1]is not 'Psychic':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Bug' or pk_type2[pokemon_index2]is 'Bug':
            if pk_type1[pokemon_index1] is not 'Rock' or pk_type2[pokemon_index1]is not 'Rock' or pk_type1[pokemon_index1] is not 'Fire' or pk_type2[pokemon_index1]is not 'Fire' or pk_type1[pokemon_index1] is not 'Flying' or pk_type2[pokemon_index1]is not 'Flying':
                advantageIndex += 1
    #if Electric type
    if pk_type1[pokemon_index1] is 'Electric' or pk_type2[pokemon_index1] is 'Electric':
        if pk_type1[pokemon_index2]is 'Ground' or pk_type2[pokemon_index2]is 'Ground':
            if pk_type1[pokemon_index1] is not 'Ice' or pk_type2[pokemon_index1]is not 'Ice' or pk_type1[pokemon_index1] is not 'Water' or pk_type2[pokemon_index1]is not 'Water' or pk_type1[pokemon_index1] is not 'Grass' or pk_type2[pokemon_index1]is not 'Grass':
                advantageIndex += 1
    #if Psychic type
    if pk_type1[pokemon_index1] is 'Psychic' or pk_type2[pokemon_index1] is 'Psychic':
        if pk_type1[pokemon_index2]is 'Bug' or pk_type2[pokemon_index2]is 'Bug':
            if pk_type1[pokemon_index1] is not 'Rock' or pk_type2[pokemon_index1]is not 'Rock' or pk_type1[pokemon_index1] is not 'Fire' or pk_type2[pokemon_index1]is not 'Fire' or pk_type1[pokemon_index1] is not 'Flying' or pk_type2[pokemon_index1]is not 'Flying':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Ghost' or pk_type2[pokemon_index2]is 'Ghost':
            if pk_type1[pokemon_index1] is not 'Dark' or pk_type2[pokemon_index1]is not 'Dark':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Dark' or pk_type2[pokemon_index2]is 'Dark':
            if pk_type1[pokemon_index1] is not 'Fighting' or pk_type2[pokemon_index1]is not 'Fighting' or pk_type1[pokemon_index1] is not 'Bug' or pk_type2[pokemon_index1]is not 'Bug' or pk_type1[pokemon_index1] is not 'Fairy' or pk_type2[pokemon_index1]is not 'Fairy':
                advantageIndex += 1
    #if ice type
    if pk_type1[pokemon_index1] is 'Ice' or pk_type2[pokemon_index1] is 'Ice':
        if pk_type1[pokemon_index2]is 'Fire' or pk_type2[pokemon_index2]is 'Fire':
            if pk_type1[pokemon_index1] is not 'Rock' or pk_type2[pokemon_index1]is not 'Rock' or pk_type1[pokemon_index1] is not 'Ground' or pk_type1[pokemon_index1] is not 'Water' or pk_type2[pokemon_index1]is not 'Water' or pk_type1[pokemon_index1] is not 'Grass' or pk_type2[pokemon_index1]is not 'Grass':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Rock' or pk_type2[pokemon_index2]is 'Rock':
            if pk_type1[pokemon_index1] is not 'Fighting' or pk_type2[pokemon_index1]is not 'Fighting' or pk_type1[pokemon_index1] is not 'Ground' or pk_type2[pokemon_index1]is not 'Ground' or pk_type1[pokemon_index1] is not 'Steel' or pk_type2[pokemon_index1]is not 'Steel' or pk_type1[pokemon_index1] is not 'Water' or pk_type2[pokemon_index1]is not 'Water' or pk_type1[pokemon_index1] is not 'Grass' or pk_type2[pokemon_index1]is not 'Grass':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Fighting' or pk_type2[pokemon_index2]is 'Fighting':
            if pk_type1[pokemon_index1] is not 'Psychic' or pk_type2[pokemon_index1]is not 'Psychic' or pk_type1[pokemon_index1] is not 'Flying' or pk_type2[pokemon_index1]is not 'Flying' or pk_type1[pokemon_index1] is not 'Fairy' or pk_type2[pokemon_index1]is not 'Fairy':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Steel' or pk_type2[pokemon_index2]is 'Steel':
            if pk_type1[pokemon_index1] is not 'Fighting' or pk_type2[pokemon_index1]is not 'Fighting' or pk_type1[pokemon_index1] is not 'Ground' or pk_type2[pokemon_index1]is not 'Ground' or pk_type1[pokemon_index1] is not 'Fire' or pk_type2[pokemon_index1]is not 'Fire':
                advantageIndex += 1
    #if dragon type
    if pk_type1[pokemon_index1] is 'Dragon' or pk_type2[pokemon_index1] is 'Dragon':
        if pk_type1[pokemon_index2]is 'Dragon' or pk_type2[pokemon_index2]is 'Dragon':
            if pk_type1[pokemon_index1] is not 'Ice' or pk_type2[pokemon_index1]is not 'Ice' or pk_type1[pokemon_index1] is not 'Fairy' or pk_type2[pokemon_index1]is not 'Fairy':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Ice' or pk_type2[pokemon_index2]is 'Ice':
            if pk_type1[pokemon_index1] is not 'Fighting' or pk_type2[pokemon_index1]is not 'Fighting' or pk_type1[pokemon_index1] is not 'Rock' or pk_type2[pokemon_index1]is not 'Rock' or pk_type1[pokemon_index1] is not 'Steel' or pk_type2[pokemon_index1]is not 'Steel' or pk_type1[pokemon_index1] is not 'Fire' or pk_type2[pokemon_index1]is not 'Fire':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Fairy' or pk_type2[pokemon_index2]is 'Fairy':
            if pk_type1[pokemon_index1] is not 'Poison' or pk_type2[pokemon_index1]is not 'Poison' or pk_type1[pokemon_index1] is not 'Steel' or pk_type2[pokemon_index1]is not 'Steel':
                advantageIndex += 1
    #if Dark Type
    if pk_type1[pokemon_index1] is 'Dark' or pk_type2[pokemon_index1] is 'Dark':
        if pk_type1[pokemon_index2]is 'Fairy' or pk_type2[pokemon_index2]is 'Fairy':
            if pk_type1[pokemon_index1] is not 'Poison' or pk_type2[pokemon_index1]is not 'Poison' or pk_type1[pokemon_index1] is not 'Steel' or pk_type2[pokemon_index1]is not 'Steel':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Fighting' or pk_type2[pokemon_index2]is 'Fighting':
            if pk_type1[pokemon_index1] is not 'Psychic' or pk_type2[pokemon_index1]is not 'Psychic' or pk_type1[pokemon_index1] is not 'Flying' or pk_type2[pokemon_index1]is not 'Flying' or pk_type1[pokemon_index1] is not 'Fairy' or pk_type2[pokemon_index1]is not 'Fairy':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Bug' or pk_type2[pokemon_index2]is 'Bug':
            if pk_type1[pokemon_index1] is not 'Rock' or pk_type2[pokemon_index1]is not 'Rock' or pk_type1[pokemon_index1] is not 'Fire' or pk_type2[pokemon_index1]is not 'Fire' or pk_type1[pokemon_index1] is not 'Flying' or pk_type2[pokemon_index1]is not 'Flying':
                advantageIndex += 1
    #if fairy type
    if pk_type1[pokemon_index1] is 'Fairy' or pk_type2[pokemon_index1] is 'Fairy':
        if pk_type1[pokemon_index2]is 'Steel' or pk_type2[pokemon_index2]is 'Steel':
            if pk_type1[pokemon_index1] is not 'Fighting' or pk_type2[pokemon_index1]is not 'Fighting' or pk_type1[pokemon_index1] is not 'Ground' or pk_type2[pokemon_index1]is not 'Ground' or pk_type1[pokemon_index1] is not 'Fire' or pk_type2[pokemon_index1]is not 'Fire':
                advantageIndex += 1
        if pk_type1[pokemon_index2]is 'Steel' or pk_type2[pokemon_index2]is 'Steel':
            if pk_type1[pokemon_index1] is not 'Fighting' or pk_type2[pokemon_index1]is not 'Fighting' or pk_type1[pokemon_index1] is not 'Ground' or pk_type2[pokemon_index1]is not 'Ground' or pk_type1[pokemon_index1] is not 'Fire' or pk_type2[pokemon_index1]is not 'Fire':
                advantageIndex += 1