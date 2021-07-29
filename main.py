import math
import random
from graphics import *

NUM_CARDS = 11
NUM_SYMBOLS = 60
# COLORS = [(45, 186, 165), (186, 73, 45),(214, 58, 222),(167, 232, 201), (232, 180, 167), (223, 167, 232),(235, 2, 41)]
COLORS = []
for i in range(NUM_SYMBOLS):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    COLORS.append((r,g,b))

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
        # print(curr_card_symbols)
    
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
            # print(curr_card_symbols)
    
    #slope symbols
    curr_card_symbols = []
    for i in range(n**2, n**2+n+1):
        curr_card_symbols.append(i)
    curr_card = Card(card_id)
    curr_card.symbols = curr_card_symbols
    cards.append(curr_card)
    card_id += 1
    # print(curr_card_symbols)
    
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

def displayCards(card1,card2):
    # print("Displaying cards")
    window_size = 500
    num_symbols = len(card1.symbols)
    y_coords = [5*i for i in random.sample(range(0, 100), num_symbols)]
    # print("y_coords1: ", y_coords)
    y_coords = sorted(y_coords)
    prev_coords = (0,0)
    win = GraphWin("My window", window_size,window_size)
    win.setBackground(color_rgb(0,0,0))
    for i in range(num_symbols):
        if i == num_symbols - 1:
            rect = Rectangle(Point(0,prev_coords[1]),Point(window_size,window_size))
            rect.setFill(color_rgb(COLORS[card1.symbols[i]][0],COLORS[card1.symbols[i]][1],COLORS[card1.symbols[i]][2]))
            rect.draw(win)
        else:
            rect = Rectangle(Point(0,prev_coords[1]),Point(window_size,y_coords[i]))
            rect.setFill(color_rgb(COLORS[card1.symbols[i]][0],COLORS[card1.symbols[i]][1],COLORS[card1.symbols[i]][2]))
            rect.draw(win)
        prev_coords = (window_size,y_coords[i])
    
    y_coords2 = [5*i for i in random.sample(range(0, 100), num_symbols)]
    # print("y_coords2: ", y_coords2)
    y_coords2 = sorted(y_coords2)
    prev_coords = (0,0)
    win2 = GraphWin("My window2", window_size,window_size)
    win2.setBackground(color_rgb(0,0,0))
    for i in range(num_symbols):
        if i == num_symbols - 1:
            rect = Rectangle(Point(0,prev_coords[1]),Point(window_size,window_size))
            rect.setFill(color_rgb(COLORS[card2.symbols[i]][0],COLORS[card2.symbols[i]][1],COLORS[card2.symbols[i]][2]))
            rect.draw(win2)
        else:
            rect = Rectangle(Point(0,prev_coords[1]),Point(window_size,y_coords2[i]))
            rect.setFill(color_rgb(COLORS[card2.symbols[i]][0],COLORS[card2.symbols[i]][1],COLORS[card2.symbols[i]][2]))
            rect.draw(win2)
        prev_coords = (window_size,y_coords2[i])
    
    res1 = win.checkMouse()
    res2 = win2.checkMouse()
    while (not(res1 or res2)):
        res1 = win.checkMouse()
        res2 = win2.checkMouse()

    # print(res1,res2)
    
    ans = None
    if res1:
        y_coords.insert(0,0)
        y_coords.pop(len(y_coords)-1)
        i = 0
        while (i < len(y_coords) and (res1.y > y_coords[i])):
            print(res1.y, y_coords[i])
            i +=1
        ans = card1.symbols[i-1]
    elif res2:
        y_coords2.insert(0,0)
        y_coords.pop(len(y_coords)-1)
        i = 0
        while (i < len(y_coords)) and (res2.y > y_coords2[i]):
            i +=1
        ans = card2.symbols[i-1]
    
    print("selected ans: ", ans)


    win.close()
    win2.close()

    return ans




def play(all_cards, relationships):
    card1, card2 = pick_cards(all_cards)
    ans = displayCards(card1,card2)
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
    # win = GraphWin("My Circle", 100, 100)
    # c = Circle(Point(50,50), 10)
    # c.draw(win)
    # c = Circle(Point(100,100), 10)
    # c.draw(win)
    # rect = Rectangle(Point(0,0),Point(window_size,y_coords[i]))
    # rect.setFill(color_rgb(COLORS[card2.symbols[i]][0],COLORS[card2.symbols[i]][1],COLORS[card2.symbols[i]][2]))
    # rect.draw(win2)
    # win.getMouse() # Pause to view result
    # win.close()    # Close window when done

    # pt = Point(150,150)
    # cir = Circle(pt,50)
    # cir.setFill(color_rgb(100,255,50))
    # cir.draw(win)

    # win.getMouse()
    # win.close()

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