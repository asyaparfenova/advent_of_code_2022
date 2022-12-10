def parse_data(input_data):
    input_lines = input_data.split("\n")
    commands = []
    for il in input_lines:
        command = il.split(" ")
        if len(command) == 1:
            commands.append(command)
        else:
            commands.append([command[0], int(command[1])])
    return commands


def part_one(commands):
    x = 1
    register = []
    result = 0
    # create register
    for command in commands:
        if command[0] == "noop":
            register.append(x)
        else:
            register.append(x)
            register.append(x)
            x += command[1]
    # calculate answer
    for i in [20, 60, 100, 140, 180, 220]:
        result += i * register[i - 1]
    return result


def screenwrite(i, sprite, screen):
    if i % 40 in sprite:
        screen += "#"
    else:
        screen += "."
    i += 1
    return i, screen


def part_two(commands):
    sprite = [0, 1, 2]
    i = 0
    screen = ""
    # create screen input
    for command in commands:
        if command[0] == "noop":
            i, screen = screenwrite(i, sprite, screen)
        else:
            i, screen = screenwrite(i, sprite, screen)
            i, screen = screenwrite(i, sprite, screen)
            sprite = [
                sprite[0] + command[1],
                sprite[1] + command[1],
                sprite[2] + command[1],
            ]
    # print screen
    for n in range(len(screen) // 40):
        print(screen[n * 40 : n * 40 + 40])


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.read()
    commands = parse_data(data)
    print(f"The answer for the 1st task is: {part_one(commands)}")
    print(f"The answer for the 2nd task is:")
    # print visual representation of the part two answer
    part_two(commands)
