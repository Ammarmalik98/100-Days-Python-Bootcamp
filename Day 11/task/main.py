import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

greeting = input("Welcome! Do you want to play a game of Blackjack? (y/n) \n").lower()


if greeting == "y":
    print(art.logo)
    user_cards = random.sample(cards, 2)
    card_total = sum(user_cards)
    print(f"Your cards are {user_cards} : total score is {card_total}")

    computer_cards = []
    computer_cards.append(random.choice(cards))
    print(f"Computer's first card is {computer_cards}")
    computer_cards_total = 0

    if card_total > 21:
        print("Bust! You lost")
    elif card_total == 21:
        print("Black Jack! You won")
    elif card_total < 21:
        increase_user_cards = input("Would you like to add another card? (y/n) \n").lower()
        if increase_user_cards == "n":
            print(f"Your cards are {user_cards} : total score is {card_total}")
            computer_cards.append(random.choice(cards))
            computer_cards_total = sum(computer_cards)
            while computer_cards_total < 17:
                computer_cards.append(random.choice(cards))
            print(f"Computer's total cards are {computer_cards}: total score is {computer_cards_total}")
            if card_total > computer_cards_total and card_total <= 21:
                print(f"Your cards are {user_cards} : total score is {card_total}\nComputer's Cards are {computer_cards} Total of {computer_cards_total}\nYou Win!")
            elif computer_cards_total > card_total and computer_cards_total <= 21:
                print(f"Your cards are {user_cards} : total score is {card_total}\nComputer's Cards are {computer_cards} Total of {computer_cards_total}\nYou Lose!")
            elif card_total == computer_cards_total:
                print("Sorry, It is a Draw")
        elif increase_user_cards == "y":
            user_cards.append(random.choice(cards))
            card_total = sum(user_cards)
            print(f"Your cards are {user_cards} : total score is {card_total}")

            computer_cards.append(random.choice(cards))
            computer_cards_total = sum(computer_cards)
            print(f"Computer's cards are {computer_cards}, Total of {computer_cards_total}")



