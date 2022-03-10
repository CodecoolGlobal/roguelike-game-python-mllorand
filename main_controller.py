import model
import view
import util
from time import sleep


def main():
    level = 0
    # view.display_intro_screen(board=model.create_board(model.BOARD_WIDTH, model.BOARD_HEIGHT))
    while True:
        level += 1
        model.PLAYER_ITEM['inventory'] = {}
        board = model.create_board(model.BOARD_WIDTH, model.BOARD_HEIGHT)
        model.create_valid_random_map(board, model.PLAYER_ITEM['coord'], model.BOARD_HEIGHT + model.BOARD_WIDTH + level, 1, 4)
        model.check_icons(board)
        while 'gate' not in model.PLAYER_ITEM['inventory']:
            util.clear_screen()
            view.display_board(board)
            key = util.key_pressed()
            if key == 'q':
                exit(1)
            if key in ['w', 's', 'a', 'd']:
                model.move_player(board, model.PLAYER_ITEM, key)
                for enemy in model.ENEMIES:
                    model.move_enemies(board, enemy)
                for movable_items in model.MOVABLE_ITEM:
                    model.put_movable_item_on_board(board, movable_items)
                if model.PLAYER_ITEM['coord'] == model.ENEMIES_ITEM_1['coord'] or model.PLAYER_ITEM['coord'] == model.ENEMIES_ITEM_2['coord'] or model.PLAYER_ITEM['coord'] == model.ENEMIES_ITEM_3['coord'] or model.PLAYER_ITEM['coord'] == model.ENEMIES_ITEM_4['coord'] or model.PLAYER_ITEM['hp'] <= 0:
                    print(f"You're dead now... you've made it to level {level}!")
                    sleep(3)
                    exit(1)
            if key == 'i':
                print(model.PLAYER_ITEM['inventory'], "\nHP: ", model.PLAYER_ITEM['hp'], "\nLEVEL: ", level)
                sleep(2)


if __name__ == '__main__':
    main()
