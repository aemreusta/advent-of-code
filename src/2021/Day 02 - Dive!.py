# Reading file
with open(r"advent_of_code\src\2021\Inputs\day2.txt") as f:
    list = [line.strip().split(" ") for line in f.readlines()]
f.close()

# Part 1 Solution
depth, horizontal = 0, 0

for command, value in list:
    if command == "forward":
        horizontal += int(value)

    elif command == "down":
        depth += int(value)

    elif command == "up":
        depth -= int(value)

print(horizontal * depth)

# Part 2 Solution
depth, horizontal, aim = 0, 0, 0

for command, value in list:
    if command == "forward":
        horizontal += int(value)
        depth += int(value) * aim

    elif command == "down":
        aim += int(value)

    elif command == "up":
        aim -= int(value)

print(horizontal * depth)
