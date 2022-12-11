import copy
import numpy as np
import re

from functools import partial


def parse_data(input_data):
    input_monkeys = input_data.split("\n\n")
    monkeys = []
    for im in input_monkeys:
        monkey = {}
        iml = im.split("\n")
        monkey["items"] = [int(i) for i in re.findall(".(\d+)", iml[1])]
        monkey["operation"] = re.findall("(\+.+|\*.+)", iml[2])[0].split(" ")
        monkey["test"] = int(re.findall(".(\d+)", iml[3]).pop())
        monkey["true"] = int(re.findall(".(\d+)", iml[4]).pop())
        monkey["false"] = int(re.findall(".(\d+)", iml[5]).pop())
        monkey["inspected"] = 0
        monkeys.append(monkey)
    return monkeys


def play_round(monkeys, worry_decrease):
    big_divider = np.prod([m["test"] for m in monkeys])
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
                    wl = (item + item) // worry_decrease
                else:
                    wl = (item * item) // worry_decrease
            if wl % monkey["test"] == 0:
                monkeys[monkey["true"]]["items"].append(wl % big_divider)
            else:
                monkeys[monkey["false"]]["items"].append(wl % big_divider)


def monkey_business(monkeys, worry_decrease, rounds):
    mnks = copy.deepcopy(monkeys)
    for n in range(rounds):
        play_round(mnks, worry_decrease)
    all_instected = [m["inspected"] for m in mnks]
    all_instected.sort()
    result = all_instected[-1] * all_instected[-2]
    return result


part_one = partial(monkey_business, worry_decrease=3, rounds=20)
part_two = partial(monkey_business, worry_decrease=1, rounds=10000)

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.read()
    monkeys = parse_data(data)
    print(f"The answer for the 1st task is: {part_one(monkeys)}")
    print(f"The answer for the 2nd task is: {part_two(monkeys)}")
