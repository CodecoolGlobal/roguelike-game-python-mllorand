from engine import create_board
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


if __name__ == '__main__':
    BOARD_WIDTH = 30
    BOARD_HEIGHT = 20
    board = create_board(BOARD_WIDTH, BOARD_HEIGHT)
    display_intro_screen(board)
