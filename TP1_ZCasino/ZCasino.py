import time
from random import randrange
from math import ceil


def choose_number():
    """Ask the player on which number he want to bet on. It should be between 0 and 49.

    Returns:
        int: the choosen number on which player want to bet.
    """
    number_placed = -1  # Incorrect value to enter in the while

    while number_placed < 0 or number_placed > 49:
        try:
            number_placed = int(
                input(">> Enter a number, between 0 and 49, on which you want to bet: ")
            )
        except ValueError:
            print("Your input is not an integer.")
            number_placed = -1  # Stay in the while
        if number_placed < 0 or number_placed > 49:
            print("Your number is not in the range (0 - 49).")

    return number_placed


def choose_bet(money):
    """Ask the player how much he want want to bet. He can't be more than he has money.

    Args:
        money (int): Amount of money that the player currently have.

    Returns:
        int: The amount he choosed to bet.
    """
    bet_amount = 0  # Incorrect value to enter in the while

    while bet_amount <= 0 or bet_amount > money:
        try:
            bet_amount = int(input(">> Enter a amount (in $) to bet: "))
        except ValueError:
            print("Your input is not an integer.")
            bet_amount = 0  # Stay in the while
        if bet_amount <= 0:
            print("You can't a bet a negative value.")
        elif bet_amount > money:
            print("You can't bet more money that you have ($", money, ").")
    return bet_amount


def main():
    # Initial values to enter in the ZCasino
    money = 500
    play = True
    print("Welcome to the ZCasino roulette. You start with $", money, ".")

    while play:

        # Player places his bet a on roulette's number
        number_placed = choose_number()
        bet_amount = choose_bet(money)

        # Spin the roulette
        print("The bets are placed !\n**The roulette spins...**")
        time.sleep(3)  # Simulate the duration of the spinning roulette
        winning_number = randrange(50)

        # Announce the result
        print("And the winning number is: ", winning_number, "!!!")
        time.sleep(1)  # Simulate the speaking time

        # Determine if the player lost or earned money
        if winning_number == number_placed:
            print("Congratulations ! You earn $", bet_amount * 3, "!")
            money += bet_amount * 3
        elif winning_number % 2 == number_placed % 2:  # Same color
            recompense = ceil(bet_amount / 2)
            print("You bet on the right color, so you earn $", recompense, ".")
            money += recompense
        else:
            print("No luck, you lose your bet...")
            money -= bet_amount

        time.sleep(1)  # Simulate the speaking time

        # Check if the game can continue
        if money <= 0:
            print("Sorry but you've no more money to bet.")
            play = False

        # Player can leave the game or continue to bet
        else:
            print("You currently have $", money, ".")
            leave = input(">> Do you want to leave the casino ? (y/n) ")
            if leave == "y" or leave == "Y":
                print("Thank you for playing, bye !")
                play = False


if __name__ == "__main__":
    main()
