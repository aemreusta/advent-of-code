import re

# Reading file
with open("src/2023/Inputs/day1.txt") as f:
    data = [line.strip() for line in f.readlines()]
f.close()

# Part 1 Solution

total = 0

for line in data:
    num = re.findall(r"\d+", line)
    num = "".join(num)
    if len(num) > 1:
        total = total + int(num[0]) * 10 + int(num[-1])
    else:
        total = total + int(num[0]) * 11

print(total)

# Part 2 Solution


def xy(ch):
    digits = [int(x) for x in ch if x in "0123456789"]
    return 10 * digits[0] + digits[-1]


pb = lambda L: sum(xy(ch) for ch in L)

L1 = "one,two,three,four,five,six,seven,eight,nine".split(",")
L2 = "o1e,t2o,t3ree,f4ur,f5ve,s6x,s7ven,e8ght,n9ne".split(",")
for x, y in zip(L1, L2):
    data = [ch.replace(x, y) for ch in data]

print(pb(data))
