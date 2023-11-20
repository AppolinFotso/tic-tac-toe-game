
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

#Players input

def player1_input(letter):
    player1 = letter['player 1']
    player1_index = 10
    while player1_index not in range(0, 9):
        player1_index = int(input('player 1 please pick a slot on the board between 0-8: '))
        if player1_index not in range(0, 9):
            print('Please enter a valid number')

    player = [player1_index, player1]
    update_board_player1(player, letter)

def player2_input(letter):
    player2 = 2
    if letter['player 1'] == 'X':
        player2 = 'O'
    elif letter['player 1'] == 'O':
        player2 = 'X'
    player2_index = 20
    while player2_index not in range(0, 9):
        player2_index = int(input('player 2 please pick a slot on the board between 0-8: '))
        if player2_index not in range(0, 9):
            print('Please enter a valid number')

    player = [player2_index, player2]
    update_board_player2(player, letter)

#Players update
def update_board_player1(player, letter):
    if board[player[0]] == '':
        board[player[0]] = player[1]
    elif '' in board:
        player1_input(letter)
    else:
        display_board(board)

def update_board_player2(player, letter):
    if board[player[0]] == '':
        board[player[0]] = player[1]
    elif '' in board:
        player2_input(letter)
    else:
        display_board(board)

def play_the_game():
    display_board(board)
    player1_letter = letter_allocation()
    while '' in board:
        player1_input(player1_letter)
        player2_input(player1_letter)
        display_board(board)

play_the_game()