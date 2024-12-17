lines = []

# Separate rules and printing order
with open("./puzzle-inputs/06.txt") as f:
    lines = [[c for c in l.replace("\n", "")] for l in f.readlines()]
    original_lines = [[c for c in l.replace("\n", "")] for l in f.readlines()]

init_row = None
init_col = None
init_dir = 'up'

# Keep track of col and row and direction
curr_row = None
curr_col = None
curr_dir = 'up'
has_exit = False
visited_positions = set()
turned_positions = set()

for line_idx in range(len(lines)):
    line = lines[line_idx]
    for char_idx in range(len(line)):
        char = line[char_idx]

        if char == "^":
            init_row = line_idx
            init_col = char_idx

            curr_row = line_idx
            curr_col = char_idx

def set_pos(row, col, dir = 'up'):
    global curr_row
    global curr_col
    global curr_dir

    curr_row = row
    curr_col = col
    curr_dir = dir

# returns new row, new col, new direction, has exit and is a turn
def move_player(row,col,dir):
    if dir == "up":
        if row-1 < 0:
            return [row,col,dir,True,False]
        else:
            if lines[row-1][col] == "#":
                return [row,col,"right",False,True]
            else:
                return [row-1,col,dir,False,False]

        
    if dir == "down":
        if row+1 >= len(lines):
            return [row,col,dir,True,False]
        else:
            if lines[row+1][col] == "#":
                return [row,col,"left",False,True]
            else:
                return [row+1,col,dir,False,False]



    if dir == "right":
        if col+1 >= len(lines[0]):
            return [row,col,dir,True,False]
        else:
            if lines[row][col+1] == "#":
                return [row,col,"down",False,True]
            else:
                return [row,col+1,dir,False,False]

    if dir == "left":
        if col-1 < 0:
            return [row,col,dir,True,False]
        else:
            if lines[row][col-1] == "#":
                return [row,col,"up",False,True]
            else:
                return [row,col-1,dir,False,False]

    return [row,col,dir,False,False]

def start_search():
    global has_exit
    global curr_row
    global curr_col
    global curr_dir

    visited_positions.add((init_row, init_col))

    # Start game
    while has_exit is False:
        new_row, new_col, new_dir, new_has_exit,is_turn = move_player(curr_row, curr_col, curr_dir)
        print(f'{new_row} {new_col} {new_dir} {new_has_exit}')
        set_pos(new_row, new_col, new_dir)
        has_exit = new_has_exit
        visited_positions.add((new_row, new_col))
        print(f"visited positions {len(visited_positions)}")

start_search()
# print(len(visited_positions))

confirmed_blockages_count = 0

for (row, col) in visited_positions:
    print(f"Simulating for ({row}, {col})")
    turned_positions = set()
    # Set the position to be a hash
    lines[row][col] = "#"

    # Reset player position
    set_pos(init_row,init_col,init_dir)

    # Try to start search
    is_loop = False
    inner_loop_count = 0

    while is_loop is False:
        n_row, n_col, n_dir, has_exit, is_turn = move_player(curr_row, curr_col, curr_dir)

        # Check if the inner loop count is more than 6 (threshold is 6)
        # i.e., If the player turned more than 6 times at the same turning point, consider it a loop
        if inner_loop_count >= 6:
            inner_loop_count = 0
            is_loop = True
            break

        # If there is an exit, break the loop
        if has_exit:
            break

        # If it is confirmed a turn
        if is_turn:
            # Check if the current row and col is in the turned positions
            if (n_row, n_col) in turned_positions:
                inner_loop_count += 1
            else:
                # If not, add it to turned positions
                turned_positions.add((n_row, n_col))

        # print(y,x,dir,exit)
        set_pos(n_row, n_col, n_dir)

    # If it is considered a loop
    # Make sure the valid number of blockages increase
    if is_loop:
        confirmed_blockages_count += 1
        print(f"Simulating passed for ({row}, {col})")
    else:
        print(f"Simulating failed. Found an exit")

    # Reset after every loop
    turned_positions = set()
    lines[row][col] = "."


    print(f"Confirmed Blockages Count: {confirmed_blockages_count}")
