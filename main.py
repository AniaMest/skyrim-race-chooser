import json

with open("races.json") as f:
    races = json.load(f)

with open("survey.json") as f1:
    survey = json.load(f1)

def user_interference():

    print("\n| -------------------------------------- |")
    print("|  Welcome to the Skyrim Race Chooser!   |")
    print("| -------------------------------------- |\n")

    chosen_skills = set()

    for question in survey["questions"]:
        print(question["question"])
        options = question["options"]

        for i, option in enumerate(options, start=1):
            print("(",i, ")", option["text"])

        choice = int(input("Choose option: "))
        selected_option = options[choice - 1]

        for skill in selected_option["skills"]:
            chosen_skills.add(skill)

        print()

    return chosen_skills


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

chosen_skills = user_interference()
def rank_results():
    scores = evaluate_races(races, chosen_skills)  
    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    print("The results (Ranked best to worst.)")
    for race, score in sorted_scores:
        print(race, score)

rank_results()
