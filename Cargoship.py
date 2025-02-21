def read_file(PATH, START_LINE, END_LINE):
        with open(PATH, 'r') as file:
                for i in range(START_LINE - 1, END_LINE):
                        print(file.readline())