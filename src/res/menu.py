import os
import sys


TITLE = r"""
 __  __          _ _        ___        _
|  \/  | ___  __| (_) __ _ / _ \ _   _(_)_______
| |\/| |/ _ \/ _` | |/ _` | | | | | | | |_  /_  /
| |  | |  __/ (_| | | (_| | |_| | |_| | |/ / / /
|_|  |_|\___|\__,_|_|\__,_|\__\_\\__,_|_/___/___|
"""

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_title():
    print(TITLE)

def wait_enter():
    input("\nPress Enter to return to the main menu...")

def start_game():
    clear_screen()
    show_title()

def instructions():
    clear_screen()
    show_title()
    print("=== Instructions ===\n")
    print("You will be shown a series of facts about a movie.")
    print("Use these clues to guess the movie.")
    print("The fewer clues you need, the better your score!")
    print("If you guess another movie of the same franchise (e.g. a sequel),")
    print("you will see \"Correct Franchise -- Wrong Movie\".\n")
    print("Movies of a franchise can also be guessed as \"<Franchise>: <Number>\",")
    print("where the number is the movie's place in the series (by release):")
    print("  \"Toy Story: 2\" or \"Toy Story 2\"  ->  Toy Story 2")
    print("  \"The Lord of the Rings: 3\"     ->  The Lord of the Rings: The Return of the King")
    print("The first movie can also be guessed by the franchise name alone:")
    print("  \"The Lord of the Rings\"        ->  The Lord of the Rings: The Fellowship of the Ring\n")
    print("Scoring: a correct guess on hint 1 is worth 4 points,")
    print("hint 2 is worth 3, hint 3 is worth 2 and hint 4 is worth 1.")
    print("If you don't guess the movie, you get 0 points for that round.")
    wait_enter()

def quit_game(score, rounds):
    clear_screen()
    show_title()
    print(f"Final score: {score} points in {rounds} round(s)")
    print("Thanks for playing!")
    sys.exit()

