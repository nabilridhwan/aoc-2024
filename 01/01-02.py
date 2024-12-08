sum = 0

collection = {}

left = []
right = []

with open("./puzzle-inputs/01-01.txt") as f:
    contents = f.readlines()

    for i in range(len(contents)):
        numbers = [int(item.strip()) for item in contents[i].replace("\n", "").split(" ") if len(item.strip()) > 0]

        left.append(numbers[0])
        right.append(numbers[1])

# sort left and right
left.sort()
right.sort()


left_set = set(left)

for item in left_set:
    # Find the number of times it appears in the right list

    for i in range(len(right)):
        if item == right[i]:
            if item in collection:
                collection[item] += 1
            else:
                collection[item] = 1


for k,v in collection.items():
    sum += v * k

print(sum)