from assets.title import title_1
from assets.tutorial import tutorial_1, tutorial_2

def startup():
        # title screen
        print('\n' * 100)
        print(f'{title_1}')
        startup_input = input('Input: ')

        # tutorial
        if startup_input == "tutorial" or startup_input == "0" or tutorial_input == "1":
                print(f'{tutorial_1}')
                tutorial_input = input('Input: ')
        if tutorial_input == "2":
                print(f'{tutorial_2}')
                tutorial_input = input('Input: ')