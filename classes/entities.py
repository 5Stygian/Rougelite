class Player:
        def __init__(self, name, health, health_max, defense_flat, defense_nonflat, attack, equipped, inventory, xp, xp_req, level):
                self.name            = name
                self.health          = health
                self.health_max      = health_max
                self.defense_flat    = defense_flat
                self.defense_nonflat = defense_nonflat
                self.attack          = attack
                self.equipped        = equipped
                self.inventory       = inventory
                self.xp              = xp
                self.xp_req          = xp_req
                self.level           = level
        
        def attack(self):
                Enemy.health = Enemy.health - (self.attack - (Enemy.defense_flat * Enemy.defense_nonflat))

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
                
