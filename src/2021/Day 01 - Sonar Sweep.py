# Reading file
with open(r"advent_of_code\src\2021\Inputs\day1.txt") as f:
    list = [int(line.strip()) for line in f.readlines()]
f.close()

# Part 1 Solution
count = 0

for i in range(1, len(list)):
    if list[i] > list[i - 1]:
        count += 1

print(count)

# Part 2 Solution
count = 0

for i in range(len(list)):
    if sum(list[i : i + 3]) < sum(list[(i + 1) : (i + 1) + 3]):
        count += 1

print(count)
