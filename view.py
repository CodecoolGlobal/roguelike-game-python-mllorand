from util import clear_screen
from time import sleep

DELAY_SEC = 0.2
INTRO_1ST_LINE = "ENTER"
START_1ST_LINE = (5, 12)
INTRO_2ND_LINE = "TO THE WORLD"
START_2ND_LINE = (8, 9)
INTRO_3RD_LINE = "OF EVILS"
START_3RD_LINE = (11, 11)
INTRO_4TH_LINE = '❤' * 9
START_4TH_LINE = (14, 10)
AUTHORS = ["AUTHORS", "RANDOM MAP: ANDRIS", "SILENT DROID: DANI", "ENTHUSIAST: LÓRI", "HEART: TOMI", "CSICSA: VANDA", "ENUMERATE: ZÉNÓ", "REDUNDANT: KATALIN", "EXTRAS: BENCE, FERENC"]
MOVING_LINES = 10


def display_text_within_board(board, text, start_text):
    for i_text in range(len(text)):
        for i_board in range(len(board)):
            print(f"{' '.join(board[i_board])}")
            if i_board == start_text[0]:
                board[start_text[0]][start_text[1]+i_text] = text[i_text]
                print("\033[A\033[A")
                print(f"{' '.join(board[start_text[0]])}")
        sleep(DELAY_SEC)
        if i_text != len(text) - 1:
            clear_screen()
    return board


def display_intro_screen(board):
    clear_screen()
    print()
    text_1st_line = display_text_within_board(board, INTRO_1ST_LINE, START_1ST_LINE)
    clear_screen()
    text_2nd_line = display_text_within_board(text_1st_line, INTRO_2ND_LINE, START_2ND_LINE)
    clear_screen()
    text_3rd_line = display_text_within_board(text_2nd_line, INTRO_3RD_LINE, START_3RD_LINE)
    clear_screen()
    display_text_within_board(text_3rd_line, INTRO_4TH_LINE, START_4TH_LINE)
    print()
    input("Press Enter to continue...")


def display_authors(text):
    for i_text in range(1, len(text)):
        prints = MOVING_LINES
        for _ in range(prints):
            for word in text[:i_text]:
                print(word.center(40))
            for _ in range(prints):
                print()
            print(text[i_text].center(40))
            sleep(DELAY_SEC)
            clear_screen()
            prints -= 1
    for word in text:
        print(word.center(40))
    print()


def display_board(board):
    for i in range(len(board)):
        print(f"{' '.join(board[i])}")


def print_table(inventory, order=None):
    if inventory == {}: return print("Empty backpack")
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


def display_player_inventory(inventory, order=None):
    if order == 'count,asc':
        inventory = sorted(inventory.items(), key=lambda kv: kv[1])
    elif order == 'count,desc':
        inventory = sorted(inventory.items(), key=lambda kv: kv[1], reverse=True)
    else:
        inventory = inventory.items()
    print(f"{'-----------------'}\n"
          f"{'item name | count'}\n"
          f"{'-----------------'}")
    for kv in inventory:
        print(f"{kv[0]:>9} | {kv[1]:>5}")
    print('-----------------')


if __name__ == '__main__':
    # board = model.create_board(model.BOARD_WIDTH, model.BOARD_HEIGHT)
    # display_intro_screen(board)
    display_authors(AUTHORS)
