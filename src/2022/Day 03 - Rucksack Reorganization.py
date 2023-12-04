# Reading file
with open(r"advent_of_code\src\2022\Inputs\day3.txt") as f:
    data = [line.strip() for line in f]
f.close()

# Part 1 Solution
score = 0

for line in data:
    half_length = len(line) // 2

    first_half = line[0:half_length]
    second_half = line[half_length:]

    for i in first_half:
        if i in second_half:
            if i.isupper():
                score += ord(i) - 38

            else:
                score += ord(i) - 96

            break

print(score)
# 8139

# Part 2 Solution
score = 0

for l1 in range(0, len(data), 3):
    for i in data[l1]:
        if i in data[l1 + 1] and i in data[l1 + 2]:
            if i.isupper():
                score += ord(i) - 38

            else:
                score += ord(i) - 96

            break

print(score)
# 2668
