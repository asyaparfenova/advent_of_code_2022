import ast


def parse_data(input_data):
    distress_signal = []
    for pair in input_data.split("\n\n"):
        pair = pair.split("\n")
        pair = [ast.literal_eval(pair[0]), ast.literal_eval(pair[1])]
        distress_signal.append(pair)
    return distress_signal


def compare_items(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return True
        elif left > right:
            return False
    else:
        if type(right) == int:
            right = [right]
        elif type(left) == int:
            left = [left]
        return compare_lists(left, right)


def compare_lists(left, right):
    mln = min(len(left), len(right))
    for n in range(mln):
        res = compare_items(left[n], right[n])
        if res == None:
            pass
        else:
            return res
    if len(left) > len(right):
        return False
    elif len(left) < len(right):
        return True


def part_one(distress_signal):
    result = 0
    for n, pair in enumerate(distress_signal):
        b = compare_lists(pair[0], pair[1])
        if b:
            result += n + 1
    return result


def part_two(distress_signal):
    all_packets = [[[2]], [[6]]]
    for pair in distress_signal:
        for packet in pair:
            if compare_lists(packet, all_packets[0]):
                all_packets = [packet] + all_packets
            elif compare_lists(all_packets[-1], packet):
                all_packets = all_packets + [packet]
            else:
                for n, m in enumerate(all_packets, start=1):
                    if compare_lists(
                        all_packets[n - 1], packet
                    ) and compare_lists(packet, all_packets[n]):
                        all_packets = (
                            all_packets[:n] + [packet] + all_packets[n:]
                        )
                        break
    return (all_packets.index([[2]]) + 1) * (all_packets.index([[6]]) + 1)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.read()
    ds = parse_data(data)
    print(f"The answer for the 1st task is: {part_one(ds)}")
    print(f"The answer for the 2nd task is: {part_two(ds)}")
