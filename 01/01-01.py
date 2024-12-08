sum = 0

left = []
right = []

with open("./puzzle-inputs/01-01.txt") as f:
    lines = f.readlines()

    for line in lines:
        numbers = [int(item.strip()) for item in line.replace("\n", "").split(" ") if len(item.strip()) > 0]
        left.append(numbers[0])
        right.append(numbers[1])

# sort left and right
left.sort()
right.sort()

for i in range(len(left)):
    sum += abs(left[i] - right[i])

print(sum)