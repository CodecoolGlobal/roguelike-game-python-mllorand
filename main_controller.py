import model
import view
import util
from time import sleep
BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def main():
    player = model.create_player()
    enemies = model.create_enemies()
    board = model.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    view.display_intro_screen(board)
    is_running = True
    while is_running:
        model.put_player_on_board(board, player)
        model.put_enemies_on_board(board, enemies)
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
