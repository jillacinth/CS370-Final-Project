'''
Jillian Jacinto
CS370
Midterm Project Proposal
'''

import pandas as pd

data = pd.read_csv(r"C:\Users\jill3\Documents\Junior Year\Fall 2022\CS 370\project\pokemon_stats.csv")

names = data['Pokemon'].tolist()
hp = data['HP'].tolist()
at = data['Attack'].tolist()
defe = data['Defense'].tolist()
spAt = data['Special Attack'].tolist()
spDef = data['Special Defense'].tolist()
sd = data['Speed'].tolist()
total_score = data['Total'].tolist()

av_hp = (sum(hp))/151
av_at = (sum(at))/151
av_def = (sum(defe))/151
av_spAt = (sum(spAt))/151
av_spDef = (sum(spDef))/151
av_sd = (sum(sd))/151
av_score = (sum(total_score))/151

def betterOpp(user):
    if at[names.index(user)] < av_at:
        return names[search_higher(defe, at[names.index(user)])]
    elif defe[names.index(user)] < av_def:
        return names[search_higher(at, defe[names.index(user)])]
    elif spAt[names.index(user)] < av_spAt:
        return names[search_higher(spDef, spAt[names.index(user)])]
    elif spDef[names.index(user)] < av_spDef:
        return names[search_higher(spAt, spDef[names.index(user)])]
    else:
        return names[search_higher(total_score, total_score[names.index(user)])]


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
print("Your pokemon: " + str(user) + "\nStats:\nHP = " + str(hp[names.index(user)])+ "\nAttack = " + str(at[names.index(user)]) + "\nDefense = " + str(defe[names.index(user)]) + "\nSpecial Attack = " + str(spAt[names.index(user)]) + "\nSpecial Defense = " + str(spDef[names.index(user)]) + "\nSpeed = " + str(sd[names.index(user)]) + "\nTotal = " + str(total_score[names.index(user)]))
better = betterOpp(user)
print("You will lose to a " + better)

