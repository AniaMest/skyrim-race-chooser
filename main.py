from survey import user_interference
from scoring import rank_results
from statistics import statistics

def display():

    print("\n| -------------------------------------- |")
    print("|  Welcome to the Skyrim Race Chooser!   |")
    print("| -------------------------------------- |\n")

def main():
    display()
    chosen_skills = user_interference()

    results = rank_results(chosen_skills)

    print("The top results are:")
    for race, score in results[:3]:
        print(race, score)

    statistics(chosen_skills)

if __name__ == "__main__":
    main()