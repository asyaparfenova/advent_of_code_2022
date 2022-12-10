def parse_data(input_data):
    input_lines = input_data.split("\n")
    crates = []
    commands = []
    empty = False
    for il in input_lines:
        if il != "" and not empty:
            crates.append(il)
        elif il == "":
            empty = True
        else:
            commands.append(il)
    cln_crates = clean_crates(crates)
    cln_commands = clean_commands(commands)
    return cln_crates, cln_commands


def clean_crates(data):
    nums = data[-1].split("  ")
    crates = {}
    for num in nums:
        crates[int(num)] = []
    for il in list(reversed(data[:-1])):
        for n in crates:
            crate = il[(n - 1) * 4 + 1]
            if crate != " ":
                crates[n].append(crate)
    return crates


def clean_commands(data):
    commands = []
    for il in data:
        line = il.split(" ")
        command = []
        for l in line:
            try:
                command.append(int(l))
            except:
                pass
        commands.append(command)
    return commands


def part_one(crates, commands):
    crts = crates.copy()
    result = ""
    for a, b, c in commands:
        movable = crts[b][-a:]
        movable.reverse()
        crts[c] = crts[c] + movable
        crts[b] = crts[b][:-a]
    for stack in crts:
        result += crts[stack][-1]
    return result


def part_two(crates, commands):
    crts = crates.copy()
    result = ""
    for a, b, c in commands:
        movable = crts[b][-a:]
        crts[c] = crts[c] + movable
        crts[b] = crts[b][:-a]
    for stack in crts:
        result += crts[stack][-1]
    return result


if __name__ == "__main__":
    with open("test.txt", "r") as file:
        data = file.read()
    crates, commands = parse_data(data)
    print(f"The answer for the 1st task is: {part_one(crates, commands)}")
    print(f"The answer for the 2nd task is: {part_two(crates, commands)}")
