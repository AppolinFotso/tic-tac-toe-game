
#board
board = ['', '', '', '', '', '', '', '', '']
#display board
def display_board(board):
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('---------')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('---------')
    print(f'{board[6]} | {board[7]} | {board[8]}')
#Player 1
def letter_allocation():
    chosen1 = 'not yet'
    chosen2 = 'not yet'
    while chosen1 not in ['X', 'O']:
        chosen1 = input("Player 1 please choose 'X' or 'O' (capital): ")
        if chosen1 == 'X':
            chosen2 = 'O'
            print('Player 1 is "X"')
            print('Player 2 is "O"')
            print('Start Playing now!')
        elif chosen1 == 'O':
            chosen2 = 'X'
            print('Player 1 is "O"')
            print('Player 2 is "X"')
            print('Start Playing now!')
        else:
            print('Wrong letter!')
    return {"player 1": chosen1, "player 2": chosen2}

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
    player2 = letter['player 2']
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


def update_board_player2(player, letter):
    if board[player[0]] == '':
        board[player[0]] = player[1]
    elif '' in board:
        player2_input(letter)

#check for win, loss, tie
def win_lost_tie(board, letter):
    if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8]:
        if letter['player 1'] == board[0] == board[1] == board[2] or letter['player 1'] == board[3] == board[4] == board[5] or letter['player 1'] == board[6] == board[7] == board[8]:
            print('''
           ----------------
           | Player 1 won |
           ----------------
           | Player 2 lost|
           -----------------
                            ''')

            return 'won'
        elif letter['player 2'] == board[0] == board[1] == board[2] or letter['player 2'] == board[3] == board[4] == board[5] or letter['player 2'] == board[6] == board[7] == board[8]:
            print('''
           ----------------
           | Player 2 won |
           ----------------
           | Player 1 lost|
           -----------------
                            ''')

            return 'won'

    elif board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8]:
            if letter['player 1'] == board[0] == board[3] == board[6] or letter['player 1'] == board[1] == board[4] == board[7] or letter['player 1'] == board[2] == board[5] == board[8]:
                print('''
               ----------------
               | Player 1 won |
               ----------------
               | Player 2 lost|
               -----------------
                                ''')

                return 'won'

            elif letter['player 2'] == board[0] == board[3] == board[6] or letter['player 2'] == board[1] == board[4] == board[7] or letter['player 2'] == board[2] == board[5] == board[8]:
                print('''
               ----------------
               | Player 2 won |
               ----------------
               | Player 1 lost|
               -----------------
                                 ''')

                return 'won'

    elif board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
            if letter['player 1'] == board[0] == board[4] == board[8] or letter['player 1'] == board[2] == board[4] == board[6]:
                print('''
                ----------------
                | Player 1 won |
                ----------------
                | Player 2 lost|
                -----------------
                                ''')

                return 'won'

            elif letter['player 2'] == board[0] == board[4] == board[8] or letter['player 2'] == board[2] == board[4] == board[6]:
                print('''
                ----------------
                | Player 2 won |
                ----------------
                | Player 1 lost|
                -----------------
                ''')
                return 'won'


#play the game
def play_the_game():
    display_board(board)
    player1_letter = letter_allocation()
    game = True
    while game:
        player1_input(player1_letter)
        check_win_player1 = win_lost_tie(board, player1_letter)
        if check_win_player1 == 'won':
            display_board(board)
            play_again()
            break
        player2_input(player1_letter)
        check_win_player2 = win_lost_tie(board, player1_letter)
        if check_win_player2 == 'won':
            display_board(board)
            play_again()
            break
        display_board(board)

# Play again
def play_again():
    question = input('Would you like to play again yes/no: ')
    if question == 'no' or question == 'n':
        pass
    elif question == 'yes' or question == 'y':
        global board
        board = ['', '', '', '', '', '', '', '', '']
        play_the_game()
####
play_the_game()