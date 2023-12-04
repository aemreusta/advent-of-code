# Reading file
with open(r"advent_of_code\src\2022\Inputs\day2.txt") as f:
    data = [line.strip() for line in f]
f.close()

# Part 1 Solution
score = 0

for round in data:
    if round == "A X":
        score += 4

    elif round == "A Y":
        score += 8

    elif round == "A Z":
        score += 3

    elif round == "B X":
        score += 1

    elif round == "B Y":
        score += 5

    elif round == "B Z":
        score += 9

    elif round == "C X":
        score += 7

    elif round == "C Y":
        score += 2

    elif round == "C Z":
        score += 6

print(score)
# 14069

# Part 2 Solution
result_scores = 0

for round in data:
    if round[2] == "X":
        scores = {"A": 3, "B": 1, "C": 2}
        result_scores += scores.get(round[0])

    elif round[2] == "Y":
        scores = {"A": 1, "B": 2, "C": 3}
        result_scores += 3 + scores.get(round[0])

    elif round[2] == "Z":
        scores = {"A": 2, "B": 3, "C": 1}
        result_scores += 6 + scores.get(round[0])

print(result_scores)
# 12411
