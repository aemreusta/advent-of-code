import numpy as np

# Reading file
with open(".\Inputs\day11.txt") as f:
    data = [line.strip() for line in f.readlines()]
f.close()

data = np.array(data, dtype=int)

# Part 1 Solution
print(data[0])
