lines = []
lines_2 = []
from itertools import product

# Only used and experimented with itertools.product from this video and then figured my way through to the solution after testing what itertools.product does
# https://www.youtube.com/watch?v=wRof9uV6GBA

# Parse
with open("./puzzle-inputs/07.txt") as f:
    lines = [l.replace("\n", "") for l in f.readlines()]

    for l in lines:
        lines_2.append([li.strip() for li in l.split(":")])

    for li in lines_2:
        li[0] = int(li[0])
        li[1] = [int(l) for l in li[1].split(" ")]

    lines = lines_2

def test(combo, test_value, nums):
    # combo is a tuple of "*" or "+" (times or plus)

    idx = 0
    ans = nums[idx]
    for instructions in combo:
        if instructions == "*":
            idx += 1
            ans *= nums[idx]
        elif instructions == "|":
            idx +=1
            ans = int(f"{ans}{nums[idx]}")
        else:
            idx +=1
            ans += nums[idx]

    return ans == test_value


correct = set()
for item in lines:
    test_value, nums = item

    # itertools.product goes through every permutation
    # example given "*+" and repeat of 2, it will permute every single combination
    # e.g.:
    # ('*', '*')
    # ('*', '+')
    # ('+', '*')
    # ('+', '+')

    for combo in product("*+|", repeat=len(nums)-1):
        # print(combo)
        if(test(combo, test_value, nums)):
            print(test_value, nums, combo)
            correct.add(test_value)

sum = 0

for num in correct:
    print(num)
    sum+=num

print(f"Correct: {sum}")
