import math
import random

NUM_CARDS = 11
NUM_SYMBOLS = 55

class Card:
    def __init__(self, id):
        self.symbols = []
        self.id = id


class Game:
    def __init__(self):
        self.num_symbols = 55
        # self.num_unique_cards = (1 + math.sqrt(1 + 8*num_symbols)) / (2)
        self.num_unique_cards = 11

def get_all_cards():
    #make num_unique_cards cards
    elems = [i for i in range(NUM_SYMBOLS)]
    random.shuffle(elems)

    relationship_dic = {}
    card_dic = {}

    for i in range(NUM_CARDS):
        card_dic[i] = Card(i)
        for j in range(i):
            curr_symbol = elems.pop(0)
            relationship_dic[(i,j)] = curr_symbol
            card_dic[i].symbols.append(curr_symbol)
            card_dic[j].symbols.append(curr_symbol)
    return list(card_dic.values()), relationship_dic

def pick_cards(cards):
    num_cards = len(cards)
    #choose 2 cards:
    card1 = random.randint(0, num_cards-1)
    card2 = random.randint(0, num_cards-1)
    while (card2 == card1):
        card2 = random.randint(0, NUM_SYMBOLS)
    return cards[card1], cards[card2]


def play(all_cards, relationships):
    card1, card2 = pick_cards(all_cards)
    print("What is matching between these two?")
    print(card1.symbols)
    print(card2.symbols)
    print()
    answer = ""
    correct_answer = relationships[(max(card1.id, card2.id), min(card1.id, card2.id))]
    while answer == "" or int(answer) != int(correct_answer):
        answer = input()
        if int(answer) == int(correct_answer):
            print("Correct!")
        else:
            print("Wrong! Try again")


def main():
    print('Hello! Welcome to SpotNid! Hit enter when you are ready to play!')
    print("Ready? (Y/N)")
    score = 0
    answer = input()
    all_cards, relationships = get_all_cards()
    while answer == "Y":
        play(all_cards, relationships)
        score += 1
        print("Current Score:", score)
        print("Play again? (Y/N)")
        answer = input()


if __name__ == '__main__':
    main()