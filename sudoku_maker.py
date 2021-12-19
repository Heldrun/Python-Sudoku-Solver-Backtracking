from random import randint

def sudo_check(r,c,cell,digit):
    global l
    block=False
    column=False
    row=False
    #below checks 'blocks'
    if grid[r][c].count(digit)==0:
        block=True
    else:
        return(False)
    #below checks rows
    row_count=0
    if str(cell) in '012':
        mini_row = 0
    elif  str(cell) in '345':
        mini_row=1
    else:
        mini_row=2
    if mini_row == 0:
        for column in range(3):
            for position in range(3):
                if grid[r][column][position]==digit:
                    row_count+=1
    elif mini_row==1:
        for column in range(3):
            for position in range(3,6):
                if grid[r][column][position]==digit:
                    row_count+=1
    else:
        for column in range(3):
            for position in range(6,9):
                if grid[r][column][position]==digit:
                    row_count+=1
    if row_count==0:
        row=True
    else:
        return(False)
    # below checks columns
    column_count=0
    if str(cell) in '036':
        mini_column = 0
    elif  str(cell) in '147':
        mini_column=1
    else:
        mini_column=2
    if mini_column == 0:
        for array in range(3):
            for mini_row in range(0,7,+3):
                if grid[array][c][mini_row]==digit:
                    column_count+=1
    elif mini_column==1:
        for array in range(3):
            for mini_row in range(1,8,+3):
                if grid[array][c][mini_row]==digit:
                    column_count+=1
    else:
        for array in range(3):
            for mini_row in range(2,9,+3):
                if grid[array][c][mini_row]==digit:
                    column_count+=1
    if column_count==0:
        column=True
    if block==column==row==True:
        return(True)
    else:
        return(False)

        
    #####
def print_sudoku():
    for r in range(3):
        for digit in range(0,7,+3):
            print(grid[r][0][digit:digit+3],':',grid[r][1][digit:digit+3],':',grid[r][2][digit:digit+3])
        print('-'*50)
#         print()

cont=True    
while cont == True:
    grid=[[[0 for cell in range(9)]for c in range(3)]for r in range(3)]
    create_count=eval(input('How many cells are already completed?'))
    while create_count>0:
        r = randint(0,2)
        c = randint(0,2)
        cell=randint(0,8)
        if grid[r][c][cell]==0:
            digit = randint(1,9)
            if sudo_check(r,c,cell,digit)==True:
                grid[r][c][cell]=digit
                create_count-=1     
    print_sudoku()     
    prompt=input('continue(y/n)')
    if prompt=='n':
        cont=False
