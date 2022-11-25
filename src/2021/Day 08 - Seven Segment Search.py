# Reading file
with open(r"advent_of_code\src\2021\Inputs\day1.txt") as f:
    data = [line.strip().split(" | ") for line in f.readlines()]
f.close()

pattern = [["".join(sorted(word)) for word in line[0].split()] for line in data]
output = [["".join(sorted(word)) for word in line[1].split()] for line in data]

# Part 1 Solution
result = 0
for idx, line in enumerate(output):
    for idx, word in enumerate(line):
        if len(word) in [2, 3, 4, 7]:  # [1, 7, 4, 8]
            result += 1

print(result)
# 387

# Part 2 Solution
result = 0
for idx, line in enumerate(pattern):
    digits = {}

    while len(digits) < 10:
        for id, word in enumerate(line):
            word_length = len(word)

            if word_length == 2 and "1" not in digits:
                digits["1"] = word

            if word_length == 3 and "7" not in digits:
                digits["7"] = word

            if word_length == 4 and "4" not in digits:
                digits["4"] = word

            if word_length == 7 and "8" not in digits:
                digits["8"] = word

            if word_length == 5:  # 2, 3, 5
                if "7" in digits and all(
                    [i in list(word) for i in list(digits.get("7"))]
                ):
                    digits["3"] = word

                elif "9" in digits and all(
                    [i in list(digits.get("9")) for i in list(word)]
                ):
                    digits["5"] = word

                elif "9" in digits:
                    digits["2"] = word

            if word_length == 6:  # 0, 6, 9
                if "3" in digits and all(
                    [i in list(word) for i in list(digits.get("3"))]
                ):
                    digits["9"] = word

                elif (
                    "5" in digits
                    and sum([i in list(digits.get("5")) for i in list(word)]) == 5
                ):
                    digits["6"] = word

                elif (
                    "5" in digits
                    and sum([i in list(digits.get("5")) for i in list(word)]) == 4
                ):
                    digits["0"] = word

    num = ""
    for word in output[idx]:
        for k, v in digits.items():
            if word == v:
                num += k

    # print(digits, num)
    try:
        result += int(num)
    except ValueError:
        continue

print(result)
# 986034
