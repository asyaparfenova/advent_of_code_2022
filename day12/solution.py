import networkx as nx


def parse_data(input_data):
    nodes = {}
    ps = []
    for x, l in enumerate(input_data.split("\n")):
        for y, c in enumerate(l):
            if c == "S":
                nodes[(x, y)] = ord("a")
                ps.append((x, y))
                s = (x, y)
            elif c == "E":
                nodes[(x, y)] = ord("z")
                e = (x, y)
            elif c == "a":
                nodes[(x, y)] = ord(c)
                ps.append((x, y))
            else:
                nodes[(x, y)] = ord(c)
    return nodes, s, e, ps


def get_graph(nodes):
    graph = nx.DiGraph()
    for n in nodes:
        for p in [
            (n[0] + 1, n[1]),
            (n[0] - 1, n[1]),
            (n[0], n[1] + 1),
            (n[0], n[1] - 1),
        ]:
            if p in nodes and nodes[p] - nodes[n] <= 1:
                graph.add_edge(n, p)
    return graph


def part_one(graph, s, e):
    l = nx.shortest_path_length(graph, s, e)
    return l


def part_two(graph, ps, e):
    shortest_paths = []
    for s in ps:
        try:
            l = nx.shortest_path_length(graph, s, e)
        except:
            pass
        shortest_paths.append(l)
    return min(shortest_paths)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.read()
    nodes, s, e, ps = parse_data(data)
    graph = get_graph(nodes)
    print(f"The answer for the 1st task is: {part_one(graph, s, e)}")
    print(f"The answer for the 2nd task is: {part_two(graph, ps, e)}")
