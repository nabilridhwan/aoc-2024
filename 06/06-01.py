lines = []

# Separate rules and printing order
with open("./puzzle-inputs/06.txt") as f:
    lines = [[c for c in l.replace("\n", "")] for l in f.readlines()]


# Keep track of col and row and direction
curr_row = None
curr_col = None
curr_dir = 'up'
has_exit = False
visited_positions = set()

for line_idx in range(len(lines)):
    line = lines[line_idx]
    # print(line)
    for char_idx in range(len(line)):
        char = line[char_idx]

        if char == "^":
            curr_row = line_idx
            curr_col = char_idx

# print(curr_row, curr_col)

def check_dir(row,col,dir):
    if dir == "up":
        if lines[row-1][col] == "#":
            print("HELP")
            return "right"

        if row-1 <= 0:
            has_exit = True
            return dir
        
    if dir == "down":
        if lines[row+1][col] == "#":
            return "left"

        if row+1 >= len(lines):
            has_exit = True
            return dir



    if dir == "right":
        if lines[row][col+1] == "#":
            return "down"
        
        if col+1 >= len(lines[0]):
            has_exit = True
            return dir

    if dir == "left":
        if lines[row][col-1] == "#":
            return "up"

        if col-1 <= 0:
            has_exit = True
            return dir



    return dir

# Start game
while has_exit is False:

    curr_dir = check_dir(curr_row, curr_col, curr_dir)

    print(f'curr_dir {curr_dir}')

    has_exit = curr_row <= 0 or curr_row >= len(lines) or curr_col <= 0 or curr_col >= len(lines[0])

    if curr_dir == "up":
        curr_row -= 1
    elif curr_dir == "down":
        curr_row += 1
    elif curr_dir == "right":
        curr_col += 1
    else:
        curr_col -= 1

    visited_positions.add((curr_row, curr_col))
    print(curr_row, curr_col, curr_dir)
    print(f"visited positions {len(visited_positions)}")

