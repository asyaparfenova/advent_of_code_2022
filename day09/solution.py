def parse_data(input_data):
    input_lines = input_data.split("\n")
    commands = []
    for il in input_lines:
        command = il.split(" ")
        commands.append([command[0], int(command[1])])
    return commands


def head_move(hx, hy, dir):
    if dir == "R":
        hx += 1
    elif dir == "L":
        hx -= 1
    elif dir == "U":
        hy += 1
    elif dir == "D":
        hy -= 1
    return hx, hy


def follow(hx, hy, tx, ty):
    if abs(tx - hx) + abs(ty - hy) == 4:
        tx = (tx + hx) // 2
        ty = (ty + hy) // 2
    elif abs(tx - hx) >= 2:
        tx = (tx + hx) // 2
        ty = hy
    elif abs(ty - hy) >= 2:
        tx = hx
        ty = (ty + hy) // 2
    return tx, ty


def move(rope, command, t_trace):
    dir = command[0]
    for step in range(command[1]):
        rope[0][0], rope[0][1] = head_move(rope[0][0], rope[0][1], dir)
        for node_num in range(len(rope) - 1):
            rope[node_num + 1][0], rope[node_num + 1][1] = follow(
                rope[node_num][0],
                rope[node_num][1],
                rope[node_num + 1][0],
                rope[node_num + 1][1],
            )
        t_trace.add((rope[-1][0], rope[-1][1]))
    return rope, t_trace


def move_rope_by_instructions(rope_length, commands):
    rope = []
    t_trace = {(0, 0)}
    for node in range(rope_length):
        rope.append([0, 0])
    for command in commands:
        rope, t_trace = move(rope, command, t_trace)
        # print(rope)
    return len(t_trace)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.read()
    commands = parse_data(data)
    print(
        f"The answer for the 1st task is: {move_rope_by_instructions(2, commands)}"
    )
    print(
        f"The answer for the 2nd task is: {move_rope_by_instructions(10, commands)}"
    )
