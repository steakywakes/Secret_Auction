from os import system
from art import logo

game_dictionary = {}

def game_start():
    print(logo)
    print("Welcome to the secret auction! >:)")
    dictionary_addition()

def dictionary_addition():
    game_end = False

    while not game_end:
        name = input("Please enter your name: ")
        bid = int(input("Please enter a bid amount: "))
        continuation = input("Are there any other bidders? Please enter 'y' or 'n' ").lower()
        game_dictionary[name] = bid
        print(game_dictionary)
        if continuation == 'y':
            system("clear")
            game_start()
        else:
            game_end = True
            calculate_winner()

def calculate_winner():
    winner = ''
    winner_score = 0
    for bidder in game_dictionary:
        if int(game_dictionary[bidder]) > winner_score:
            winner_score = game_dictionary[bidder]
            winner = bidder
    print(f"The winner is: {winner}! Thanks for playing :)")

game_start()