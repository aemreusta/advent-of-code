import argparse
import time


# Part 1 Solution
def part_one_solution(data):
    part_sum = 0

    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == "O":
                data[y][x] = "."
                i = y - 1
                while i >= 0 and data[i][x] == ".":
                    i -= 1
                data[i + 1][x] = "O"
                part_sum += len(data) - i - 1

    return part_sum


# Part 2 Solution
def part_two_solution(data):
    direction, cycles, states = 0, 0, {}
    while True:
        if direction in {0, 2}:
            if direction == 2:
                data.reverse()
            else:
                if states is not None:
                    new_state = tuple(
                        [
                            (x, y)
                            for y, row in enumerate(data)
                            for x, char in enumerate(row)
                            if data[y][x] == "O"
                        ]
                    )
                    if new_state in states:
                        cycles = 1000000000 - (1000000000 - cycles) % (
                            cycles - states[new_state]
                        )
                        states = None
                    else:
                        states[new_state] = cycles
            for y, row in enumerate(data):
                for x, char in enumerate(row):
                    if char == "O":
                        data[y][x] = "."
                        i = y - 1
                        while i >= 0 and data[i][x] == ".":
                            i -= 1
                        data[i + 1][x] = "O"
            if direction == 2:
                data.reverse()
        elif direction == 1:
            for x in range(len(data[0])):
                for y in range(len(data)):
                    if data[y][x] == "O":
                        data[y][x] = "."
                        i = x - 1
                        while i >= 0 and data[y][i] == ".":
                            i -= 1
                        data[y][i + 1] = "O"
        else:
            for x in range(len(data[0]) - 1, -1, -1):
                for y in range(len(data)):
                    if data[y][x] == "O":
                        data[y][x] = "."
                        i = x + 1
                        while i < len(data[0]) and data[y][i] == ".":
                            i += 1
                        data[y][i - 1] = "O"
            cycles += 1
            if cycles == 1000000000:
                return sum(
                    [
                        len(data) - y
                        for y, row in enumerate(data)
                        for x, char in enumerate(row)
                        if char == "O"
                    ]
                )
        direction = (direction + 1) % 4


# Main solving function
def solve(input_file: str) -> tuple:
    with open(input_file) as f:
        data = [list(line.strip()) for line in f]

    solution_1 = part_one_solution(data)
    solution_2 = part_two_solution(data)

    return solution_1, solution_2


if __name__ == "__main__":
    t1 = time.perf_counter()

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="?")
    args = parser.parse_args()

    if args.filename is None:
        args.filename = "/Users/emre/GitHub/advent-of-code/src/2023/Inputs/day14.txt"

    solution_1, solution_2 = solve(args.filename)

    print(f"Part 1 Answer: {solution_1}")
    print(f"Part 2 Answer: {solution_2}")

    t2 = time.perf_counter()
    print(f"Execution time: {0:0.4f} seconds".format(t2 - t1))
