class Player:
        def __init__(self, name, health, health_max, defense_flat, defense_nonflat, attack, xp, xp_req, level, equipped, inventory):
                self.name            = name
                self.health          = health
                self.health_max      = health_max
                self.defense_flat    = defense_flat
                self.defense_nonflat = defense_nonflat
                self.attack          = attack
                self.xp              = xp
                self.xp_req          = xp_req
                self.level           = level
                self.equipped        = {
                        "slot_1": ,
                        "slot_2": ,
                        "slot_3": ,
                        "slot_4": ,
                        "slot_mainhand": ,
                        "slot_offhand":
                }
                self.inventory       = inventory
        
        def attack(self):
                Enemy.health = Enemy.health - (self.attack - (Enemy.defense_flat * Enemy.defense_nonflat))

player = Player(
        "name", # Player name
        10,     # Health
        10,     # Maximum health
        1,      # Flat defense
        1,      # Nonflat defense
        1,      # Attack
        {},     # Equipped
        {},     # Inventory
        0,      # Xp
        100,    # Required xp
        1       # Level
        )

class Enemy:
        def __init__(self, name, health, health_max, defense_flat, defense_nonflat, attack):
                self.name            = name
                self.health          = health
                self.health_max      = health_max
                self.defense_flat    = defense_flat
                self.defense_nonflat = defense_nonflat
                self.attack          = attack
        
        def attack(self):
                Player.health = Player.health - (self.attack - (Player.defense_flat * Player.defense_nonflat))
                
