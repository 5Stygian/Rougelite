import player as pla

class Enemy:
        def __init__(self, name, health, health_max, defense_flat, defense_nonflat, attack, ):
                self.name            = name
                self.health          = health
                self.health_max      = health_max
                self.defense_flat    = defense_flat
                self.defense_nonflat = defense_nonflat
                self.attack          = attack
        
        def attack(self):
                pla.health = pla.health - (self.attack - (pla.defense_flat * pla.defense_nonflat))
                
