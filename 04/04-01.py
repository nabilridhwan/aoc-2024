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

        if c == 'X':
            # start search on all 8 directions

            backward = None
            forward = line[char_position:char_position+4]
            up = None
            down = None
            diag_right_down = None
            diag_right_up = None
            diag_left_up = None
            diag_left_down = None

            if char_position >= 3:
                # can compute backward as there is enough space to go backwards
                backward = line[char_position-3:char_position+1]
            
            if line_index >= 3:
                # check up
                up = [
                    lines[line_index][char_position],
                    lines[line_index-1][char_position],
                    lines[line_index-2][char_position],
                    lines[line_index-3][char_position]
                ]


            if line_index <= len(lines) - 4:
                # check down
                down = [
                    lines[line_index][char_position],
                    lines[line_index+1][char_position],
                    lines[line_index+2][char_position],
                    lines[line_index+3][char_position]
                ]

            if line_index >= 3 and char_position <= len(line) - 4:
                diag_right_up = [
                    lines[line_index][char_position],
                    lines[line_index - 1][char_position+1],
                    lines[line_index - 2][char_position+2],
                    lines[line_index - 3][char_position+3],
                ]


            if line_index <= len(lines) - 4 and char_position <= len(line) - 4:
                diag_right_down = [
                    lines[line_index][char_position],
                    lines[line_index + 1][char_position+1],
                    lines[line_index + 2][char_position+2],
                    lines[line_index + 3][char_position+3],
                ]

            if line_index >= 3 and char_position >= 3:
                diag_left_up = [
                    lines[line_index][char_position],
                    lines[line_index - 1][char_position-1],
                    lines[line_index - 2][char_position-2],
                    lines[line_index - 3][char_position-3],
                ]
            
            if line_index <= len(lines) - 4 and char_position >=3:
                diag_left_down = [
                    lines[line_index][char_position],
                    lines[line_index + 1][char_position-1],
                    lines[line_index + 2][char_position-2],
                    lines[line_index + 3][char_position-3],
                ]
            


            print(f"forward {forward}")
            print(f"backward {backward}")
            print(f"up {up}")
            print(f"down {down}")

            print(f"diag_right_up {diag_right_up}")
            print(f"diag_right_down {diag_right_down}")

            print(f"diag_left_up {diag_left_up}")
            print(f"diag_left_down {diag_left_down}")

            if ''.join(forward) == "XMAS":
                found += 1

            if backward and (''.join(backward) == "XMAS" or ''.join(backward) == "SAMX"):
                found += 1

            if up and ("".join(up) == "XMAS" or "".join(up) == "SAMX"):
                found += 1

            if down and ("".join(down) == "XMAS" or "".join(down) == "SAMx"):
                found += 1

            if diag_right_up and ("".join(diag_right_up) == "XMAS" or "".join(diag_right_up) == "SAMX"):
                found += 1

            if diag_right_down and ("".join(diag_right_down) == "XMAS" or "".join(diag_right_down) == "SAMX"):
                found += 1

            if diag_left_up and ("".join(diag_left_up) == "XMAS" or "".join(diag_left_up) == "SAMX"):
                found += 1

            if diag_left_down and ("".join(diag_left_down) == "XMAS" or "".join(diag_left_down) == "SAMX"):
                found += 1

        char_position += 1
    print('---')
    print(f"found {found}")
    # print(found_indexes)
    print('---')
    line_index += 1