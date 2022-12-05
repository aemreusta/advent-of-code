# Reading file
with open(r"advent_of_code\src\2022\Inputs\day5.txt") as f:
    data = [line for line in f]
f.close()


def create_stacks(raw_data: list, stacks_line_num: int):
    stacks = []
    LETTER_NUM = 1

    for _ in range(int(raw_data[stacks_line_num - 1][-3])):
        temp_stack = []

        for line in range(stacks_line_num - 1):
            tmp_var = raw_data[line][LETTER_NUM]

            if tmp_var != " ":
                temp_stack.append(tmp_var)

        LETTER_NUM += 4
        stacks.append(temp_stack)

    return stacks


MOVE_LINE_NUM = 11
moves = []

for line in data[MOVE_LINE_NUM - 1 :]:
    edited_moves = []

    for word in line.split():

        try:
            edited_moves.append(int(word))

        except ValueError:
            pass

    moves.append(edited_moves)

# Part 1 Solution
stacks = create_stacks(data, 9)

for move in moves:
    for i in range(move[0]):
        stacks[move[2] - 1].insert(0, stacks[move[1] - 1].pop(0))

result = ""

for stack in stacks:
    result += stack.pop(0)

print(result)
# TBVFVDZPN

# Part 2 Solution
stacks = create_stacks(data, 9)

for move in moves:
    tmp_stack = stacks[move[1] - 1][0 : move[0]]
    tmp_stack.reverse()

    for i in range(move[0]):
        stacks[move[2] - 1].insert(0, tmp_stack[i])
        stacks[move[1] - 1].pop(0)


result = ""

for stack in stacks:
    result += stack.pop(0)

print(result)
# VLCWHTDSZ
