DICT = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}

def parse_data(input_data):
    input_lines = input_data.split("\n")
    result = []
    for il in input_lines:
        subres = list(il)
        result.append(subres)
    return result

def part_one(data):
    total = 0
    dict = DICT
    for backpack in data:
        for i in backpack[: len(backpack) // 2]:
            if i in backpack[len(backpack) // 2 :]:
                found = i
        total += dict[found]
    return total

def part_two(data):
    total = 0
    dict = DICT
    for num in range(len(data)//3):
        sub = []
        for i in data[3*num]:
            if i in data[3*num + 1]:
                sub.append(i)
        for i in sub:
            if i in data[3*num + 2]:
                found = i
        total += dict[found]
    return total


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.read()
    input = parse_data(data)
    print(f"The answer for the 1st task is: {part_one(input)}")
    print(f"The answer for the 2nd task is: {part_two(input)}")
