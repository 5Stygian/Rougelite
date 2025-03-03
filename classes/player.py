import enemies as enm

class Player:
        def __init__(self, health, health_max, defense_flat, defense_nonflat, attack, name):
                self.health          = health
                self.health_max      = health_max
                self.defense_flat    = defense_flat
                self.defense_nonflat = defense_nonflat
                self.attack          = attack
                self.name            = name
        
        def attack(self):
                enm.health = enm.health - (self.attack - (enm.defense_flat * enm.defense_nonflat))
