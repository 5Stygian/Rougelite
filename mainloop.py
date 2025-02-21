from assets.title import title_1
from assets.tutorial import tutorial_1, tutorial_2

input_ml = ''

# condenses the printing of boxes
# cs teacher said keeping the code as condensed as possible was a good thing 
def print_box(NEW_LINE_COUNT, BOX_TO_PRINT):
        print('\n' * NEW_LINE_COUNT)
        print(f'{BOX_TO_PRINT}')

def mainloop():
        global input_ml
        input_ml = ''

        # ==========================================================
        # title screen
        # ==========================================================
        print_box(100, title_1)
        input_ml = input('Input: '.lower().strip())
        if input_ml == "startup":
                print_box(100, title_1)
                input_ml = input('Input: '.lower().strip())
        elif not input_ml:
                input_ml = print('\n' + '(Invalid input)' + input('Input: '.lower().strip()) + '\n')

        # ==========================================================
        # tutorial
        # ==========================================================
        # finish later | reason: i need time to roleplay on c.ai
        while True:
                try: 
                        break
                except:
                        pass

        '''if input_ml == "tutorial" or input_ml == "0" or tutorial_input == "1":
                print_box(10, tutorial_1)
                tutorial_input = input('Input: '.lower().strip())
        elif tutorial_input == "2":
                print_box(10, tutorial_2)
                tutorial_input = input('Input: '.lower().strip())
        elif tutorial_input == "startup":
                mainloop()      
        elif not tutorial_input or not input_ml:
                tutorial_input = print('\n' + '(Invalid input)' + input('Input: '.lower().strip()) + '\n')'''

        # ==========================================================
        # play
        #==========================================================
        if input_ml == "play" or input_ml == "1":
                pass
        elif not input_ml:
                input_ml = print('\n' + '(Invalid input)' + input('Input: '.lower().strip()) + '\n')