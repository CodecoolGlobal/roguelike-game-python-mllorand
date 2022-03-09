import random
from time import sleep
from engine import create_board
from ui import display_board
from util import clear_screen


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


def create_obstacles(board, wall_length, direction):
    while True:
        column = random.randint(1, 29)
        row = random.randint(1, 19)
        try:
            if direction == 'horizontal':
                for i in range(column, column + wall_length):
                    board[row][i] = "▩"
                break
            elif direction == 'vertical':
                for i in range(row, row + wall_length):
                    board[i][column] = "▩"
                break
        except IndexError:
            continue


def create_random_level(number_of_obstacles, min_size_of_obstacles, max_size_of_obstacles):
    for _ in range(number_of_obstacles):
        create_obstacles(board, random.randint(min_size_of_obstacles, max_size_of_obstacles), random.choice(['vertical', 'horizontal']))


while True:
    board = create_board(30, 20)
    create_random_level(10, 3, 12)
    display_board(board)
    sleep(1)
    clear_screen()





#create_level_one(width=30, height=20)
