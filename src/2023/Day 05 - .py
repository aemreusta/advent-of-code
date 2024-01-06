import argparse
import time


# Part 1 Solution
def part_one_solution(data):
    part_sum = 0

    return part_sum


# Part 2 Solution
def part_two_solution(data):
    total = 0
    return total


# Main solving function
def solve(input_file: str) -> tuple:
    with open(input_file) as f:
        data = [[line.strip()] for line in f.readlines()]

    solution_1 = part_one_solution(data)
    solution_2 = part_two_solution(data)

    return solution_1, solution_2


if __name__ == "__main__":
    t1 = time.perf_counter()

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="?")
    args = parser.parse_args()

    if args.filename is None:
        args.filename = "/Users/emre/GitHub/advent-of-code/src/2023/Inputs/day4.txt"

    solution_1, solution_2 = solve(args.filename)

    print(f"Part 1 Answer: {solution_1}")
    print(f"Part 2 Answer: {solution_2}")

    t2 = time.perf_counter()
    print(f"Execution time: {0:0.4f} seconds".format(t2 - t1))
