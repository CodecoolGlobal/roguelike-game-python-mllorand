import util
import engine
import ui

BOMB = '💣'
KNIFE = '🔪'
COIN = '💰'
FOOD = '🍆'
PLAYER_ICON = '🕴️'
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
    return {"icon": PLAYER_ICON, "coord": (PLAYER_START_X, PLAYER_START_Y)}


def main():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        if key in ['w', 's', 'a', 'd']:
            engine.move(board, player, key)
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()
