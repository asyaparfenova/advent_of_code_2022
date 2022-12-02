RULES = {"A": (1, "C", "B"), "B": (2, "A", "C"), "C": (3, "B", "A")}

def parse_data(input_data):
    input_lines = input_data.split("\n")
    result = []
    for il in input_lines:
        subres = il.split(" ")
        result.append(subres)
    return result


def part_one(data):
    rules = RULES
    xyz = {"X": "A", "Y": "B", "Z": "C"}
    total = 0
    for elf, you in data:
        you = xyz[you]
        if you == elf:
            score = 3 + rules[you][0]
        elif elf == rules[you][1]:
            score = 6 + rules[you][0]
        else:
            score = rules[you][0]
        total += score
    return total

def part_two(data):
    rules = {"A": (1, "C", "B"), "B": (2, "A", "C"), "C": (3, "B", "A")}
    total = 0
    for elf, you in data:
        if you == "X":
            you = rules[elf][1]
            score = rules[you][0]
        elif you == "Y":
            you = elf
            score = 3 + rules[you][0]
        else:
            you = rules[elf][2]
            score = 6 + rules[you][0]
        total += score
    return total


if __name__ == "__main__":
    with open("test.txt", "r") as file:
        data = file.read()
    input = parse_data(data)
    print(f"The answer for the 1st task is: {part_one(input)}")
    print(f"The answer for the 2nd task is: {part_two(input)}")
