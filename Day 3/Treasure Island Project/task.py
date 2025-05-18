print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to The Cave of Trials.")
print("Your mission is to find the treasure.")

print("SCENARIO 1: Forked path")
print("you step into the cave and you see two paths. \n Do you go 'Left' or 'Right' ?")

choice1 = input("Left or Right")
if choice1 == "Left" or choice1 == "left":
    print("You choose correctly, please proceed to the next scenario!")
    print("SCENARIO 2: The Riddle Pool")
    print(
        "After surviving the spider (lucky you picked left), you reach a glowing pool.\n"
        "A stone tablet reads: \n Answer truthfully, or drown.")

    print("The tablet asks: 'What has to be broken before it can be used?'")
    print("A. A promise\nB. An egg\nC. A seal")

    choice2 = input("Your answer (A, B, or C): ")

    if choice2 == "B" or "b":
        print("You choose correctly, please proceed to the next scenario!")
        print("SCENARIO 3: The Guardian’s Choice")
        print("A spectral guardian blocks your way. "
              "He says:\n“Choose a gift: Strength, Wisdom, or Speed.”")

        print("Choose your gift: strength, wisdom, or speed")

        choice3 = input("Your choice: ").lower()

        if choice3 == "wisdom":
            print("You have chosen correctly, please proceed to the treasure room!")
            print("FINAL SCENARIO: The Treasure Room")
            print(
                "You have made it to the treasure room, Alas! a trial remains\n"
                "atop the pedestal lies a box.\nIt has two buttons: Red and Blue. "
                "One gives treasure. The other, death. ")

            print("You see a box with two buttons: red and blue.")
            choice4 = input("Which do you press? ")

            if choice4.lower() == "blue":
                print("✨The box opens! Treasure pours out! You win!")
            else:
                print("💥 Boom! The cave collapses. Game Over!")
        elif choice3 == "strength":
            print("You try to fight the guardian. You lose. Game Over!")
        elif choice3 == "speed":
            print("You try to run. You trip. Game Over!")
        else:
            print("The guardian vanishes, unimpressed. Game Over!")
    else:
        print("The pool boils. You screamed your last. Game Over!")
elif choice1 == "right":
    print("A giant spider descends and wraps you like a burrito. Game Over!")
else:
    print("Confused, you walk into a wall. Game Over!")