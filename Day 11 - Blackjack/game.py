from random import choice
from art import logo
from os import system


def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)


def calculate_score(list):
    score = sum(list)
    if score == 21 and len(list) == 2:
        return 0
    elif score > 21:
        if 11 in list:
            list.remove(11)
            list.append(1)
            calculate_score(list)
        else:
            return score
    else:
        return score


def compare(score1, score2):
    if score1 == score2:
        return "A draw"
    elif score1 == 0:

        return "You win! You got a blackjack"
    elif score2 == 0:

        return "You lose... The computer got a blackjack"
    elif score1 > 21:
        return "You lose... Your score went over 21"
    elif score2 > 21:
        return "You win! The computer went over 21"
    else:
        return "You win! You have a higher score" if score1 > score2 else "You lose...The computer had a higher score"


def game():
    your_cards = []
    comp_cards = []
    game_over = False
    for _ in range(2):
        card = deal()
        your_cards.append(card)
    for _ in range(2):
        card = deal()
        comp_cards.append(card)

    while not game_over:

        your_score = calculate_score(your_cards)
        comp_score = calculate_score(comp_cards)

        print(f"Your cards are {your_cards} and your score is {sum(your_cards)}")
        print(f"Computer's first card is {comp_cards[0]}")
        if your_score == 0 or comp_score == 0 or your_score > 21:
            game_over = True
        else:
            ask = input("Would you like another card? Y/N ").upper()
            if ask == 'Y':
                your_cards.append(deal())
                your_score = calculate_score(your_cards)
            else:
                game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal())
        comp_score = calculate_score(comp_cards)

    print(f"Your final hand is {your_cards}, score: {sum(your_cards)}")
    print(f"Computer's final hand is {comp_cards}, score: {sum(comp_cards)}\n")

    print(compare(your_score, comp_score))


while input("Do you wanna play a game of Blackjack? Y/N ").upper() == "Y":
    system('CLS')
    print(logo)
    game()
