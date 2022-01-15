import time, sys


SLEEP_TIME = 0.5

the_board = {"1" : "1", "2" : "2", "3" : "3",
             "4" : "4", "5" : "5", "6" : "6",
             "7" : "7", "8" : "8", "9" : "9"}


occupied_places = []


def print_board(board):
    time.sleep(SLEEP_TIME)
    print("Current board:")
    time.sleep(SLEEP_TIME)
    print(board['1'] + "|" + board['2'] + "|" + board["3"])
    print("-+-+-")
    print(board['4'] + "|" + board['5'] + "|" + board["6"])
    print("-+-+-")
    print(board['7'] + "|" + board['8'] + "|" + board["9"])
    print("-+-+-")

print("Player 1 is X and player 2 is O.")

while True:

    time.sleep(SLEEP_TIME)
    print_board(the_board)
    time.sleep(SLEEP_TIME)

    #PLAYER 1 TURN
    while True:
        print("Playe 1's turn.")
        player1_place = input("Place: ")
        if player1_place not in the_board.keys():
            print("Please type 1 to 9!")
            continue
        elif player1_place in occupied_places:
            print("This place is occupied. Try again.")
        else:
            occupied_places.append(player1_place)
            the_board[player1_place] = "X"
            break

    print_board(the_board)
    #PLAYER 2 TURN
    while True:
        print("Playe 2's turn.")
        player2_place = input("Place: ")
        if player2_place not in the_board.keys():
            print("Please type 1 to 9!")
            continue
        elif player2_place in occupied_places:
            print("This place is occupied. Try again.")
        else:
            occupied_places.append(player2_place)
            the_board[player2_place] = "O"
            break
