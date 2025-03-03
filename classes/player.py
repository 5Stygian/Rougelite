import enemies as enm

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
                enm.health = enm.health - (self.attack - (enm.defense_flat * enm.defense_nonflat))
