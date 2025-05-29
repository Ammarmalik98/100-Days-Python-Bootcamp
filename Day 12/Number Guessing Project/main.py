import random
import art
print(art.logo)
print("I am thinking of a number between 1 and 100.")
number = random.randint(1, 100)

player_guess = 0
player_life = 0

difficulty = input("Choose a difficulty: easy or hard:\n ").lower()
if difficulty == "easy":
    player_life += 10
    while player_life > 0:
        player_guess = int(input("Guess a number between 1 and 100: "))
        if player_guess < number:
            player_life -= 1
            print(f"Your guess is too low, you have {player_life} tries remaining")
        elif player_guess > number:
            player_life -= 1
            print(f"Your guess is too high, you have {player_life} tries remaining")
        elif player_guess == number:
            print("Congratulations, You guessed right!")
            break
    if player_life == 0:
        print(f"Game over, you lose! the secret number was: {number}")

if difficulty == "hard":
    player_life += 5
    while player_life > 0:
        player_guess = int(input("Guess a number between 1 and 100: "))
        if player_guess < number:
            player_life -= 1
            print(f"Your guess is too low, you have {player_life} tries remaining")
        elif player_guess > number:
            player_life -= 1
            print(f"Your guess is too high, you have {player_life} tries remaining")
        elif player_guess == number:
            print("Congratulations, You guessed right!")
            break
    if player_life == 0:
        print(f"Game over, you lose! the secret number was: {number}")
