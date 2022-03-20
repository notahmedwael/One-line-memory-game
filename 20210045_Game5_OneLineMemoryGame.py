# This is a one line memory game made by python 3
# Author: Ahmed Wael Mohamed
# Version: 1.0

#Shuffling the positions of the list

import random
import time
num_list = ['1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0']
char_list = ["A", "B", "C", "D", "E", "F", "G","H", "I", "J"]*2
p1_score = 0
p2_score = 0
random.shuffle(char_list)
print(num_list)


def display_state():  # defining display state to print player 1, 2 scores respectively
    global p1_score
    global p2_score
    p1_score , p2_score = str(p1_score) , str(p2_score)
    print("[P1: " + p1_score + " / P2: " + p2_score + "]")\


def get_input(player):  # getting player input
    valid = False
    while not valid:
        msg = player + " Player enter your choice: "
        move = input(msg)
        if move.isdigit():
            move = int(move)
            if move <= 20:
                valid = True
    return move

def update_state(x,y):  # updating the lists, changing its values according to player performance, also adding a short delay
    global num_list
    global char_list
    global p1_score
    global p2_score
    origin_x = num_list[x]
    origin_y = num_list[y]
    num_list[x] = char_list[x]
    num_list[y] = char_list[y]
    if char_list[x] == char_list[y]:
        print(num_list)
        time.sleep(1)
        num_list[x], num_list[y] = "*","*"
        print(num_list)
        
    else:
        print(num_list)
        time.sleep(1)
        num_list[x], num_list[y] = origin_x, origin_y
        print(num_list)
        
def check_point(x):
    global num_list
    if num_list[x] == "*":
        return True

def end_game():  # defining functions to detect winner
    global p1_score
    global p2_score
    for i in num_list:
        if i.isdigit():
            valid = False
            break
        else:
            valid = True
    if valid == True:
        if p1_score > p2_score:
            p1_score , p2_score = str(p1_score) , str(p2_score)
            print("Player 1 Won, Congrats!" + " [P1: " + p1_score + " / P2: " + p2_score + "]")
        elif p1_score == p2_score:
            p1_score , p2_score = str(p1_score) , str(p2_score)
            print("It's Draw!" + " [P1: " + p1_score + " / P2: " + p2_score + "]")
        else:
            p1_score , p2_score = str(p1_score) , str(p2_score)
            print("Player 2 Won, Congrats!" + " [P1: " + p1_score + " / P2: " + p2_score + "]")
    return valid
            

while True:
    valid = False   # if no winner the game continues
    while not valid:
        x1 = get_input("First") - 1
        y1 = get_input("First") - 1
        if x1 != y1:
            valid = True
    update_state(x1,y1)
    if check_point(x1):
        p1_score = int(p1_score)
        p1_score += 1
    display_state()
    if end_game():
        break
    
    valid = False
    while not valid:
        x2 = get_input("Second") - 1
        y2 = get_input("Second") - 1
        if x2 != y2:
            valid = True    
    update_state(x2,y2)
    if check_point(x2):
        p2_score = int(p2_score)
        p2_score += 1
    display_state()
    if end_game():
        break
    