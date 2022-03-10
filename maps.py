import random
from engine import create_board
from ui import display_board
import gameitems
import colorama
from time import sleep
from util import clear_screen
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def create_level_one(width, height):
    board = create_board(width=30, height=20)
    for i in range(height):
        for j in range(width):
            if i == 8 and j >= 6 and j < 16:
                board[i][j] = gameitems.wall_icon
            if i == 11 and j >= 1 and j < 18:
                board[i][j] = gameitems.wall_icon
            if j == 6 and i >= 2 and i < 9:
                board[i][j] = gameitems.wall_icon
            if i == 2 and j >= 6 and j < 16:
                board[i][j] = gameitems.wall_icon
            if j == 15 and i >= 4 and i < 9:
                board[i][j] = gameitems.wall_icon
            if i == 4 and j >= 8 and j < 15:
                board[i][j] = gameitems.wall_icon
            if j == 8 and i >= 5 and i < 7:
                board[i][j] = gameitems.wall_icon
            if i == 6 and j >= 8 and j < 14:
                board[i][j] = gameitems.wall_icon
            if j == 25 and i >= 2 and i < 5:
                board[i][j] = gameitems.wall_icon
            if i == 4 and j >= 26 and j < 28:
                board[i][j] = gameitems.wall_icon
            if j == 22 and i >= 2 and i < 14:
                board[i][j] = gameitems.wall_icon
            if i == 8 and j >= 23 and j < 29:
                board[i][j] = gameitems.wall_icon
            if i == 10 and j >= 23 and j < 28:
                board[i][j] = gameitems.wall_icon
            if i == 12 and j >= 24 and j < 29:
                board[i][j] = gameitems.wall_icon
            if i == 14 and j >= 22 and j < 28:
                board[i][j] = gameitems.wall_icon
            if j == 26 and i >= 4 and i < 7:
                board[i][j] = gameitems.wall_icon
            if i == 5 and j >= 1 and j < 3:
                board[i][j] = gameitems.wall_icon
            if i == 5 and j >= 4 and j < 6:
                board[i][j] = gameitems.wall_icon
            if i == 6 and j >= 17 and j < 18:
                board[i][j] = gameitems.wall_icon
            if i == 7 and j >= 16 and j < 17:
                board[i][j] = gameitems.wall_icon
            if i == 5 and j >= 18 and j < 19:
                board[i][j] = gameitems.wall_icon
            if i == 7 and j >= 19 and j < 20:
                board[i][j] = gameitems.wall_icon
            if i == 8 and j >= 20 and j < 21:
                board[i][j] = gameitems.wall_icon
            if i == 9 and j >= 21 and j < 22:
                board[i][j] = gameitems.wall_icon
            if j == 2 and i >= 13 and i < 19:
                board[i][j] = gameitems.wall_icon
            if j == 6 and i >= 13 and i < 19:
                board[i][j] = gameitems.wall_icon
            if j == 10 and i >= 13 and i < 19:
                board[i][j] = gameitems.wall_icon
            if j == 4 and i >= 12 and i < 18:
                board[i][j] = gameitems.wall_icon
            if j == 8 and i >= 12 and i < 18:
                board[i][j] = gameitems.wall_icon
            if j == 12 and i >= 12 and i < 18:
                board[i][j] = gameitems.wall_icon
            if j == 14 and i >= 13 and i < 18:
                board[i][j] = gameitems.wall_icon
            if j == 16 and i >= 12 and i < 15:
                board[i][j] = gameitems.wall_icon
            if j == 16 and i >= 16 and i < 19:
                board[i][j] = gameitems.wall_icon
            if i == 3 and j >= 19 and j < 20:
                board[i][j] = gameitems.wall_icon
            if i == 4 and j >= 20 and j < 21:
                board[i][j] = gameitems.wall_icon
            if i == 5 and j >= 21 and j < 22:
                board[i][j] = gameitems.wall_icon
            if i == 16 and j >= 17 and j < 18:
                board[i][j] = gameitems.wall_icon
            if i == 16 and j >= 19 and j < 22:
                board[i][j] = gameitems.wall_icon
            if j == 22 and i >= 14 and i < 17:
                board[i][j] = gameitems.wall_icon
            if j == 19 and i >= 17 and i < 18:
                board[i][j] = gameitems.wall_icon
            if j == 21 and i >= 18 and i < 19:
                board[i][j] = gameitems.wall_icon
            if j == 23 and i >= 14 and i < 18:
                board[i][j] = gameitems.wall_icon
            if j == 25 and i >= 14 and i < 16:
                board[i][j] = gameitems.wall_icon
            if j == 25 and i >= 17 and i < 19:
                board[i][j] = gameitems.wall_icon
            if j == 27 and i >= 14 and i < 18:
                board[i][j] = gameitems.wall_icon

    board[5][9] = gameitems.coin_item['icon']
    board[9][23] = gameitems.coin_item['icon']
    board[18][1] = gameitems.coin_item['icon']
    board[3][26] = gameitems.knife_item['icon']
    board[8][18] = gameitems.bomb_item['icon']
    board[15][24] = gameitems.bomb_item['icon']
    board[7][3] = gameitems.bomb_item['icon']
    board[15][13] = gameitems.bomb_item['icon']
    board[1][1] = gameitems.food_item['icon']
    board[7][23] = gameitems.food_item['icon']
    #  board[4][3] = gameitems.enemies_item['icon']

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
                    board[row][i] = gameitems.wall_icon
                break
            elif direction == 'vertical':
                for i in range(row, row + wall_length):
                    board[i][column] = gameitems.wall_icon
                break
        except IndexError:
            continue


def create_random_map(board, number_of_obstacles, min_size_of_obstacles, max_size_of_obstacles):
    coordinates_of_items = set()
    for _ in range(number_of_obstacles):
        create_obstacles(board, random.randint(min_size_of_obstacles, max_size_of_obstacles), random.choice(['vertical', 'horizontal']))
    for item in gameitems.items:
        row, column = random.randint(1, 18), random.randint(1, 28)
        while board[row][column] != ' ':
            row, column = random.randint(1, 18), random.randint(1, 28)
        board[row][column] = item['icon']
        coordinates_of_items.add((row, column))
    return coordinates_of_items


def validate_board(board, player_position, coordinates_of_items):
    reachable_coordinates = {player_position}
    already_checked_cooridnates = set()
    found_all_reachables = False
    while not found_all_reachables:
        new_reachable_coordinates = set()
        old_length_of_reachables = len(reachable_coordinates)
        for coordinate in reachable_coordinates.difference(already_checked_cooridnates):
            neighbours = get_neighbour_coordinates(coordinate)
            already_checked_cooridnates.add(coordinate)
            for neighbour in neighbours:
                row, column = neighbour
                try:
                    if board[row][column] != gameitems.wall_icon:
                        new_reachable_coordinates.add(neighbour)
                except IndexError:
                    continue
        reachable_coordinates.update(new_reachable_coordinates)
        new_length_of_reachables = len(reachable_coordinates)
        if new_length_of_reachables == old_length_of_reachables:
            found_all_reachables = True
    if coordinates_of_items.issubset(reachable_coordinates):
        return True
    else:
        return False


def get_neighbour_coordinates(coordinate):
    row, col = coordinate
    return [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]


def create_valid_random_map(board, player_coordinates, number_of_obstacles, min_length_of_obstacles, max_length_of_obstacles):
    while True:
        items_coordinates = create_random_map(board, number_of_obstacles, min_length_of_obstacles, max_length_of_obstacles)
        is_valid_board = validate_board(board, player_coordinates, items_coordinates)
        display_board(board)
        if is_valid_board:
            break


if __name__ == '__main__':
    while True:
            board = create_board(30, 20)
            items_coordinates = create_random_map(board, 20, 5, 15)
            is_valid_board = validate_board(board, (2, 2), items_coordinates)
            display_board(board)
            if is_valid_board:
                break
            sleep(1)
            clear_screen()
