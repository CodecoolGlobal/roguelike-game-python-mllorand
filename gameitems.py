import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# BOMB = '💣'
# KNIFE = '🔪'
# COIN = '💰'
# FOOD = '🍆'

bomb_item = {'name': 'bomb', 'type': 'consumable', 'icon':Fore.YELLOW + '☢' + Style.RESET_ALL, 'effect': -25}
food_item = {'name': 'food', 'type': 'consumable', 'icon':Fore.RED + '❤' + Style.RESET_ALL, 'effect': 25}
coin_item = {'name': 'coin', 'type': 'collectible', 'icon':Fore.GREEN + '€' + Style.RESET_ALL}
knife_item = {'name': 'knife', 'type': 'collectible', 'icon':Fore.BLUE + '➹' + Style.RESET_ALL}
enemies_item = {'name': 'enemies', 'type': 'consumable', 'icon':Fore.CYAN + '𓆗' + Style.RESET_ALL, 'effect': -25}
items = [bomb_item, food_item, coin_item, knife_item, enemies_item]
