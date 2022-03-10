from colorama import Fore, Style
import random

BOARD_WIDTH = 30
BOARD_HEIGHT = 20

PLAYER_STARTING_COORDINATE = BOARD_HEIGHT // 2, BOARD_WIDTH // 2

WALL_ICON = Fore.BLUE + "▩" + Style.RESET_ALL
BOARD_ICON = ' '
PLAYER_ICON = 'P'
ENEMY_ICON_1 = Fore.CYAN + 'E' + Style.RESET_ALL
ENEMY_ICON_2 = Fore.CYAN + 'V' + Style.RESET_ALL
ENEMY_ICON_3 = Fore.CYAN + 'I' + Style.RESET_ALL
ENEMY_ICON_4 = Fore.CYAN + 'L' + Style.RESET_ALL
BOMB_ICON = Fore.YELLOW + '☢' + Style.RESET_ALL
FOOD_ICON = Fore.RED + '❤' + Style.RESET_ALL
COIN_ICON = Fore.GREEN + '€' + Style.RESET_ALL
GATE_ICON = 'O'

BOMB_ITEM = {'name': 'bomb', 'type': 'consumable', 'icon': BOMB_ICON, 'effect': -25}
FOOD_ITEM = {'name': 'food', 'type': 'consumable', 'icon': FOOD_ICON, 'effect': 25}
COIN_ITEM = {'name': 'coin', 'type': 'collectible', 'icon': COIN_ICON}
ENEMIES_ITEM_1 = {'name': 'enemies', 'type': 'consumable', 'icon': ENEMY_ICON_1, 'effect': -100}
ENEMIES_ITEM_2 = {'name': 'enemies', 'type': 'consumable', 'icon': ENEMY_ICON_2, 'effect': -100}
ENEMIES_ITEM_3 = {'name': 'enemies', 'type': 'consumable', 'icon': ENEMY_ICON_3, 'effect': -100}
ENEMIES_ITEM_4 = {'name': 'enemies', 'type': 'consumable', 'icon': ENEMY_ICON_4, 'effect': -100}
PLAYER_ITEM = {'name': 'player', 'type': 'player', 'icon': PLAYER_ICON, 'coord': PLAYER_STARTING_COORDINATE, 'inventory': {}, 'hp': 100}
GATE_ITEM = {'name': 'gate', 'type': 'collectible', 'icon': GATE_ICON}

ITEMS = [BOMB_ITEM, FOOD_ITEM, COIN_ITEM, ENEMIES_ITEM_1, ENEMIES_ITEM_2, ENEMIES_ITEM_3, ENEMIES_ITEM_4, GATE_ITEM]


def create_board(width, height):
    board = []
    for i in range(height):
        board.append([])
        for j in range(width):
            if i == 0 or i == height - 1:
                board[i].append(WALL_ICON)
            else:
                board[i].append(" ")
    for left_right in board:
        left_right[0] = WALL_ICON
        left_right[-1] = WALL_ICON
    return board


def find_in_list_of_list(mylist, char):
    for sub_list in mylist:
        if char in sub_list:
            return (mylist.index(sub_list), sub_list.index(char))
    raise ValueError("'{char}' is not in list".format(char=char))


def put_player_on_board(board, player):
    x = player['coord'][0]
    y = player['coord'][1]
    icon = player['icon']
    board[x][y] = icon


def put_enemies_on_board(board, enemies):
    x = enemies['coord'][0]
    y = enemies['coord'][1]
    icon = enemies['icon']
    board[x][y] = icon


def item_check(move, board, player):
    for item in ITEMS:
        if item['icon'] == board[move['coord'][0]][move['coord'][1]]:
            if item['type'] == 'consumable':
                event = {'hp': player['hp']+item['effect']}
                player.update(event)
            if item['type'] == 'collectible':
                if item['name'] in player['inventory']:
                    player['inventory'][item['name']] += 1
                else:
                    player['inventory'].setdefault(item['name'], 1)


def move_enemies(board, enemies):
    keys = ['d', 'a', 'w', 's']
    key = random.choice(keys)
    board[enemies['coord'][0]][enemies['coord'][1]] = " "
    move = {'coord': (enemies['coord'][0], enemies['coord'][1])}
    if key == 'd':
        if board[enemies['coord'][0]][enemies['coord'][1] + 1] not in (WALL_ICON, GATE_ICON, COIN_ICON):
            move = {'coord': (enemies['coord'][0], enemies['coord'][1] + 1)}
    if key == 'a':
        if board[enemies['coord'][0]][enemies['coord'][1] - 1] not in (WALL_ICON, GATE_ICON, COIN_ICON):
            move = {'coord': (enemies['coord'][0], enemies['coord'][1] - 1)}
    if key == 'w':
        if board[enemies['coord'][0] - 1][enemies['coord'][1]] not in (WALL_ICON, GATE_ICON, COIN_ICON):
            move = {'coord': (enemies['coord'][0] - 1, enemies['coord'][1])}
    if key == 's':
        if board[enemies['coord'][0] + 1][enemies['coord'][1]] not in (WALL_ICON, GATE_ICON, COIN_ICON):
            move = {'coord': (enemies['coord'][0] + 1, enemies['coord'][1])}
    enemies.update(move)


def move(board, player, key):
    board[player['coord'][0]][player['coord'][1]] = " "
    move = {'coord': (player['coord'][0], player['coord'][1])}
    if 'coin' in player['inventory']:
        if key == 'd':
            if board[player['coord'][0]][player['coord'][1] + 1] != WALL_ICON:
                move = {'coord': (player['coord'][0], player['coord'][1] + 1)}
        if key == 'a':
            if board[player['coord'][0]][player['coord'][1] - 1] != WALL_ICON:
                move = {'coord': (player['coord'][0], player['coord'][1] - 1)}
        if key == 'w':
            if board[player['coord'][0] - 1][player['coord'][1]] != WALL_ICON:
                move = {'coord': (player['coord'][0] - 1, player['coord'][1])}
        if key == 's':
            if board[player['coord'][0] + 1][player['coord'][1]] != WALL_ICON:
                move = {'coord': (player['coord'][0] + 1, player['coord'][1])}
        if board[move['coord'][0]][move['coord'][1]] not in [' ', WALL_ICON]:
            item_check(move, board, player)
    else:
        if key == 'd':
            if board[player['coord'][0]][player['coord'][1] + 1] not in (WALL_ICON, GATE_ICON):
                move = {'coord': (player['coord'][0], player['coord'][1] + 1)}
        if key == 'a':
            if board[player['coord'][0]][player['coord'][1] - 1] not in (WALL_ICON, GATE_ICON):
                move = {'coord': (player['coord'][0], player['coord'][1] - 1)}
        if key == 'w':
            if board[player['coord'][0] - 1][player['coord'][1]] not in (WALL_ICON, GATE_ICON):
                move = {'coord': (player['coord'][0] - 1, player['coord'][1])}
        if key == 's':
            if board[player['coord'][0] + 1][player['coord'][1]] not in (WALL_ICON, GATE_ICON):
                move = {'coord': (player['coord'][0] + 1, player['coord'][1])}
        if board[move['coord'][0]][move['coord'][1]] not in [' ', WALL_ICON]:
            item_check(move, board, player)
    player.update(move)


def create_obstacles(board, wall_length, direction):
    while True:
        column = random.randint(1, BOARD_WIDTH-1)
        row = random.randint(1, BOARD_HEIGHT-1)
        try:
            if direction == 'horizontal':
                for i in range(column, column + wall_length):
                    board[row][i] = WALL_ICON
                break
            elif direction == 'vertical':
                for i in range(row, row + wall_length):
                    board[i][column] = WALL_ICON
                break
        except IndexError:
            continue


def create_random_map(board, number_of_obstacles, player_starting_coordinates, min_size_of_obstacles, max_size_of_obstacles):
    coordinates_of_items = set()
    for _ in range(number_of_obstacles):
        create_obstacles(board, random.randint(min_size_of_obstacles, max_size_of_obstacles), random.choice(['vertical', 'horizontal']))
    board[player_starting_coordinates[0]][player_starting_coordinates[1]] = PLAYER_ICON
    for item in ITEMS:
        row, column = random.randint(1, BOARD_HEIGHT-2), random.randint(1, BOARD_WIDTH-2)
        while board[row][column] != ' ':
            row, column = random.randint(1, BOARD_HEIGHT-2), random.randint(1, BOARD_WIDTH-2)
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
                    if board[row][column] != WALL_ICON:
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
        items_coordinates = create_random_map(board, number_of_obstacles, player_coordinates, min_length_of_obstacles, max_length_of_obstacles)
        is_valid_board = validate_board(board, player_coordinates, items_coordinates)
        if is_valid_board:
            break


def create_enemies():
    return {"icon": ENEMY_ICON, "coord": (3, 4)}
