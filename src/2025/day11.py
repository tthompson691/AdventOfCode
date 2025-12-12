import networkx as nx

from utils.utils import read_input


def part1(devices):
    G = nx.DiGraph()
    for device in [d[0] for d in devices]:
        G.add_node(device)

    for source, destinations in devices.items():
        for destination in destinations:
            G.add_edge(source, destination)

    print(f"Part 1: {len(list(nx.all_simple_paths(G, 'you', 'out')))}")


def travel_to_next(
    current_node,
    end,
    devices,
    cache,
):
    if current_node == "out":
        return 0
    next_nodes = devices[current_node]
    cache[current_node] = 0
    for next_node in next_nodes:
        if next_node == "out" and end != "out":
            cache[current_node] = 0
        if next_node == end:
            cache[current_node] = 1
        elif next_node in cache:
            cache[current_node] += cache[next_node]
        else:
            cache[current_node] += travel_to_next(next_node, end, devices, cache)

    return cache[current_node]


def part2(devices):
    """
    1) nx graph does not scale for part 2
    2) there are no paths from 'dac' to 'fft', even though the prompt says there might be
    3) we have to find 3 separate path groups and multiply their counts together:
       - from 'svr' to 'fft'
       - from 'fft' to 'dac'
       - from 'dac' to 'out'
    4) going to try memoized recursion
    """

    node_pairs = [
        ("svr", "fft"),
        ("fft", "dac"),
        ("dac", "out")
    ]
    p2 = 1
    for start, end in node_pairs:
        res = travel_to_next(start, end, devices, {})
        p2 *= res

    print(f"Part 2: {p2}")


if __name__ == "__main__":
    data = read_input(2025, 11, source="real")
    devices = {x: y.split(" ") for x, y in (line.split(": ") for line in data)}
    part1(devices)
    part2(devices)
