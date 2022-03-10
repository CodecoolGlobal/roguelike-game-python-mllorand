from time import sleep
import util
import engine
import ui
import levels
import gameitems

PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    return {"icon": gameitems.player_icon, "coord": (PLAYER_START_X, PLAYER_START_Y), "inventory": {}, "hp": 100}


def create_enemies():
    return {"icon":gameitems.enemy_icon, "coord": (3, 4)}


def main():
    player = create_player()
    enemies = create_enemies()
    # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    board = maps.create_level_one(BOARD_WIDTH, BOARD_HEIGHT)
    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        engine.put_enemies_on_board(board, enemies)
        ui.display_board(board)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        if key in ['w', 's', 'a', 'd']:
            engine.move_enemies(board, enemies)
            engine.move(board, player, key)
        if key == 'i':
            engine.print_table(player['inventory'])
            sleep(2)
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()
