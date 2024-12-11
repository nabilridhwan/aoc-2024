lines = []
lines_2 = []

# Parse
with open("./puzzle-inputs/07.txt") as f:
    lines = [l.replace("\n", "") for l in f.readlines()]

    for l in lines:
        lines_2.append([li.strip() for li in l.split(":")])

    for li in lines_2:
        li[0] = int(li[0])
        li[1] = [int(l) for l in li[1].split(" ")]

    lines = lines_2

for item in lines:
    test_value, nums = item