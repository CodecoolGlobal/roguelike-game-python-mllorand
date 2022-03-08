from turtle import width


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
                board[i].append("▩")
            else:
                board[i].append(" ")
    for left_right in board:
        left_right[0] = "▩"
        left_right[-1] = "▩"
    return board

def put_player_on_board(board, player):
    x = player['coord'][0]
    y = player['coord'][1]
    icon = player['icon']
    board[x][y] = icon
