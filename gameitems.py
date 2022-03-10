import colorama
import icons
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

bomb_item = {'name': 'bomb', 'type': 'consumable', 'icon':icons.bomb_icon, 'effect': -25}
food_item = {'name': 'food', 'type': 'consumable', 'icon':icons.food_icon, 'effect': 25}
coin_item = {'name': 'coin', 'type': 'collectible', 'icon':icons.coin_icon}
knife_item = {'name': 'knife', 'type': 'collectible', 'icon':icons.knife_icon}
enemies_item = {'name': 'enemies', 'type': 'consumable', 'icon':icons.enemy_icon, 'effect': -25}

items = [bomb_item, food_item, coin_item, knife_item, enemies_item]
