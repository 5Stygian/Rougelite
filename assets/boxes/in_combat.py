from classes import *

player_name           = f"{player.name}\tLevel: {player.level} ({player.xp:,.2f}/{player.xp_req:,.2f})"
player_health_display = f"HP: {player.health:,.2f}/{player.health_max}"
player_defense        = f"{player.defense_flat * player.defense_nonflat}"
player_attack         = f"{player.attack:,.2f}"

enemy_name            = f"{enemy.name}"
enemy_health_display  = f"HP: {enemy.health:,.2f}/{enemy.health_max}"
enemy_defense         = f"{enemy.defense_flat * enemy.defense_nonflat}"
enemy_attack          = f"{enemy.attack:,.2f}"

in_combat_out = f"""
+--------------------------------------------------------------------------+
|     ______     ______     __    __     ______     ______     ______      |
|    /\  ___\   /\  __ \   /\ "-./  \   /\  == \   /\  __ \   /\__  _\     |
|    \ \ \____  \ \ \/\ \  \ \ \-./\ \  \ \  __<   \ \  __ \  \/_/\ \/     | 
|     \ \_____\  \ \_____\  \ \_\ \ \_\  \ \_____\  \ \_\ \_\    \ \_\     | 
|      \/_____/   \/_____/   \/_/  \/_/   \/_____/   \/_/\/_/     \/_/     | 
+--------------------------------------------------------------------------+
+-----------------------------------+  +-----------------------------------+
|{player_name:^35}|  |{enemy_name:^35}|
|{player_health_display:^35}|  |{enemy_health_display:^35}|
|{player_defense:^35}|  |{enemy_defense:^35}|
|{player_attack:^35}|  |{enemy_attack:^35}|
+-----------------------------------+  +-----------------------------------+
|{:^35}|  |{:^35}|
|{:^35}|  |{:^35}|
|{:^35}|  |{:^35}|
|{:^35}|  |{:^35}|
+-----------------------------------+  +-----------------------------------+"""
