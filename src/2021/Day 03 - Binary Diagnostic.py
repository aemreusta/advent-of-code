# Reading file
with open(r"advent_of_code\src\2021\Inputs\day3.txt") as f:
    data = [line.strip() for line in f.readlines()]
f.close()

# Part 1 Solution
line_length = len(data[0])
rate = [0] * line_length

for i in range(len(data)):
    for k in range(line_length):
        if data[i][k] == "0":
            rate[k] -= 1

        elif data[i][k] == "1":
            rate[k] += 1

gamma_rate, epsilon_rate = "", ""
for i in range(line_length):
    if rate[i] > 0:
        gamma_rate += "0"
        epsilon_rate += "1"

    else:
        gamma_rate += "1"
        epsilon_rate += "0"

power = int(gamma_rate, 2) * int(epsilon_rate, 2)
print(power)

# Part 2 Solution
line_length = len(data[0])
o2_list, co2_list = data.copy(), data.copy()

for i in range(line_length):

    o2_bit, co2_bit = {"0": 0, "1": 0}, {"0": 0, "1": 0}
    o2, co2 = "0", "0"

    if len(o2_list) != 1:
        for number in o2_list:
            o2_bit[number[i]] += 1

        if o2_bit["1"] >= o2_bit["0"]:
            o2 = "1"

        o2_list = [n for n in o2_list if n[i] == o2]

    if len(co2_list) != 1:

        for number in co2_list:
            co2_bit[number[i]] += 1

        if co2_bit["1"] < co2_bit["0"]:
            co2 = "1"

        co2_list = [n for n in co2_list if n[i] == co2]


o2_rate = int(o2_list[0], 2)
co2_rate = int(co2_list[0], 2)

print(o2_rate * co2_rate)
