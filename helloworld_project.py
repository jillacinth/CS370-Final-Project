'''
Jillian Jacinto
CS370
Midterm Project Proposal
'''

import pandas as pd

pokemon_list = pd.read_csv(r'pokemon.csv')

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
av_score = (sum(hp)+sum(at)+sum(defe)+sum(spAt)+sum(spDef)+sum(sd))/1190

def betterOpp(user):
    if at[names.index(user)] < av_at:
        return names[search_higher(defe, at[names.index(user)])]
    elif defe[names.index(user)] < av_def:
        return names[search_higher(at, defe[names.index(user)])]
    elif spAt[names.index(user)] < av_spAt:
        return names[search_higher(spDef, spAt[names.index(user)])]
    elif spDef[names.index(user)] < av_spDef:
        return names[search_higher(spAt, spDef[names.index(user)])]
    #else:
        #return names[search_higher(total_score, total_score[names.index(user)])]


def search_higher(list, num):
    highest_diff = 0
    best_index = 0
    for x in list:
        if (x - num) > highest_diff:
            highest_diff = x - num
            best_index =  list.index(x)
    
    return best_index

print(names)
user = input("What Gen 1 Pokemon would you like to use? ")
print("Your pokemon: " + str(user) + "\nStats:\nHP = " + str(hp[names.index(user)])+ "\nAttack = " + str(at[names.index(user)]) + "\nDefense = " + str(defe[names.index(user)]) + "\nSpecial Attack = " + str(spAt[names.index(user)]) + "\nSpecial Defense = " + str(spDef[names.index(user)]) + "\nSpeed = " + str(sd[names.index(user)]))
better = betterOpp(user)
print("You will lose to a " + better)

