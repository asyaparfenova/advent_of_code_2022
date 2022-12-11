from functools import partial


def detect_marker(data, marker):
    for n, m in enumerate(data[: -marker + 1]):
        if len(set(data[n : n + marker])) == marker:
            return n + marker


part_one = partial(detect_marker, marker=4)
part_two = partial(detect_marker, marker=14)


if __name__ == "__main__":
    with open("test.txt", "r") as file:
        data = file.read()
    print(f"The answer for the 1st task is: {part_one(data)}")
    print(f"The answer for the 2nd task is: {part_two(data)}")
