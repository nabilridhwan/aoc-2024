converted_lines = []
safe_reports = 0

def check_line(line: str):
    safe = True
    direction = []

    ptr_1 = 0
    ptr_2 = 1

    while ptr_2 <= len(line)-1:

        num_1 = line[ptr_1]
        num_2 = line[ptr_2]

        # print(f"{num_1} {num_2}")

        if num_2 - num_1 < 0:
            # Number is negative
            direction.append(-1)
        elif num_2 - num_1 > 0:
            # Number is positive
            direction.append(1)

        abs_value = abs(num_2-num_1)

        if abs_value > 3 or abs_value == 0:
            safe = False

        if(len(set(direction)) > 1):
            safe = False

        ptr_1 += 1
        ptr_2 += 1

    return safe



# Read lines and convert each line into 2d array of numbers
with open('./puzzle-inputs/02.txt', 'r') as f:
    lines = f.readlines()
    converted_lines = [[int(str_num) for str_num in line.replace("\n", "").split(" ")] for line in lines]

for i in range(len(converted_lines[:])):
    line = converted_lines[i]

    safe = check_line(line)
    print(safe)

    if safe:
        safe_reports +=1



print(f"safe_reports {safe_reports}")