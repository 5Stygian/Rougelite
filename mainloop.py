from assets.title import title_1
from assets.tutorial import tutorial_1, tutorial_2
from classes.entities import Player
from classes.entities import Enemy

pla = Player(
        "name", # Player name
        10,     # Health
        10,     # Maximum health
        1,      # Flat defense
        1,      # Nonflat defense
        1,      # Attack
        0
        )

# condenses the printing of boxes
# cs teacher said keeping the code as condensed as possible was a good thing 
def print_box(NEW_LINE_COUNT, BOX_TO_PRINT):
        print('\n' * NEW_LINE_COUNT)
        print(f'{BOX_TO_PRINT}')

def mainloop():
        pass