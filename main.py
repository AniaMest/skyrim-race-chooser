import json

with open("races.json") as f:
    races = json.load(f)

chosen_skills = {"Conjuration", "Light Armor",  "Speech",  "Smithing",  "Lockpicking"}

def evaluate_races(races, chosen_skills):

    scores = {}
    for race in races:
        scores[race] = 0
    return scores
#   for skill in chosen_skills:
#       for race, race_skills in races.items():
            

    

print(races.items())
