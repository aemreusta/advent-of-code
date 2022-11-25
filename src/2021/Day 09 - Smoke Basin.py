import cv2
import numpy as np

# Reading file
with open(r"advent_of_code\src\2021\Inputs\day9.txt") as f:
    data = [line.strip() for line in f.readlines()]
f.close()

data = [list(map(int, list(s))) for s in data]

# Part 1 Solution
result = 0
# Adding 9 all side of the map
e_map = [[9] + i + [9] for i in [[9] * len(data[0])] + data + [[9] * len(data[0])]]
# Not add the 9 into loops
for row in range(1, len(e_map) - 1):
    for col in range(1, len(e_map[0]) - 1):
        if e_map[row][col] < min(
            e_map[row][col - 1],
            e_map[row - 1][col],
            e_map[row][col + 1],
            e_map[row + 1][col],
        ):
            result += e_map[row][col] + 1

print(result)
# 498

# Part 2 Solution
d = data
a = np.where(np.array(d) < 9, 255, 0).astype(np.uint8)
_, _, stats, _ = cv2.connectedComponentsWithStats(a, connectivity=4)

n = sorted([i[-1] for i in stats[1:]])[-3:]

result = n[0] * n[1] * n[2]
print(result)
# 1071000
