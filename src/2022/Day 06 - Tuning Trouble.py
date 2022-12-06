# Reading file
with open(r"advent_of_code\src\2022\Inputs\day6.txt") as f:
    raw_data = f.readline()
f.close()


def dif_char(chars: list, package_length: int):

    for i in range(package_length - 1):
        if chars[i] in chars[i + 1 :]:
            return False

    return True


def run_task(data: list, package_legnth: int):
    pos = 0

    for i in range(len(data) - (package_legnth + 1)):

        if dif_char(data[i : i + package_legnth], package_legnth) is True:
            # print(i + 4, data[i : i + 4])
            pos = i + package_legnth
            break

    return pos


# Part 1 Solution
print(run_task(raw_data, 4))
# 1134

# Part 2 Solution
print(run_task(raw_data, 14))
# 2263
