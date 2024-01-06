import argparse
import time
import re


# Part 1 Solution
def part_one_solution(data):
    part_sum = 0

    for line in data:
        line = line.split("|")
        line_1 = [int(i) for i in line[0].split(":")[1].strip().split(" ") if i != ""]
        line_2 = [int(i) for i in line[1].strip().split(" ") if i != ""]

        # print(line_1, line_2)

        count_dict = {}

        for num in line_1:
            if num in count_dict:
                continue
            else:
                count_dict[num] = 0

        for num in line_2:
            if num in count_dict:
                count_dict[num] += 1
            else:
                continue

        bingo = sum(count_dict.values())
        part_sum += int(2 ** (bingo - 1))

        # print(count_dict, bingo, part_sum)

    return part_sum


# Part 2 Solution
def part_two_solution(data):
    total = 0

    cards_dict = {}
    pattern = re.compile(r"(\d+):")

    for line in data:
        card_no = pattern.search(line)

        if card_no:
            card_no = int(card_no.group(1))
            cards_dict[card_no] = 1

    for line in data:
        card_no = int(pattern.search(line).group(1))
        line = line.split("|")
        line_1 = [int(i) for i in line[0].split(":")[1].strip().split(" ") if i != ""]
        line_2 = [int(i) for i in line[1].strip().split(" ") if i != ""]
        count_dict = {}

        for num in line_1:
            if num in count_dict:
                continue
            else:
                count_dict[num] = 0

        for num in line_2:
            if num in count_dict:
                count_dict[num] += 1
            else:
                continue

        bingo = sum(count_dict.values())

        if bingo > 0:
            for i in range(card_no + 1, card_no + bingo + 1):
                if i in cards_dict:
                    cards_dict[i] += 1 * cards_dict[card_no]

            # print(card_no, i, bingo, cards_dict)

    # print(cards_dict)

    for card in cards_dict:
        total += cards_dict[card]

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
        args.filename = "/Users/emre/GitHub/advent-of-code/src/2023/Inputs/day4.txt"

    solution_1, solution_2 = solve(args.filename)

    print(f"Part 1 Answer: {solution_1}")
    print(f"Part 2 Answer: {solution_2}")

    t2 = time.perf_counter()
    print(f"Execution time: {0:0.4f} seconds".format(t2 - t1))
