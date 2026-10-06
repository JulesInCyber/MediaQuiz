from src.res.queries import *
from src.res.loop import *
from src.res.menu import *

def play_round():
    media = get_random_media()
    media_title = media[1]
    media_type = media[3]

    all_clues = get_clues(media)
    points = 0

    for i, clue in enumerate(all_clues):
        print(f"Hint {i+1}: {clue}")
        user_input = input("Make a Guess: ")
        user_answer = normalize_answer(user_input)

        result = check_answer(user_answer, media_title)
        if result == True:
            # Fewer hints used means more points
            points = len(all_clues) - i
            print("\nCorrect!")
            break
        elif check_franchise(user_answer, media_title):
            print("Correct Franchise -- Wrong Movie\n")

    print(f"The secret {media_type} was: {media_title}")
    print(f"You scored {points} point(s) this round.")

    return points

def main():
    total_score = 0
    rounds_played = 0

    while True:
        clear_screen()
        show_title()
        print("=== Main Menu ===\n")
        print(f"Score: {total_score} points in {rounds_played} round(s)\n")
        print("1) Start Game")
        print("2) Instructions")
        print("3) Quit")
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            start_game()
            total_score += play_round()
            rounds_played += 1
            print(f"Total score: {total_score} points")
            wait_enter()
        elif choice == "2":
            instructions()
        elif choice == "3":
            quit_game(total_score, rounds_played)

if __name__ == "__main__":
    main()
