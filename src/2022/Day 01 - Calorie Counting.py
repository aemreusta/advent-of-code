# Reading file
with open(r"advent_of_code\src\2022\Inputs\day1.txt") as f:
    data = [line.strip() for line in f]
f.close()

# Part 1 Solution
elves = []
total_calories = 0

# Iterate over the data and keep track of the total number of Calories for each Elf
for calories in data:
    # If we encounter a blank line, start a new Elf
    if calories != "":
        total_calories += int(calories)

    else:
        elves.append(total_calories)
        total_calories = 0

print(max(elves))
# 72070

# Part 2 Solution
elves.sort()
total = sum(elves[-3:])
print(total)
# 211805
