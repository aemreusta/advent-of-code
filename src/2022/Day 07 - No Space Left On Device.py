import re

with open(r"src/2022/Inputs/day7.txt") as f:
    raw_data = [line.strip() for line in f.readlines()]
f.close()


class Files:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)


class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.subdirs = []

    def add_file(self, file):
        self.files.append(file)

    def add_subdir(self, subdir):
        self.subdirs.append(subdir)

    def total_size(self):
        return sum(f.size for f in self.files) + sum(
            d.total_size() for d in self.subdirs
        )


def parse_input(raw_data):
    dirs = {}
    current_dir = None

    for line in raw_data:
        if line.startswith("$ cd"):
            if line.split()[-1] == "/":
                root = Directory("/")
                current_dir = "/"
                dirs[current_dir] = root

            elif line.split()[-1] == "..":
                cur = re.findall(r"(/[a-z]*)", current_dir)[:-2]
                current_dir = "".join(cur) + "/"
                # print(current_dir, dirs[current_dir].total_size())

            else:
                current_dir = current_dir + line.split()[-1] + "/"

        elif line.startswith("dir"):
            dir_name = line.split()[1]
            subdir = Directory(current_dir + dir_name + "/")
            dirs[current_dir].add_subdir(subdir)
            dirs[current_dir + dir_name + "/"] = subdir

        elif line.startswith("$ ls"):
            continue

        else:
            size, name = line.split()
            files = Files(name, size)
            dirs[current_dir].add_file(files)

        # print(current_dir)

    return dirs


dirs = parse_input(raw_data)

# Part 1 Solution
result = 0

for dir in dirs.keys():
    dir_size = dirs[dir].total_size()
    if dir_size < 100000:
        # print(dir)
        result += dir_size

print(result)

# Part 2 Solution
FILESYSTEM = 70000000
UPDATE_SPACE = 30000000
SPACE_NEEDED = UPDATE_SPACE - (FILESYSTEM - dirs["/"].total_size())
# print(SPACE_NEEDED)

removed_dir = dirs["/"].total_size()

for dir in dirs.keys():
    dir_size = dirs[dir].total_size()

    if dir_size > SPACE_NEEDED and dir_size < removed_dir:
        removed_dir = dir_size

print(removed_dir)
