# Reading file
with open(r"advent_of_code\src\2021\Inputs\day10.txt") as f:
    data = [line.strip() for line in f.readlines()]
f.close()

# Part 1 Solution
POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
corrupted_lines = {}

for idx, line in enumerate(data):
    tmp_stack = []

    for chx in line:

        if chx in ["(", "[", "<", "{"]:
            tmp_stack.append(chx)

        else:
            check = tmp_stack.pop()
            if chx == ")" and check == "(":
                pass

            elif chx == "]" and check == "[":
                pass

            elif chx == "}" and check == "{":
                pass

            elif chx == ">" and check == "<":
                pass

            else:
                corrupted_lines[idx] = chx

score = 0
for chx in corrupted_lines.values():
    score += POINTS.get(chx)

print(score)
# 341823

# Part 2 Solution
for idx in reversed(corrupted_lines.keys()):
    data.pop(idx)

scores = []

for line in data:

    tmp_stack = []

    for chx in line:

        if chx in ["(", "[", "<", "{"]:
            tmp_stack.append(chx)

        else:
            check = tmp_stack.pop()

    score = 0

    for chx in reversed(tmp_stack):

        if chx == "(":
            score = score * 5 + 1

        elif chx == "[":
            score = score * 5 + 2

        elif chx == "{":
            score = score * 5 + 3

        elif chx == "<":
            score = score * 5 + 4

    scores.append(score)

scores.sort()
idx = len(scores) // 2
print(scores[idx])
# 2801302861
