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


correct_indexes = []

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

    if correct:
        correct_indexes.append(line_index)

print(correct_indexes)

sum = 0

# Get the middle number
for v in correct_indexes:
    mi = int(len(printing_order[v])/2)
    value = printing_order[v][mi]

    sum += value

print(sum)