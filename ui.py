def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''   
    for i in range(len(board)):
        print(f"{' '.join(board[i])}")


def print_table(inventory, order=None):
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
