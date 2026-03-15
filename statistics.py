from scoring import rank_results

def statistics(chosen_skills):
    user_answer = input("Would you like to learn about the result statistics? (y/n) ")

    if  user_answer == "y":
        
        for race, score in rank_results(chosen_skills):
            percent = round((score / 7) * 100) 
            print(f"{race}: {score}/7 ({percent}%)")


    elif user_answer == "n":
        pass

    else:
        print("Invalid input. ")
        statistics(chosen_skills)