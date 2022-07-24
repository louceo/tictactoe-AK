# FUNCTION FOR 'X' INPUT
def x_user_input(grid): 
    global x_loc
    while True:
        print('')
        x_loc = str(input('Type in coordinates for "X" (COLUMN, ROW!) -> '))
        print('')
        x_loc = x_loc.replace(' ', '')
        x_loc = x_loc.replace(',', '')
        x_loc = list(map(int, x_loc))
        if grid[x_loc[1]][x_loc[0]] == 'x' or grid[x_loc[1]][x_loc[0]] == 'o':
            print('The square is already occupied. Try another one')
            continue
        break
    return x_loc
   
# FUNCTION FOR 'O' INPUT  
def o_user_input(grid):
    global o_loc
    while True:
        print('')
        o_loc = str(input('Type in coordinates for "O" (COLUMN, ROW!) -> '))
        print('')
        o_loc = o_loc.replace(' ', '')
        o_loc = o_loc.replace(',', '')
        o_loc = list(map(int, o_loc))
        if grid[o_loc[1]][o_loc[0]] == 'x' or grid[o_loc[1]][o_loc[0]] == 'o':
            print('The square is already occupied. Try another one')
            continue
        break
    return o_loc

# FUNCTIONS TO STORE VALUE IN GRID
def store_x_in_grid(x_loc, grid): 
    i = x_loc[0]
    j = x_loc[1]
    grid[j][i] = 'x'
    return grid

def store_o_in_grid(o_loc, grid): 
    i = o_loc[0]
    j = o_loc[1]
    grid[j][i] = 'o'
    return grid

# FUNCTION TO CHECK FOR GAMEOVER
def check_win(grid):
    #check diag manual
    if grid[0][0] == 'x' and grid[1][1] == 'x' and grid[2][2] == 'x':
        return True
    elif grid[0][0] == 'o' and grid[1][1] == 'o' and grid[2][2] == 'o':
        return True
    elif grid[0][2] == 'x' and grid[1][1] == 'x' and grid[2][0] == 'x':
        return True
    elif grid[0][2] == 'o' and grid[1][1] == 'o' and grid[2][0] == 'o':
        return True
    for i in range(len(grid)): 
        # row check 
        if grid[i][0] == 'x' and grid[i][1] == 'x' and grid[i][2] == 'x':
            return True
        elif grid[i][0] == 'o' and grid[i][1] == 'o' and grid[i][2] == 'o':
            return True
        for j in range(len(grid[i])):
             # col check
            if grid[0][j] == 'x' and grid[1][j] == 'x' and grid[2][j] == 'x':
                return True
            elif grid[0][j] == 'o' and grid[1][j] == 'o' and grid[2][j] == 'o':
                return True
    
# FUNCTION TO PRINT UI
def print_grid(grid):
    coord_ui_cnt = 0
    # print coord ui for COL
    coord_ui_col = [' ', 0, 1, 2]
    print('  '.join(map(str, coord_ui_col)))
    for e in grid:
        # add temp coord ui for ROW
        if len(e) < 4:
            e.insert(0, coord_ui_cnt)
        coord_ui_cnt += 1
        print('  '.join(map(str, e)))
    # remove temp coord ui for ROW
    for e in grid: 
        e.pop(0)

# CREATE GRID
grid = [['-']*3 for e in range(3)]

# MAIN 
print('')
print_grid(grid)
for cycle in range(1, 6):
    x_user_input(grid)
    store_x_in_grid(x_loc, grid)
    print_grid(grid)
    if check_win(grid):
        print('')
        print('GAME OVER!')
        print('')
        break
    if not check_win(grid) and cycle == 5: 
        print('')
        print('TIE!')
        print('')
        break
    o_user_input(grid)
    store_o_in_grid(o_loc, grid)
    print_grid(grid)
    if check_win(grid):
        print('')
        print('GAME OVER!')
        print('')
        break

    







