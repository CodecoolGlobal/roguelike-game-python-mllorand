import model
import view
import util
from time import sleep
BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def main():
    # view.display_intro_screen(board=model.create_board(BOARD_WIDTH, BOARD_HEIGHT))
    board = model.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    model.create_valid_random_map(board, model.PLAYER_STARTING_COORDINATE, 20, 1, 10)
    is_running = True
    while is_running:
        util.clear_screen()
        model.put_player_on_board(board, model.PLAYER_ITEM)
        #model.put_enemies_on_board
        view.display_board(board)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        if key in ['w', 's', 'a', 'd']:
            #model.move_enemies(board, model.ENEMIES_ITEM)
            model.move(board, model.PLAYER_ITEM, key)
        if key == 'i':
            view.print_table(model.PLAYER_ITEM['inventory'])
            sleep(2)




if __name__ == '__main__':
    main()
