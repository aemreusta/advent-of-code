import numpy as np

# Reading file
with open(r"advent_of_code\src\2021\Inputs\day7.txt") as f:
    data = [int(i) for i in f.read().strip().split(",")]
f.close()

# Part 1 Solution
steps = abs(data - np.median(data))
print(int(sum(steps)))
# 336120

# Part 2 Solution
data = np.array(data)
result = (
    np.abs(data - int(np.mean(data))) * (np.abs(data - int(np.mean(data))) + 1) // 2
)
print(np.sum(result))
# 96864235
