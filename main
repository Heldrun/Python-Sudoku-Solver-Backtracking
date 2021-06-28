def sudo_check(r,cell,digit):
    block=False
    column=False
    row=False
    #below checks 'blocks'
    block_check = 0
    if str(cell) in '012':
        block_c = 0
    elif  str(cell) in '345':
        block_c=3
    else:
        block_c=6
    if str(r) in '012':
        block_r = 0
    elif  str(r) in '345':
        block_r=3
    else:
        block_r=6
    for i in range(block_r, block_r+3):
        for j in range(block_c, block_c+3):
            if grid[i][j] == digit:
                block_check += 1
    if block_check == 0:
        block = True
    else:
        return(False)
    #below checks rows
    if grid[r].count(digit)==0:
        row = True
    else:
        return(False)
    # below checks columns
    column_count=0
    for r in grid:
        if r[cell ] == digit:
            column_count+=1 ####return here later, its likely that this can just be (return(False)), but check this version first
    if column_count == 0:
        column = True
    else:
        return(False)
    if block==column==row==True:
        return(True)
    else:
        return(False)
    
def print_sudoku():
    for r in grid:
        print(r)

grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0],
             [5, 2, 0, 0, 0, 0, 0, 0, 0],
             [0, 8, 7, 0, 0, 0, 0, 3, 1],
             [0, 0, 3, 0, 1, 0, 0, 8, 0],
             [9, 0, 0, 8, 6, 3, 0, 0, 5],
             [0, 5, 0, 0, 9, 0, 6, 0, 0], 
             [1, 3, 0, 0, 0, 0, 2, 5, 0],
             [0, 0, 0, 0, 0, 0, 0, 7, 4],
             [0, 0, 5, 2, 0, 6, 3, 0, 0] ]
# print_sudoku() # visualising initial grid in shell     
zero_index = []
solutions = []
for r in range(9):
    for cell in range(9):
        if grid[r][cell] == 0:
            zero_index.append((r, cell))

while len(solutions) != len(zero_index):
    #backtracking loop
    r = zero_index[len(solutions)][0]
    cell = zero_index[len(solutions)][1]
    if grid[r][cell] != 0:
        digit = grid[r][cell]+1
    else:
        digit = 1
    while True:
#         print(f'Current grid is {r}, {cell}. Current value is {digit}')#optional code for debugging puposes
        if digit == 10:
            grid[r][cell] = 0
            del solutions[-1]
            break
        if sudo_check(r,cell,digit)==True:
            grid[r][cell]=digit
            solutions.append(digit)
#             printing found and current solutions in shell #optional code for debugging puposes
#             for i in range (len(solutions)):
#                 print(f'{zero_index[i]} : {solutions[i]}')
#             print('_________')
            break
        else:
            digit+=1

print_sudoku() 
