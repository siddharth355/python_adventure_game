# Utility functions for the adventure game

def get_player_choice(options):
    while True:
        choice = input("Enter your choice: ").strip()

        if choice in options:
            return choice
        else:
            print("Invalid choice. Please try again.")


def restart_prompt():
    choice = input("\nDo you want to play again? (yes/no): ").lower()

    if choice == "yes":
        return True
    return False