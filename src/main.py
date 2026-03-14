from game import start_game
from utils import restart_prompt


def run_game():
    while True:

        result = start_game()

        if result == "win":
            print("\nCongratulations! You completed the quest!")

        else:
            print("\nBetter luck next time!")

        if not restart_prompt():
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    run_game()