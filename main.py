import json

with open("races.json") as f:
    races = json.load(f)

chosen_skills = {"Conjuration", "Light Armor",  "Speech",  "Smithing",  "Lockpicking"}

def user_interference():
    print("\n| ----------------------------------- |")
    print("| Welcome to the Skyrim Race Chooser! |")
    print("| ----------------------------------- |\n")
user_interference()
def evaluate_races(races, chosen_skills):

    scores = {}
    for race in races:
        scores[race] = 0

    for skill in chosen_skills:
        for race, race_skill_value in races.items():

            skill_value = race_skill_value.get(skill, 15)

            if skill_value == 25:
                scores[race] += 3
            elif skill_value == 20:
                scores[race] += 2
            else: 
                scores[race] += 1
    return scores


def rank_results():
    scores = evaluate_races(races, chosen_skills)  
    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    
    for race, score in sorted_scores:
        print(race, score)

rank_results()
