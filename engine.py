import random
import gameitems
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def create_board(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    board = []
    for i in range(height):
        board.append([])
        for j in range(width):
            if i == 0 or i == height - 1:
                board[i].append(gameitems.wall_icon)
            else:
                board[i].append(" ")
    for left_right in board:
        left_right[0] = gameitems.wall_icon
        left_right[-1] = gameitems.wall_icon
    return board


def print_table(inventory, order=None):
      first_column_width=max((len(max(inventory.keys(),key=len))),9)
      second_column_width=max(len(str(max(inventory.values()))),5)
      table_width=max(first_column_width+second_column_width+3,17)
      print("-"*table_width)
      print("item name".rjust(first_column_width)+" | "+"count".rjust(second_column_width))
      print("-"*table_width)
      if order=="count,asc":
            for i in sorted(inventory,key=inventory.get):
                  print(f"{i.rjust(first_column_width)} | {str(inventory.get(i)).rjust(second_column_width)}")
      elif order=="count,desc":
            for i in sorted(inventory,key=inventory.get,reverse=True):
                  print(f"{i.rjust(first_column_width)} | {str(inventory.get(i)).rjust(second_column_width)}")
      else:
            for i in inventory:
                  print(f"{i.rjust(first_column_width)} | {str(inventory.get(i)).rjust(second_column_width)}")
      print("-"*table_width)

def put_player_on_board(board, player):
    x = player['coord'][0]
    y = player['coord'][1]
    icon = player['icon']
    board[x][y] = icon


def item_check(move, board, player):
    for item in gameitems.items:
        if item['icon'] == board[move['coord'][0]][move['coord'][1]]:
            if item['type'] == 'consumable':
                event = {'hp': player['hp']+item['effect']}
                player.update(event)
            if item['type'] == 'collectible':
                if item['name'] in player['inventory']:
                    player['inventory'][item['name']] += 1
                else:
                    player['inventory'].setdefault(item['name'], 1)


def put_enemies_on_board(board, enemies):
    x = enemies['coord'][0]
    y = enemies['coord'][1]
    icon = enemies['icon']
    board[x][y] = icon


def move_enemies(board, enemies):
    keys = ['d', 'a', 'w', 's']
    key = random.choice(keys)
    board[enemies['coord'][0]][enemies['coord'][1]] = " "
    move = {'coord': (enemies['coord'][0], enemies['coord'][1])}
    if key == 'd':
        if board[enemies['coord'][0]][enemies['coord'][1] + 1] != gameitems.wall_icon:
            move = {'coord': (enemies['coord'][0], enemies['coord'][1] + 1)}
    if key == 'a':
        if board[enemies['coord'][0]][enemies['coord'][1] - 1] != gameitems.wall_icon:
            move = {'coord': (enemies['coord'][0], enemies['coord'][1] - 1)}
    if key == 'w':
        if board[enemies['coord'][0] - 1][enemies['coord'][1]] != gameitems.wall_icon:
            move = {'coord': (enemies['coord'][0] - 1, enemies['coord'][1])}
    if key == 's':
        if board[enemies['coord'][0] + 1][enemies['coord'][1]] != gameitems.wall_icon:
            move = {'coord': (enemies['coord'][0] + 1, enemies['coord'][1])}
    enemies.update(move)


def move(board, player, key):
    board[player['coord'][0]][player['coord'][1]] = " "
    move = {'coord': (player['coord'][0], player['coord'][1])}
    if key == 'd':
        if board[player['coord'][0]][player['coord'][1] + 1] != gameitems.wall_icon:
            move = {'coord': (player['coord'][0], player['coord'][1] + 1)}
    if key == 'a':
        if board[player['coord'][0]][player['coord'][1] - 1] != gameitems.wall_icon:
            move = {'coord': (player['coord'][0], player['coord'][1] - 1)}
    if key == 'w':
        if board[player['coord'][0] - 1][player['coord'][1]] != gameitems.wall_icon:
            move = {'coord': (player['coord'][0] - 1, player['coord'][1])}
    if key == 's':
        if board[player['coord'][0] + 1][player['coord'][1]] != gameitems.wall_icon:
            move = {'coord': (player['coord'][0] + 1, player['coord'][1])}
    if board[move['coord'][0]][move['coord'][1]] not in [' ', gameitems.wall_icon]:
        item_check(move, board, player)
    player.update(move)
