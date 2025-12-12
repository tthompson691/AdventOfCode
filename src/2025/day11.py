import networkx as nx

from utils.utils import read_input


def part1(devices):
    G = nx.DiGraph()
    for device in [d[0] for d in devices]:
        G.add_node(device)

    for source, destinations in devices:
        for destination in destinations:
            G.add_edge(source, destination)

    p2 = None

    path_pairs = [
        ["svr", "fft"],
        ["svr", "dac"],
        ["fft", "dac"],
        ["dac", "fft"],
        ["dac", "out"],
        ["fft", "out"],
    ]
    for start, end in path_pairs:
        paths = list(nx.all_simple_paths(G, start, end))
        if paths == []:
            continue
        if not p2:
            p2 = len(paths)
        else:
            p2 *= len(paths)

    # paths = list(nx.all_simple_paths(G, "svr", "out"))
    # paths = [p for p in paths if "fft" in p and "dac" in p]
    # p2 = len(paths)

    print(f"Part 1: {p2}")
    # print(f"Part 2: {len([p for p in all_paths if required_nodes.issubset(p)])}")


if __name__ == "__main__":
    data = read_input(2025, 11, source="real")
    devices = [(x, y.split(" ")) for x, y in (line.split(": ") for line in data)]
    part1(devices)
