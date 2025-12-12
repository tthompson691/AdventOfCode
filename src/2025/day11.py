import networkx as nx

from utils.utils import read_input


def part1(devices):
    G = nx.DiGraph()
    for device in [d[0] for d in devices]:
        G.add_node(device)

    for source, destinations in devices:
        for destination in destinations:
            G.add_edge(source, destination)

    print(f"Part 1: {len(list(nx.all_simple_paths(G, 'you', 'out')))}")


def travel_to_next(
    start,
    end,
    devices,
    cache,
):
    destinations = devices[start]
    for destination in destinations:
        if destination == "out" and end != "out":
            return 0
        if destination == end:
            return 1
        elif destination in cache:
            return cache[destination]
        else:
            cache[destination] = 0
            cache[destination] += travel_to_next(destination, end, devices, cache)

    return cache


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

    node_pairs = [("svr", "fft"), ("fft", "dac"), ("dac", "out")]

    for start, end in node_pairs:
        res = travel_to_next(start, end, devices, {})
        res


#         # if cur_node == end:
#         #     return 1

# def part2b(devices):
#     start = "svr"
#     # end = "fft"
#     stuff = []
#     stack = ["fft"]
#     while stack:
#         end = stack.pop()
#         valid_sources = [d for d in devices if end in devices[d]]
#         stack.extend([d for d in valid_sources if d != start])
#         stuff.append(len(valid_sources))

#     stuff


if __name__ == "__main__":
    data = read_input(2025, 11, source="sample")
    devices = {x: y.split(" ") for x, y in (line.split(": ") for line in data)}
    # part1(devices)
    part2(devices)
