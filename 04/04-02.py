lines = []
line_index = 0
found = 0

found_indexes = []

with open("./puzzle-inputs/04.txt") as f:
    lines = [list(l.strip()) for l in f.readlines()]


while line_index < len(lines):
    line = lines[line_index]
    char_position = 0

    while char_position < len(line):

        c = line[char_position]

        # Anchor on A
        if c == 'A':

            if line_index < 1 or line_index >= len(lines) -1:
                char_position += 1
                continue
                
            if char_position < 1 or char_position >= len(line) - 1:
                char_position += 1
                continue

            # start search in X direction
            top_left = lines[line_index-1][char_position-1]
            top_right = lines[line_index-1][char_position+1]
            bottom_left = lines[line_index+1][char_position-1]
            bottom_right = lines[line_index + 1][char_position+1]

            # Pattern 1
            pattern_1 = top_left == "M" and top_right == "S" and bottom_left == "M" and bottom_right == "S"

            # Pattern 2
            pattern_2 = top_left == "S" and top_right == "S" and bottom_left == "M" and bottom_right == "M"

            # Pattern 3
            pattern_3 = top_left == "M" and top_right == "M" and bottom_left == "S" and bottom_right == "S"

            # Pattern 4
            pattern_4 = top_left == "S" and top_right == "M" and bottom_left == "S" and bottom_right == "M"

            if pattern_1 or pattern_2 or pattern_3 or pattern_4:
                found += 1

        char_position += 1

    line_index += 1


print(f"found {found}")