import re
import numpy as np

def parse_data(input_data):
    input_monkeys = input_data.split("\n\n")
    monkeys = []
    for im in input_monkeys:
        monkey = {}
        iml = im.split("\n")
        items = re.findall(".(\d+)", iml[1])
        monkey["items"] = [int(i) for i in items]
        operation = re.findall("(\+.+|\*.+)", iml[2])
        #operation[1] = int(operation[1])
        monkey["operation"] = operation[0].split(" ")
        monkey["test"] = int(re.findall(".(\d+)", iml[3]).pop())
        monkey["true"] = int(re.findall(".(\d+)", iml[4]).pop())
        monkey["false"] = int(re.findall(".(\d+)", iml[5]).pop())
        monkey["inspected"] = 0
        monkeys.append(monkey)
    return monkeys

def play_round(monkeys, worry_decrease):
    for monkey in monkeys:
        for item in monkey["items"]:
            monkey["items"] = monkey["items"][1:]
            monkey["inspected"] += 1
            try:
                if monkey["operation"][0] == "+":
                    wl = (item + int(monkey["operation"][1])) // worry_decrease
                else:
                    wl = (item * int(monkey["operation"][1])) // worry_decrease
            except:
                if monkey["operation"][0] == "+":
                    wl = (item + item) // 3
                else:
                    wl = (item * item) // 3
            test = (wl % monkey["test"] == 0)
            if test:
                monkeys[monkey["true"]]["items"].append(wl)
            else:
                monkeys[monkey["false"]]["items"].append(wl)


def part_one(monkeys):
    for n in range(20):
        play_round(monkeys, 3)
    all_instected = [m["inspected"] for m in monkeys]
    all_instected.sort()
    result = all_instected[-1] * all_instected[-2]
    return result

def play_round_two(monkeys):
    big_divider = np.prod([m["test"] for m in monkeys])
    for monkey in monkeys:
        for item in monkey["items"]:
            monkey["items"] = monkey["items"][1:]
            monkey["inspected"] += 1
            try:
                if monkey["operation"][0] == "+":
                    wl = (item + int(monkey["operation"][1]))
                else:
                    wl = (item * int(monkey["operation"][1]))
            except:
                if monkey["operation"][0] == "+":
                    wl = (item + item)
                else:
                    wl = (item * item)
            test = (wl % monkey["test"] == 0)
            if test:
                monkeys[monkey["true"]]["items"].append(wl % big_divider)
            else:
                monkeys[monkey["false"]]["items"].append(wl % big_divider)

def part_two(monkeys):
    for n in range(10000):
        play_round_two(monkeys)
        if n in (0, 19, 999, 1999, 2999, 3999, 4999, 5999):
            print("----- after round", n+1, "-----")
            print(monkeys)
    all_instected = [m["inspected"] for m in monkeys]
    all_instected.sort()
    result = all_instected[-1] * all_instected[-2]
    return result


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.read()
    monkeys = parse_data(data)
    print(monkeys)
    print(f"The answer for the 1st task is: {part_one(monkeys)}")
    monkeys = parse_data(data)
    print(f"The answer for the 2nd task is: {part_two(monkeys)}")
    # # print visual representation of the part two answer
    # part_two(commands)
