from utils import get_player_choice


def forest_path():
    print("\nYou enter the dark forest.")
    print("You see a river and a tall tree.")

    print("1. Follow the river")
    print("2. Climb the tree")

    choice = get_player_choice(["1", "2"])

    if choice == "1":
        print("\nThe river leads you to a hidden temple.")
        print("🏆 You found the treasure!")
        return "win"

    elif choice == "2":
        print("\nYou fall from the tree.")
        print("💀 Game Over.")
        return "lose"


def cave_path():
    print("\nYou enter the mysterious cave.")

    print("1. Light a torch")
    print("2. Walk in the dark")

    choice = get_player_choice(["1", "2"])

    if choice == "1":
        print("\nThe torch reveals a treasure chest!")
        print("🏆 You found the treasure!")
        return "win"

    elif choice == "2":
        print("\nYou fall into a pit.")
        print("💀 Game Over.")
        return "lose"


def start_game():
    print("\n=== Adventure Game ===")

    name = input("Enter your name: ")

    print(f"\nWelcome {name}! Your quest is to find the legendary treasure.")

    print("\nChoose your path:")
    print("1. Dark Forest")
    print("2. Mysterious Cave")

    choice = get_player_choice(["1", "2"])

    if choice == "1":
        return forest_path()
    else:
        return cave_path()