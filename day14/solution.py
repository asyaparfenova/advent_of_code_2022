def parse_data(input_data):
    paths = []
    bottom = 0
    r_max = 500
    l_max = 500
    for raw_path in input_data.split("\n"):
        raw_path = raw_path.split(" -> ")
        path = []
        for n, point in enumerate(raw_path):
            point = point.split(",")
            point = [int(point[0]), int(point[1])]
            if int(point[1]) > bottom:
                bottom = int(point[1])
            if int(point[0]) > r_max:
                r_max = int(point[0])
            if int(point[1]) < l_max:
                l_max = int(point[0])
            path.append(point)
        paths.append(path)
    return paths, bottom, [r_max + 500, bottom + 2], [l_max - 500, bottom + 2]


def draw_path(path):
    new_path = path
    for n, point in enumerate(path[:-1], start=1):
        for x in range(point[0] + 1, path[n][0]):
            new_path.append([x, path[n][1]])
        for x in range(path[n][0] + 1, point[0]):
            new_path.append([x, path[n][1]])
        for y in range(point[1] + 1, path[n][1]):
            new_path.append([path[n][0], y])
        for y in range(path[n][1] + 1, point[1]):
            new_path.append([path[n][0], y])
    return new_path


def draw_all(paths):
    all_paths = []
    for path in paths:
        full_path = draw_path(path)
        all_paths += full_path
    return all_paths


def sand_move_one(rocks, resting_sand, bottom, start):
    options = [
        [start[0], start[1] + 1],
        [start[0] - 1, start[1] + 1],
        [start[0] + 1, start[1] + 1],
    ]
    sm = True
    global still_moving
    for o in options:
        if o[1] > bottom:
            still_moving = False
            sm = False
        elif o not in rocks and o not in resting_sand:
            new_start = o
            break
        else:
            new_start = None
    if not sm:
        pass
    elif new_start:
        sand_move_one(rocks, resting_sand, bottom, new_start)
    else:
        resting_sand.append(start)


def part_one(rocks, bottom):
    resting_sand = []
    l = -1
    while l < len(resting_sand):
        l = len(resting_sand)
        start = [500, 0]
        sand_move_one(rocks, resting_sand, bottom, start)
    return l


def sand_move_two(rocks, resting_sand, bottom, start):
    options = [
        [start[0], start[1] + 1],
        [start[0] - 1, start[1] + 1],
        [start[0] + 1, start[1] + 1],
    ]
    for o in options:
        if o not in rocks and o not in resting_sand:
            new_start = o
            break
        else:
            new_start = None
    if new_start:
        sand_move_two(rocks, resting_sand, bottom, new_start)
    else:
        resting_sand.append(start)
        if [start[0], start[1] + 2] in resting_sand:
            resting_sand.remove([start[0], start[1] + 2])


def part_two(rocks, bottom):
    resting_sand = []
    l = 0
    while [500, 0] not in resting_sand:
        start = [500, 0]
        sand_move_two(rocks, resting_sand, bottom, start)
        l += 1
    return l


if __name__ == "__main__":
    with open("test.txt", "r") as file:
        data = file.read()
    paths, bottom, r_max, l_max = parse_data(data)
    rocks = draw_all(paths + [[r_max, l_max]])
    print(f"The answer for the 1st task is: {part_one(rocks, bottom)}")
    print(f"The answer for the 2nd task is: {part_two(rocks, bottom)}")
