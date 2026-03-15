# Skyrim Race Chooser

Skyrim Race Chooser is a command-line tool that recommends a player race based on the player's preferred skills. 

The preferred skills are determined by a brief questionnaire that is designed to study the player's gameplay preferences in Skyrim. 
The program analyzes answers and ranks player races based on the match between prioritized skills and starting skill bonuses for each race.
Additionally, the program can display result statistics after the top results are shown.
___________________________________

## Project Purpose

The project was an experiment that served as a way to become more familiar with structuring Python projects, working with JSON data and using Git.

The goal was to make a small but well-structured, practical project that combines my interest in improving my programming skills with one of my favorite games *The Elder Scrolls V: Skyrim*.
___________________________________

## Tools Used

- Python
- JSON
- Git
__________________________________

## Requirement

Python 3.8+
___________________________________

## Example

Which combat style sounds best?
( 1 ) Fighting with melee weapons
( 2 ) Archery
( 3 ) Magic
( 4 ) Mix
Your answer: 4

Preferred armor?
( 1 ) Light armor
( 2 ) Heavy armor
( 3 ) Robes
Your answer: 1

...

The top results are:
Dunmer
Argonian
Breton
___________________________________

### Statistics Feature Example

The top results are:
Dunmer
Argonian
Breton
Would you like to learn about the result statistics? (y/n) y    #The user is prompted to type "y" to see statistics
Dunmer: 7/7 (100%)
Argonian: 6/7 (86%)
Breton: 6/7 (86%)
Khajiit: 6/7 (86%)
Redguard: 6/7 (86%)
Altmer: 5/7 (71%)
Bosmer: 5/7 (71%)
Nord: 5/7 (71%)
Imperial: 3/7 (43%)
Orsimer: 3/7 (43%)
___________________________________

## How To Run The Program

- Clone the repository:
git clone https://github.com/yourusername/skyrim-race-chooser.git



- Go to the project folder:
cd skyrim-race-chooser


- Run the program:
python main.py
___________________________________

## The Project Structure

main.py — program entry point  
survey.py — handles questions and user's input  
engine.py — assesses races and calculates scores  
statistics.py — calculates and displays result statistics  
survey.json — survey questions; answer to skill mappings 
races.json — race skill data
___________________________________

## Scoring System

Through survey the program collects desired player skills --> creates a skill-set

In Skyrim each player race has either 15, 20 or 25 starting points for every skill.

The program goes through each race and evaluates how good a match it's starting skills are to the created skill-set.
So, these starting skill points determine total scores:

- Starting Point: 25 --> +2
- Starting Point: 20 --> +1
- Starting Point: 15 --> +0

The races are then ranked by their total score.
___________________________________

## Future Additions

- Survey UI refinement;
- Option to continue choosing player race based on special racial abilities and powers (e.g. 50% Fire Resistance for Dunmers);
- More precise statistical analysis;
- Upgrade to a web app (Likely Flask-based);
- Visual representation of result statistics.

__________________________________

## Data Source

The data regarding starting skills by race was collected from the Elder Scrolls Wiki:
- https://elderscrolls.fandom.com/wiki/Races_(Skyrim)