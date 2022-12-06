def part_one(data):
    for n in range(len(data) - 3):
        if len(set(data[n:n+4])) == 4:
            return n + 4

def part_two(data):
    for n in range(len(data) - 13):
        if len(set(data[n:n+14])) == 14:
            return n + 14


if __name__ == "__main__":
    with open("test.txt", "r") as file:
        data = file.read()
    print(f"The answer for the 1st task is: {part_one(data)}")
    print(f"The answer for the 2nd task is: {part_two(data)}")
