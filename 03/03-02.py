chars = ''
counter = 0
num_sum = 0
is_enabled = True

with open("./puzzle-inputs/03.txt") as f:
    chars = f.read()


while counter < len(chars)-3:
    print(chars[counter])
    # For each character, grab the next 4 character
    mul_range = chars[counter:counter+len("mul(")]
    do_range = chars[counter:counter+len("do()")]
    dont_range = chars[counter:counter+len("don't()")]

    # True if it is the start sequence of "mul("
    is_start_of_mul = mul_range == "mul("
    is_start_of_do = do_range== "do()"
    is_start_of_dont = dont_range == "don't()"

    print(f"mul: {is_start_of_mul} do: {is_start_of_do} dont: {is_start_of_dont}")

    # If it is the start of the sequence, check the following characters until you find a closing bracket
    # e.g. mul(4,5,6)
    # Start from "(" and end at ")"

    # start_num_range starts from counter + 4 because "mul(" is 4 characters
    start_num_range = counter+4
    end_num_range = -1

    if is_start_of_dont:
        # counter += so it does less iterations :)
        # happy interpreter, happy life
        counter += len("don't()")
        is_enabled = False
        continue;
    
    if is_start_of_do:
        # counter += so it does less iterations :)
        # happy interpreter, happy life
        counter += len("do()")
        is_enabled = True
        continue;

    if is_start_of_mul:
        # once again, counter +4 because "mul(" is 4 characters
        c = counter+4

        # while there isn't a end range
        while end_num_range == -1:
            char = chars[c]

            # Check if the current character and the supposedly start range of the numbers - 1 are the same. If they're the same, this means the previous OPENING BRACKET has no closing, hence "skip" this "found" iteration
            if char == "(" and chars[start_num_range-1] == "(":
                break
            elif char == ")":
                end_num_range = c
            
            # increment internal counter
            c += 1


        # full num string just uses the start and end range to capture a full num pair
        # e.g. (584,440)
        full_num_string = chars[start_num_range-1:end_num_range+1]

        # a quick check to see if there is anything in the full_num_string
        # because it can just be (#) or () or (,)
        # minimally, it has to have 5 characters
        # 2 brackets, 1 comma and 2 number
        if len(full_num_string) > 4 and is_enabled:
            # Separate the full_num_string
            # output: [584,440]
            nums = [int(n) for n in full_num_string.replace("(","").replace(")","").split(",")]

            # add the two numbers together
            num_sum += nums[0] * nums[1]

    counter += 1

print(num_sum)