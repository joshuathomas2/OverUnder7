import random

in_game = True
cash = 150
valid_bet_types = ["OVER", "UNDER", "EXACT"]

while in_game:
    die_one = random.randint(1, 6)
    die_two = random.randint(1, 6)
    roll = die_one + die_two

    valid_input = False
    while not valid_input:
        bet_type = input("How would you like to bet? (OVER, UNDER, or EXACT) ").upper()
        if bet_type in valid_bet_types:
            valid_input = True
        else:
            print("That is an invalid bet type.")

    bet_amount = int(input(f"How much would you like to bet? You have ${cash}. "))
    cash -= bet_amount

    print(f"The roll was {roll}.")

    if bet_type == "OVER" and roll > 7:
        print(f"You win! You won ${bet_amount}!")
        cash += bet_amount * 2
    elif bet_type == "UNDER" and roll < 7:
        print(f"You win! You won ${bet_amount}!")
        cash += bet_amount * 2
    elif bet_type == "EXACT" and roll == 7:
        print(f"You win! You won ${bet_amount * 4}!")
        cash += bet_amount * 5
    else:
        print(f"You lose! You lost ${bet_amount}!")

    print(f"You have ${cash} remaining. ")

    play_again = input("Would you like to play again? (Y/N) ").upper()

    if play_again == "N" or play_again == "NO":
        in_game = False
