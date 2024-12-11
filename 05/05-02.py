rules = []
printing_order = []

# Separate rules and printing order
with open("./puzzle-inputs/05.txt") as f:
    lines = [l.replace("\n", "") for l in f.readlines()]

    has_passed_newline = False

    for line in lines:

        if line.strip() == '':
            has_passed_newline = True
            continue

        if has_passed_newline == True:
            printing_order.append(line)
        else:
            rules.append(line)

rules = [[int(n) for n in r.split("|")] for r in rules]
printing_order = [[int (n) for n in po.split(",")] for po in printing_order]
incorrect_indexes = []

arr = []

# Go through each line
for line_index in range(len(printing_order[:])):
    line = printing_order[line_index]
    correct = True

    for num in line:
        
        for [a,b] in rules:
            # check if a is before num in the sequence
            num_index = line.index(num) if num in line else None

            if b == num:
                search_index = line.index(a) if a in line else None
                if search_index is None or num_index is None:
                    continue

                if search_index > num_index:
                    correct = False
            
            if a == num:
                search_index = line.index(a) if a in line else None

                if(num_index < search_index):
                    correct = False

    if not correct:
        incorrect_indexes.append(line_index)

for idx in incorrect_indexes[:]:
    line = printing_order[idx]

    my_rules = []
    nums = []

    # Filter out rules that is only applicable to the line
    for a, b in rules:
        if not (a in line or b in line):
            continue
        my_rules.append((a, b))

    # Bubble sort
    # Infinitely loop and check if i and i+1 is in the correct position
    # If it isn't. Swap and continue looping
    # It only breaks after is_sorted = True (or that line[i+1] and line[i] is not in my_rules)
    # https://www.youtube.com/watch?v=LA4RiCDPUlI

    while True:
        is_sorted = True

        for i in range(len(line)-1):
            print((line[i+1], line[i]) in my_rules)
            if (line[i+1], line[i]) in my_rules:
                is_sorted = False
                line[i], line[i+1] = line[i+1], line[i]


        if is_sorted:
            print(line)
            nums = line
            break

    arr.append(nums)


# Sum the middle number
sum = 0

import math

# Get the middle number
for v in range(len(arr)):

    middle_idx  = int(len(arr[v]) / 2)
    value = arr[v][middle_idx]

    print(value)

    sum += value

print(sum)