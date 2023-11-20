
#board
board = ['','','','','','','','','']
#display board
def display_board(board):
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('---------')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('---------')
    print(f'{board[6]} | {board[7]} | {board[8]}')
#Player 1
def letter_allocation():
    chosen = 'not yet'
    while chosen not in ['X', 'O']:
        chosen = input("Player 1 please choose 'X' or 'O' (capital): ")
        if chosen == 'X':
            print('Player 1 is "X"')
            print('Player 2 is "O"')
            print('Start Playing now!')
        elif chosen == 'O':
            print('Player 1 is "O"')
            print('Player 2 is "X"')
            print('Start Playing now!')
        else:
            print('Wrong letter!')
    return {"player 1": chosen}

#User input

chosen_letter = letter_allocation()

def player1_input():
    player1 = 1
    player1_index = 10
    chosen = chosen_letter
    while player1_index not in range(0, 9):
        player1_index = int(input('player 1 please pick a slot on the board between 0-8: '))
        if player1_index not in range(0, 9):
            print('Please enter a valid number')

    return [player1_index, player1]

def player2_input():
    player2 = 2
    player2_index = 20
    chosen = chosen_letter
    while player2_index not in range(0, 9):
        player2_index = int(input('player 2 please pick a slot on the board between 0-8: '))
        if player2_index not in range(0, 9):
            print('Please enter a valid number')

    return [player2_index, player2]


player1_input()
player2_input()