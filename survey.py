import json

with open("survey.json") as f1:
    survey = json.load(f1)

def get_user_answer(question): 
    option_nums = len(question["options"])
    
    while True:
        answer = input("Your answer: ")

        if not answer.isdigit():
            print("You must enter a number.")
            continue

        answer = int(answer)

        if 1 <= answer <= option_nums:
            
            return answer
        
        print("Invalid answer. Try again.")


def user_interference():

    chosen_skills = set()

    for question in survey["questions"]:
        print(question["question"])
        options = question["options"]

        for i, option in enumerate(options, start=1):
            print("(",i, ")", option["text"])

        choice = get_user_answer(question)
        selected_option = options[choice - 1]

        for skill in selected_option["skills"]:
            chosen_skills.add(skill)

        print()

    return chosen_skills

