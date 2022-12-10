import string


def parse_data(input_data):
    input_lines = input_data.split("\n")
    result = []
    for il in input_lines:
        backpack = list(il)
        result.append(backpack)
    return result


def part_one(data):
    total = 0
    dict = DICT
    for backpack in data:
        for i in backpack[: len(backpack) // 2]:
            if i in backpack[len(backpack) // 2 :]:
                found = i
        total += string.ascii_letters.index(found) + 1
    return total


def part_two(data):
    total = 0
    dict = DICT
    for num in range(len(data) // 3):
        sub = []
        for i in data[3 * num]:
            if i in data[3 * num + 1]:
                sub.append(i)
        for i in sub:
            if i in data[3 * num + 2]:
                found = i
        total += string.ascii_letters.index(found) + 1
    return total


if __name__ == "__main__":
    with open("test.txt", "r") as file:
        data = file.read()
    input = parse_data(data)
    print(f"The answer for the 1st task is: {part_one(input)}")
    print(f"The answer for the 2nd task is: {part_two(input)}")
