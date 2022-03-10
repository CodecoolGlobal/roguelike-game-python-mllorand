import model
import view
import util
from time import sleep
BOARD_WIDTH = 30
BOARD_HEIGHT = 20
PLAYER_STARTING_COORDINATE = 10, 15



def main():
    enemies = model.create_enemies()
    # view.display_intro_screen(board=model.create_board(BOARD_WIDTH, BOARD_HEIGHT))
    board = model.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    model.create_valid_random_map(board, PLAYER_STARTING_COORDINATE, 20, 1, 10)
    view.display_board(board)
    key = util.key_pressed()
    if key == 'q':
        is_running = False
    if key in ['w', 's', 'a', 'd']:
        model.move_enemies(board, enemies)
        model.move(board, player, key)
    if key == 'i':
        view.print_table(player['inventory'])
        sleep(2)
    else:
        pass
    util.clear_screen()



if __name__ == '__main__':
    main()
