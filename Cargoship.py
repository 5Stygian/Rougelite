class Cargoship:
        def read_file(PATH, START_LINE, END_LINE):
                with open(PATH, 'r') as file:
                        for i in range(START_LINE - 1, END_LINE):
                                print(file.readline())
        
        def print_box(NEW_LINE_COUNT, BOX_TO_PRINT):
               print('\n' * NEW_LINE_COUNT)
               print(f'{BOX_TO_PRINT}')

        def gate_or(arg1, arg2):
                if arg1 == True | arg2 == True:
                        return True
                else:
                        return False

        def gate_and(arg1, arg2):
                if arg1 == True & arg2 == True:
                        return True
                else:
                        return False

        def gate_not(arg):
                return not(arg)
