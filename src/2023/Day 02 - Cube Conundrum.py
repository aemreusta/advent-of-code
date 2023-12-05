import re

# Reading file
with open("src/2023/Inputs/day2.txt") as f:
    data = [line.strip() for line in f.readlines()]
f.close()

# Part 1 Solution
color_pattern = r"(\d+) (\w+)"
total_game = 0
max_colors = {"red": 12, "blue": 14, "green": 13}

for game, line in enumerate(data):
    colors = re.findall(color_pattern, line)

    valid = True
    for color in colors:
        if max_colors[color[1]] < int(color[0]):
            valid = False
            break

    if valid:
        total_game += game + 1

print(total_game)
# 2285

# Part 2 Solution
total_power = 0

for game, line in enumerate(data):
    colors = re.findall(color_pattern, line)

    min_colors = {"red": 0, "blue": 0, "green": 0}

    for color in colors:
        if min_colors[color[1]] < int(color[0]):
            min_colors[color[1]] = int(color[0])

    min_power = min_colors["red"] * min_colors["blue"] * min_colors["green"]
    total_power += min_power

print(total_power)
# 77021
