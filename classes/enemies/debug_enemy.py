from entities import Enemy
from entities import player

DEBUG_ENEMY = Enemy(
        "DEBUG_ENEMY",
        10,
        10, 
        0,
        1,
        1
)

# Attack test
print(f"HP: {DEBUG_ENEMY.health}/{DEBUG_ENEMY.health_max}")
player.attack("DEBUG_ENEMY")
print(f"HP: {DEBUG_ENEMY.health}/{DEBUG_ENEMY.health_max}")
