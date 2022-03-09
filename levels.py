from engine import create_board
from ui import display_board


def create_level_one(width, height):
    board = create_board(width=30, height=20)
    for i in range(width):
        for j in range(height):
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
    # board[5][4] = '💰'
    display_board(board)
    return board
    

def create_level_two(board):
    pass


def create_level_three(board):
    pass


create_level_one(width=30, height=20)
