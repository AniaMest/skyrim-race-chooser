import json

with open("races.json") as f:
    races = json.load(f)

def evaluate_races(races, chosen_skills):

    scores = {race: 0 for race in races}


    for skill in chosen_skills:
        for race, race_skill_value in races.items():

            skill_value = race_skill_value.get(skill, 15)

            if skill_value == 25:
                scores[race] += 2
            elif skill_value == 20:
                scores[race] += 1
            else: 
                scores[race] += 0
    return scores

def rank_results(chosen_skills):
    scores = evaluate_races(races, chosen_skills)
    return sorted(scores.items(), key=lambda item: item[1], reverse=True)
