# Reading file
with open(r"advent_of_code\src\2022\Inputs\day4.txt") as f:
    data = [line.strip().split(",") for line in f]
f.close()

# Part 1 Solution
score = 0

for line in data:
    first_elf = [int(x) for x in line[0].split("-")]
    second_elf = [int(x) for x in line[1].split("-")]

    if first_elf[0] <= second_elf[0] and first_elf[1] >= second_elf[1]:
        score += 1

    elif first_elf[0] >= second_elf[0] and first_elf[1] <= second_elf[1]:
        score += 1

print(score)
# 494

# Part 2 Solution
score = 0

for line in data:
    first_elf = [int(x) for x in line[0].split("-")]
    second_elf = [int(x) for x in line[1].split("-")]

    for i in range(first_elf[0], first_elf[1] + 1):
        if i in range(second_elf[0], second_elf[1] + 1):
            score += 1
            break

print(score)
# 833
