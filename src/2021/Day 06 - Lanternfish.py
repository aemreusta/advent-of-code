#Reading file
with open(r"advent_of_code\src\2021\Inputs\day6.txt") as f:
    data = [line.strip() for line in f.readlines()]
f.close()

#Part 1 Solution
init_fish = list(map(int, data[0].split(",")))
fish_list = [0]*9

for fish in init_fish:
    fish_list[fish] += 1

for _ in range(80):
    births = fish_list.pop(0)
    fish_list.append(births)
    fish_list[6] += births
    
print(sum(fish_list))
#363101

#Part 2 Solution
init_fish = list(map(int, data[0].split(",")))
fish_list = [0]*9

for fish in init_fish:
    fish_list[fish] += 1

for _ in range(256):
    births = fish_list.pop(0)
    fish_list.append(births)
    fish_list[6] += births
    
print(sum(fish_list))
#1644286074024