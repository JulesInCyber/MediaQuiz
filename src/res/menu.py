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
    wait_enter()

def quit_game():
    clear_screen()
    print("Thanks for playing!")
    sys.exit()

def main_menu():
    pass

