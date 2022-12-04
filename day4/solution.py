def parse_data(input_data):
    input_lines = input_data.split("\n")
    result = []
    for il in input_lines:
        pair = il.split(",")
        clean_pair = []
        for elf in pair:
            assignment = elf.split("-")
            clean_assignment = set(
                range(int(assignment[0]), int(assignment[1]) + 1)
            )
            clean_pair.append(clean_assignment)
        result.append(clean_pair)
    return result


def part_one(data):
    total = 0
    for pair in data:
        if pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]):
            total += 1
    return total


def part_two(data):
    total = 0
    for pair in data:
        pairs = pair[0] | pair[1]
        if len(pairs) < len(pair[0]) + len(pair[1]):
            total += 1
    return total


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.read()
    input = parse_data(data)
    print(f"The answer for the 1st task is: {part_one(input)}")
    print(f"The answer for the 2nd task is: {part_two(input)}")
