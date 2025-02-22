from assets.title import title_1
from assets.tutorial import tutorial_1, tutorial_2

input_ml, tutorial_input = '', ''

# condenses the printing of boxes
# cs teacher said keeping the code as condensed as possible was a good thing 
def print_box(NEW_LINE_COUNT, BOX_TO_PRINT):
        print('\n' * NEW_LINE_COUNT)
        print(f'{BOX_TO_PRINT}')

def mainloop():
        # ==========================================================
        # variables
        # ==========================================================
        global input_ml, tutorial_input
        input_ml, tutorial_input = '', ''
        ts_il = True

        # ==========================================================
        # title screen
        # ==========================================================
        print_box(100, title_1)

        while ts_il: # title screen input loop
                try:
                        input_ml = input('Input: ').lower().strip()
                        ts_il = False
                except:
                        input_ml = input('Input: ').lower().strip()
        
        '''
        if input_ml == "startup":
                print_box(100, title_1)
                input_ml = input('Input: '.lower().strip())
        elif not input_ml:
                input_ml = print('\n' + '(Invalid input)' + input('Input: '.lower().strip()) + '\n')
        '''

        # ==========================================================
        # tutorial
        # ==========================================================
        # finish later | reason: i need time to roleplay on c.ai

        if input_ml == "tutorial" or input_ml == "0":
                match tutorial_input:
                        case "1":
                                print_box(10, tutorial_1)
                                tutorial_input = input('Input: ').lower().strip()
                        case "2":
                                print_box(10, tutorial_2)
                                tutorial_input = input('Input: ').lower().strip()
        
        '''                     
        if input_ml == "tutorial" or input_ml == "0" or tutorial_input == "1":
                while True:
                        try:    
                                print_box(10, tutorial_1)
                                tutorial_input = input('Input: '.lower().strip())
                                break
                        except:
                                tutorial_input = input('Input: '.lower().strip())
        
        elif tutorial_input == "2":
                while True:
                        try:    
                                print_box(10, tutorial_2)
                                tutorial_input = input('Input: '.lower().strip())
                                break
                        except:
                                tutorial_input = input('Input: '.lower().strip())
        
        elif tutorial_input == "startup":
                mainloop()
        '''

        # ==========================================================
        # play
        #==========================================================

        '''
        if input_ml == "play" or input_ml == "1":
                pass
        elif not input_ml:
                input_ml = print('\n' + '(Invalid input)' + input('Input: '.lower().strip()) + '\n')
        '''