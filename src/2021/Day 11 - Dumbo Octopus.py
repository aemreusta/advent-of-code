from typing import Iterator
import numpy as np

# Reading file
with open(r"advent_of_code\src\2021\Inputs\day11.txt") as f:
    data = [list(line.strip()) for line in f.readlines()]
f.close()


# Part 1 Solution
def neighbor_indices(matrix: np.ndarray, i: int, j: int) -> Iterator[tuple[int, int]]:

    for i_off in [-1, 0, 1]:
        for j_off in [-1, 0, 1]:
            i_new = i + i_off
            j_new = j + j_off

            if i == i_new and j == j_new:
                continue

            if (0 <= i_new < matrix.shape[0]) and (0 <= j_new < matrix.shape[1]):
                yield i_new, j_new


def stepper(matrix: np.ndarray) -> tuple[np.ndarray, int]:
    matrix += 1

    while (matrix > 9).any():
        for i, j in np.ndindex(*matrix.shape):
            if matrix[i, j] > 9:
                matrix[i, j] = np.nan

                for i_nbr, j_nbr in neighbor_indices(matrix, i, j):
                    matrix[i_nbr, j_nbr] += 1

    n_flashes = np.isnan(matrix).sum()
    matrix = np.nan_to_num(matrix)

    return matrix, n_flashes


total_flashes = 0
n_steps = 100

# Convert float to use np.nan
matrix = np.array(data, dtype=float)

for _ in range(n_steps):
    matrix, n_flashes = stepper(matrix)
    total_flashes += n_flashes

print(total_flashes)
# 1732

# Part 2 Solution
# Convert float to use np.nan
matrix = np.array(data, dtype=float)
total_steps = 0

while True:
    if matrix.sum() == 0:
        break

    matrix, _ = stepper(matrix)
    total_steps += 1

print(total_steps)
# 290
