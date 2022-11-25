# Reading file
with open(r"advent_of_code\src\2021\Inputs\day5.txt") as f:
    data = [line.strip() for line in f.readlines()]
f.close()


def fuzzy_woozy(lines):
    result = 0
    map = [[0 for _ in range(1000)] for _ in range(1000)]
    # map[y][x] -> axis notation

    for line in lines:
        # line[x][y] -> axis notation
        if line[0][0] == line[1][0]:  # on the same x axis, increases the y axis
            for i in range(
                min(line[0][1], line[1][1]),
                min(line[0][1], line[1][1]) + abs(line[0][1] - line[1][1]) + 1,
            ):
                map[i][line[0][0]] += 1

        elif line[0][1] == line[1][1]:  # on the same y axes, increases the x axes
            for i in range(
                min(line[0][0], line[1][0]),
                min(line[0][0], line[1][0]) + abs(line[0][0] - line[1][0]) + 1,
            ):
                map[line[0][1]][i] += 1

        else:  # for diagonal lines
            xk = 1 if line[0][0] < line[1][0] else -1
            yk = 1 if line[0][1] < line[1][1] else -1
            for i in range(abs(line[0][0] - line[1][0]) + 1):
                map[line[0][1] + (yk * i)][line[0][0] + (xk * i)] += 1

    for x in range(1000):
        for y in range(1000):
            if map[x][y] > 1:
                result += 1

    print(result)


# Part 1 Solution
lines = [
    i
    for i in (
        [list(map(int, x.split(","))) for x in line.split(" -> ")] for line in data
    )
    if i[0][0] == i[1][0] or i[0][1] == i[1][1]
]
# call the function without diagonal point coordinates
fuzzy_woozy(lines)
# 7269

# Part 2 Solution
lines = [[list(map(int, x.split(","))) for x in line.split(" -> ")] for line in data]
# call the functions with all lines
fuzzy_woozy(lines)
# 21140
