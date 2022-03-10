import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

wall_icon = Fore.BLUE + "▩" + Style.RESET_ALL
board_icon = ' '
player_icon = 'P'
enemy_icon = Fore.CYAN + 'E' + Style.RESET_ALL
bomb_icon = Fore.YELLOW + '☢' + Style.RESET_ALL
food_icon = Fore.RED + '❤' + Style.RESET_ALL
coin_icon = Fore.GREEN + '€' + Style.RESET_ALL
knife_icon = Fore.BLUE + '➹' + Style.RESET_ALL

bomb_item = {'name': 'bomb', 'type': 'consumable', 'icon':bomb_icon, 'effect': -25}
food_item = {'name': 'food', 'type': 'consumable', 'icon':food_icon, 'effect': 25}
coin_item = {'name': 'coin', 'type': 'collectible', 'icon':coin_icon}
knife_item = {'name': 'knife', 'type': 'collectible', 'icon':knife_icon}
enemies_item = {'name': 'enemies', 'type': 'consumable', 'icon':enemy_icon, 'effect': -25}

items = [bomb_item, food_item, coin_item, knife_item, enemies_item]
