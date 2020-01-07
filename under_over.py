import random

in_game = True
cash = 150
valid_bets = ["OVER", "UNDER", "EXACT"]

while in_game:
    die_one = random.randrange(1, 6)
    die_two = random.randrange(1, 6)
    roll = die_one + die_two

    valid_input = False
    while not valid_input:
        bet_type = input("How would you like to bet? (OVER, UNDER, or EXACT) ").upper()
        if bet_type in valid_bets:
            valid_input = True
        else:
            print("That is an invalid bet.")

    bet_amount = float(input("How much would you like to bet? "))
    cash -= bet_amount

    if bet_type == "OVER" and roll > 7:
        print(f"You win! You won {bet_amount}!")
        cash += bet_amount * 2
    elif bet_type == "UNDER" and roll < 7:
        print(f"You win! You won {bet_amount}!")
        cash += bet_amount * 2
    elif bet_type == "EXACT" and roll == 7:
        print(f"You win! You won {bet_amount * 4}!")
        cash += bet_amount * 5
    else:
        print(f"You lose! You lost {bet_amount}!")

    print(f"You have ${cash} remaining. ")

    print(f"DEBUG: bet_type was {bet_type}.")
    print(f"DEBUG: bet_amount was {bet_amount}.")
    print(f"DEBUG: roll was {roll}.")




