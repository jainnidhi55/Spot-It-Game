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

def get_all_cards(n):
    cards = []
    card_id = 0

    #vertical
    for col in range(n):
        curr_card_symbols = []
        for row in range(n):
            curr_card_symbols.append(n*row + col)
        curr_card_symbols.append(n*n + n)
        curr_card = Card(card_id)
        curr_card.symbols = curr_card_symbols
        cards.append(curr_card)
        card_id += 1
        print(curr_card_symbols)
    
    # print("A: ", len(cards))
    
    #slopes
    for slope in range(n):
        for padding in range(n):
            curr_card_symbols = []
            row = padding
            for col in range(n):
                # print("slope: %d, padding: %d, col:%d", slope, padding, col)
                curr_card_symbols.append(n*row+col)
                row = (row + slope) % n
            curr_card_symbols.append(n*n + slope)
            curr_card = Card(card_id)
            curr_card.symbols = curr_card_symbols
            cards.append(curr_card)
            card_id += 1
            print(curr_card_symbols)
    
    #slope symbols
    curr_card_symbols = []
    for i in range(n**2, n**2+n+1):
        curr_card_symbols.append(i)
    curr_card = Card(card_id)
    curr_card.symbols = curr_card_symbols
    cards.append(curr_card)
    card_id += 1
    print(curr_card_symbols)
    
    # print("B: ", len(cards))
    
    return cards,None






# def get_all_cards():
#     #make num_unique_cards cards
#     elems = [i for i in range(NUM_SYMBOLS)]
#     random.shuffle(elems)

#     relationship_dic = {}
#     card_dic = {}

#     for i in range(NUM_CARDS):
#         card_dic[i] = Card(i)
#         for j in range(i):
#             curr_symbol = elems.pop(0)
#             relationship_dic[(i,j)] = curr_symbol
#             card_dic[i].symbols.append(curr_symbol)
#             card_dic[j].symbols.append(curr_symbol)
#     return list(card_dic.values()), relationship_dic

def pick_cards(cards):
    num_cards = len(cards)
    #choose 2 cards:
    card1 = random.randint(0, num_cards-1)
    card2 = random.randint(0, num_cards-1)
    while (card2 == card1):
        card2 = random.randint(0, num_cards-1)
    return cards[card1], cards[card2]


def play(all_cards, relationships):
    card1, card2 = pick_cards(all_cards)
    print("What is matching between these two?")
    print(card1.symbols)
    print(card2.symbols)
    print()
    answer = ""
    # correct_answer = relationships[(max(card1.id, card2.id), min(card1.id, card2.id))]
    correct_answer = list(set(card1.symbols).intersection(set(card2.symbols)))[0]
    while answer == "" or int(answer) != int(correct_answer):
        answer = input()
        if int(answer) == int(correct_answer):
            print("Correct!")
        else:
            print("Wrong! Try again")


def main():
    print('Hello! Welcome to SpotNid!')
    print('How many symbols would you like per card? (2,3,4,6,8,12)?')
    num_symbols = input()
    while num_symbols not in ["2","3","4","6","8","12"]:
        print('Please enter an appropriate number: (2,3,4,6,8,12)')
        num_symbols = input()
    num_symbols = int(num_symbols)
    num_cards = (num_symbols-1)**2 + num_symbols
    print("We have a set of " + str(num_cards) + " cards. Ready? (Y/N)")
    score = 0
    answer = input()
    all_cards, relationships = get_all_cards(int(num_symbols)-1)
    while answer == "Y":
        play(all_cards, relationships)
        score += 1
        print("Current Score:", score)
        print("Play again? (Y/N)")
        answer = input()


if __name__ == '__main__':
    main()