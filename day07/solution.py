import re


def parse_data(input_data):
    input_lines = input_data.split("\n")
    all_files = {}
    all_children = {}
    path = "home/"
    check = 0
    for il in input_lines:
        if il == "$ cd ..":
            path = "/".join(path.split("/")[:-2]) + "/"
            check += 1
        elif il == "$ cd /":
            path = "home/"
            if path not in all_children:
                all_children[path] = []
                all_files[path] = []
        elif il[:4] == "$ cd":
            path += il.split(" ")[2] + "/"
            if path not in all_children:
                all_children[path] = []
                all_files[path] = []
        elif bool(re.search("^\d+ .+", il)):
            if path in all_files:
                all_files[path].append(int(il.split(" ")[0]))
        elif il[:3] == "dir":
            child = il.split(" ")[1]
            if path in all_children:
                all_children[path].append(path + child + "/")
    return all_files, all_children


def count_total_weight(dir, files, dirs):
    weight = sum(files[dir])
    for child in dirs[dir]:
        weight += count_total_weight(child, files, dirs)
    return weight


def part_one(files, dirs):
    summ = 0
    for dir in dirs:
        weight = count_total_weight(dir, files, dirs)
        if weight <= 100000:
            summ += weight
    return summ


def part_two(files, dirs):
    print("total weight of home is ", count_total_weight("home/", files, dirs))
    to_delete = 30000000 - (
        70000000 - count_total_weight("home/", files, dirs)
    )
    bigdirs = []
    for dir in dirs:
        weight = count_total_weight(dir, files, dirs)
        if weight >= to_delete:
            bigdirs.append(weight)
    return min(bigdirs)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.read()
    files, dirs = parse_data(data)
    print(f"The answer for the 1st task is: {part_one(files, dirs)}")
    print(f"The answer for the 2nd task is: {part_two(files, dirs)}")
