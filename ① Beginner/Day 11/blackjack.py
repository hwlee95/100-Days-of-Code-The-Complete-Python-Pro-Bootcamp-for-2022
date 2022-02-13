################### Simple Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import art
import random

def black_jack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    computer = []
    player = []
    play = input("\n♣️ Do you want to play a game of Blackjacks? ♠️ Type 'y' or 'n': ").lower()
    while play == 'y':
        print(art.logo)
        first_card = random.choices(cards)
        second_card = random.choices(cards)
        player = first_card + second_card
        player_score = first_card[0] + second_card[0]
        print(f"Your cards: {player}, current score: {player_score}")
        computer_first_card = random.choices(cards)
        computer_second_card = random.choices(cards)
        computer = computer_first_card + computer_second_card
        print(f"Computer's first card: {computer_first_card}")
        get_third_card = input("Type 'y' to get another card, type 'n' to pass: ")
        computer_score = computer_first_card[0] + computer_second_card[0]
        while computer_score < 17:
            more_card = random.choices(cards)
            computer += more_card
            new_total = computer_score + more_card[0]
            computer_score = new_total

        if get_third_card == 'y':
            third_card = random.choices(cards)
            player += third_card
            new_player_score = player_score + third_card[0]
            print(f"Your final hand: {player}, final score: {new_player_score}")
            print(f"Computer's final hand: {computer}, final score: {computer_score}")
            if new_player_score > 21:
                print("You're over 21. You lose 😢")
            elif (21 - new_player_score) < (21 - computer_score):
                print("You win! 🥳")
            elif (21 - new_player_score) == (21 - computer_score):
                print("Draw 🙃")
            else:
                print("You lose 😢")
        else:
            print(f"Your final hand: {player}, final score: {player_score}")
            print(f"Computer's final hand: {computer}, final score: {computer_score}")
            if player_score > 21:
                print("You're over 21. You lose 😢")
            elif (21 - player_score) < (21 - computer_score):
                print("You win! 🥳")
            elif (21 - player_score) == (21 - computer_score):
                print("Draw 🙃")
            else:
                print("You lose 😢")

        play = input("\n♣️ Do you want to play a game of Blackjacks? ♠️ Type 'y' or 'n': ").lower()



if __name__ == "__main__":
    black_jack()