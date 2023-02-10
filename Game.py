import pygame, json, time, os.path
from enum import Enum

pygame.init()

display = pygame.display.set_mode((800, 600))

# Clock
clock = pygame.time.Clock()

player_scores = {}

def reset_user_score():
    """ Reset the player's scores to default state"""
    player_scores["runs_won"] = 0
    player_scores["runs_lost"] = 0
    player_scores["pythons_slayed"] = 0
    
    #Look up what other stats to track

def rewrite_player_scores(user_scores: dict):
    """ used to save player scores to file"""
    with open("player_scores.json", 'w', encoding = "UTF-16") as outfile:
        outfile.write(json.dumps(player_scores, indent = 4))

if os.path.exists("player_values.json"):
    """ Loads the player's stats if they exist
        at the start of the program or creates
        the file if it doesn't exist.
    """
    with open("player_scores.json", 'r', encoding = "UTF-16") as openfile:
        player_scores = json.load(openfile)

else:
    player_scores = {}
    reset_user_score()
    rewrite_player_scores(player_scores)



class GameState(Enum):
    # all names currently are me having fun, not show of final product™

    Menu = 1
    Gaming = 2
    PauseScreen = 3
    Win = 4
    Lost = 5

class Game:
    

