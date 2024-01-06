import argparse
import time

# Directions for exploring adjacent cells
DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, 1], [-1, -1], [1, -1], [1, 1]]


# Part 1 Solution
def part_one_solution(data):
    part_sum = 0
    for idy, line in enumerate(data):
        digits = []
        adjacent = False
        for idx, item in enumerate(line):
            if item.isdigit():
                digits.append(item)
                if not adjacent:
                    for dx, dy in DIRECTIONS:
                        x, y = idx + dx, idy + dy
                        if (
                            0 <= x < len(line)
                            and 0 <= y < len(data)
                            and data[y][x] != "."
                            and not data[y][x].isdigit()
                        ):
                            adjacent = True
                            break
            else:
                if adjacent:
                    part_sum += int("".join(digits))
                digits = []
                adjacent = False
        if adjacent and digits:
            part_sum += int("".join(digits))
    return part_sum


# Helper function to flood horizontally
def h_flood(x: int, y: int, m: int, engine_map) -> str:
    # Check boundaries
    if y < 0 or y >= len(engine_map) or x < 0 or x >= len(engine_map[y]):
        return ""

    if not engine_map[y][x].isnumeric():
        return ""

    flood = h_flood(x + m, y, m, engine_map)
    return f'{flood if m < 0 else ""}{engine_map[y][x]}{flood if m > 0 else ""}'


# Function to get surrounding numbers
def get_surrounding(x: int, y: int, engine_map) -> list:
    return list(
        map(
            int,
            filter(
                lambda _: _,
                {
                    h_flood(_x, _y, -1, engine_map)[:-1]
                    + h_flood(_x, _y, 1, engine_map)
                    for _x, _y in get_directions(x, y)
                    if engine_map[_y][_x] != "*"
                },
            ),
        )
    )


# Function to get coordinates in all directions
def get_directions(x, y):
    return [(x + dx, y + dy) for dx, dy in DIRECTIONS]


# Part 2 Solution
def part_two_solution(data):
    engine_map = data
    total = 0

    for i, row in enumerate(engine_map):
        for j, char in enumerate(row):
            if char == "*":
                nums = get_surrounding(j, i, engine_map)
                if len(nums) == 2:
                    total += nums[0] * nums[1]

    return total


# Main solving function
def solve(input_file: str) -> tuple:
    with open(input_file) as f:
        data = [line.strip() for line in f.readlines()]

    solution_1 = part_one_solution(data)
    solution_2 = part_two_solution(data)

    return solution_1, solution_2


if __name__ == "__main__":
    t1 = time.perf_counter()

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="?")
    args = parser.parse_args()

    if args.filename is None:
        args.filename = "/Users/emre/GitHub/advent-of-code/src/2023/Inputs/day3.txt"

    solution_1, solution_2 = solve(args.filename)

    print(f"Part 1 Answer: {solution_1}")
    print(f"Part 2 Answer: {solution_2}")

    t2 = time.perf_counter()
    print(f"Execution time: {0:0.4f} seconds".format(t2 - t1))
