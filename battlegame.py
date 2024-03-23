"""
Battle Game Work Shop 1
Aaron S.
Last updated: 03/23/2024

"""
# Task 1 Game Variables
    
wizard = "Wizard"
elf = "Elf"
human = "Human"
dwarf = "Dwarf"

wizard_hp = 70
elf_hp = 100
human_hp = 150
dwarf_hp = 175

dragon_hp = 300

wizard_damage = 150
elf_damage = 100
human_damage = 20
dwarf_damage = 60

dragon_damage = 50

#Task 2 and Task 3 Player Choice
while True:
    print("\n Welcome to the Battle Game!\n")
    print("1. Wizard")
    print("2. Elf")
    print("3. Human")
    print("4. Dwarf")
    print("5. Exit\n")

    character = input("Choose your character:").lower()    

    if character == "1" or character=="wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break   
    elif character == "2" or character== "elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == "3" or character== "human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    elif character == "4" or character== "dwarf":
        character = dwarf
        my_hp = dwarf_hp
        my_damage = dwarf_damage
        break
    elif character == "5" or character== "exit":
        print("You have chosen to exit the game.")
        exit()
    else: 
        print("\n Unknown character")  
    break

# Player Choice
print("\n You have chosen a mighty: ", character)
print("Health: ", my_hp)
print("Damage: ", my_damage)
    
# Task 4 Battle Dragon

while True:
    dragon_hp = dragon_hp - my_damage
    print("\nThe", character, "damaged the Dragon!")
    print("The Dragon's hitpoints are now: ", dragon_hp)
    
    if dragon_hp <= 0:
        print("The Dragon has lost the battle.")
        break
    
    my_hp = my_hp - dragon_damage
    print("\nThe Dragon strikes back at", character)
    print("The", character, "'s hitpoints are now: ", my_hp)
    
    if my_hp <= 0:
        print("\nThe", character, "has lost the battle!")
        break

# Task 5 Play Again
while True:
    play_again = input("\nDo you want to play again? Type Yes or No: ").lower()
    if play_again == "yes":
        exec(open("battlegame.py").read())
    elif play_again == "no":
        print("\nThank you for playing the Battle Game!")
        exit()
    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")

