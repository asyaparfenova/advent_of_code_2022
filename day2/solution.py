def parse_data(input_data):
    input_lines = input_data.split("\n")
    result = []
    subres = []
    for il in input_lines:
        if il != "":
            subres.append(int(il))
        else:
            result.append(subres)
            subres = []
    result.append(subres)
    return result


def get_n_max(kcals, n):
    sums = []
    for elf in kcals:
        sums.append(sum(elf))
    sums.sort(reverse=True)
    result = sum(sums[:n])
    return result


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.read()
    input = parse_data(data)
    print(f"The answer for the 1st task is: {get_n_max(input, 1)}")
    print(f"The answer for the 2nd task is: {get_n_max(input, 3)}")
