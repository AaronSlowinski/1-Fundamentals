import random

high_score = 0

def roll_die():
    return random.randint(1, 6)

def dice_game():
    global high_score
    print("\nWelcome to the Dice Game!\n")
    print("You will roll two dice and try to get the highest score possible.\n")
    print("Current high score is:", high_score, "\n")

    while True:
        print("1. Roll the dice\n")
        print("2. Quit the game\n")
        choice = input("Enter your choice: ")

        if choice == "2":
            print("Goodbye!")
            break
        elif choice == "1":
            die1 = roll_die()
            die2 = roll_die()
            total = die1 + die2
            print("\nYou rolled a", die1, "and a", die2, "for a total of", total, "\n")

            if total > high_score:
                high_score = total
                print("\nCongratulations! You have a new high score of", high_score, "\n")
        else:
            print("Invalid choice. Please try again.")

dice_game()
