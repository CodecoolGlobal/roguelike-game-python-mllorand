from engine import create_board
from ui import display_board


def create_level_one(width, height):
    board = create_board(width=30, height=20)
    for i in range(height):
        for j in range(width):
            if i == 8 and j >= 6 and j < 16:
                board[i][j] = "▩"
            if i == 11 and j >= 1 and j < 18:
                board[i][j] = "▩"
            if j == 6 and i >= 2 and i < 9:
                board[i][j] = "▩"
            if i == 2 and j >= 6 and j < 16:
                board[i][j] = "▩"
            if j == 15 and i >= 4 and i < 9:
                board[i][j] = "▩"
            if i == 4 and j >= 8 and j < 15:
                board[i][j] = "▩"
            if j == 8 and i >= 5 and i < 7:
                board[i][j] = "▩"
            if i == 6 and j >= 8 and j < 14:
                board[i][j] = "▩"
            if j == 25 and i >= 2 and i < 5:
                board[i][j] = "▩"
            if i == 4 and j >= 26 and j < 28:
                board[i][j] = "▩"
            if j == 22 and i >= 2 and i < 14:
                board[i][j] = "▩"
            if i == 8 and j >= 23 and j < 29:
                board[i][j] = "▩"
            if i == 10 and j >= 23 and j < 28:
                board[i][j] = "▩"
            if i == 12 and j >= 24 and j < 29:
                board[i][j] = "▩"
            if i == 14 and j >= 22 and j < 28:
                board[i][j] = "▩"
            if j == 26 and i >= 4 and i < 7:
                board[i][j] = "▩"
            if i == 5 and j >= 1 and j < 3:
                board[i][j] = "▩"
            if i == 5 and j >= 4 and j < 6:
                board[i][j] = "▩"
            if i == 6 and j >= 17 and j < 18:
                board[i][j] = "▩"
            if i == 7 and j >= 16 and j < 17:
                board[i][j] = "▩"
            if i == 5 and j >= 18 and j < 19:
                board[i][j] = "▩"
            if i == 7 and j >= 19 and j < 20:
                board[i][j] = "▩"
            if i == 8 and j >= 20 and j < 21:
                board[i][j] = "▩"
            if i == 9 and j >= 21 and j < 22:
                board[i][j] = "▩"
            if j == 2 and i >= 13 and i < 19:
                board[i][j] = "▩"
            if j == 6 and i >= 13 and i < 19:
                board[i][j] = "▩"
            if j == 10 and i >= 13 and i < 19:
                board[i][j] = "▩"
            if j == 4 and i >= 12 and i < 18:
                board[i][j] = "▩"
            if j == 8 and i >= 12 and i < 18:
                board[i][j] = "▩"
            if j == 12 and i >= 12 and i < 18:
                board[i][j] = "▩"
            if j == 14 and i >= 13 and i < 18:
                board[i][j] = "▩"
            if j == 16 and i >= 12 and i < 15:
                board[i][j] = "▩"
            if j == 16 and i >= 16 and i < 19:
                board[i][j] = "▩"
            if i == 3 and j >= 19 and j < 20:
                board[i][j] = "▩"
            if i == 4 and j >= 20 and j < 21:
                board[i][j] = "▩"
            if i == 5 and j >= 21 and j < 22:
                board[i][j] = "▩"
            if i == 16 and j >= 17 and j < 18:
                board[i][j] = "▩"
            if i == 16 and j >= 19 and j < 22:
                board[i][j] = "▩"
            if j == 22 and i >= 14 and i < 17:
                board[i][j] = "▩"
            if j == 19 and i >= 17 and i < 18:
                board[i][j] = "▩"
            if j == 21 and i >= 18 and i < 19:
                board[i][j] = "▩"
            if j == 23 and i >= 14 and i < 18:
                board[i][j] = "▩"
            if j == 25 and i >= 14 and i < 16:
                board[i][j] = "▩"
            if j == 25 and i >= 17 and i < 19:
                board[i][j] = "▩"
            if j == 27 and i >= 14 and i < 18:
                board[i][j] = "▩"
            
    board[5][9] = '💰'
    board[9][23] = '💰'
    board[18][1] = '💰'
    board[3][26] ='🔪'
    board[8][18] ='💣'
    board[15][24] ='💣'
    board[7][3] ='💣'
    board[15][13] ='💣'
    board[1][1] = '🍆'
    board[7][23] = '🍆'
    display_board(board)
    return board
    

def create_level_two(board):
    pass


def create_level_three(board):
    pass


create_level_one(width=30, height=20)
