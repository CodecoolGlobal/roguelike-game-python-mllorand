from util import clear_screen
from time import sleep
DELAY_SEC = 0.3
TEXT_1ST_LINE = "WELCOME"
START_1ST_LINE = (5, 12)
TEXT_2ND_LINE = "IN OUR CRAZY"
START_2ND_LINE = (8, 9)
TEXT_3RD_LINE = "WORLD"
START_3RD_LINE = (11, 13)
TEXT_4TH_LINE = '❤' * 5
START_4TH_LINE = (14, 13)


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
    text_1st_line = display_text_within_board(board, TEXT_1ST_LINE, START_1ST_LINE)
    clear_screen()
    text_2nd_line = display_text_within_board(text_1st_line, TEXT_2ND_LINE, START_2ND_LINE)
    clear_screen()
    text_3rd_line = display_text_within_board(text_2nd_line, TEXT_3RD_LINE, START_3RD_LINE)
    clear_screen()
    display_text_within_board(text_3rd_line, TEXT_4TH_LINE, START_4TH_LINE)
    print()
    input("Press Enter to continue...")


def display_board(board):
    for i in range(len(board)):
        print(f"{' '.join(board[i])}")


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
