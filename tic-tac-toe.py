
#board
board = ['','','','','','','','','']
#display board
def display_board(board):
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('---------')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('---------')
    print(f'{board[6]} | {board[7]} | {board[8]}')
def player_1():
    played = 1
    while played not in ['X', 'O']:
        played = input("Player 1 please choose 'X' or 'O' (capital): ")
#player_1()

