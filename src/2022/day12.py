import networkx.exception

from utils.utils import pull_input_directly
import networkx as nx
import numpy as np


def dist(*args):
    (x1, y1, val1) = args[0]
    (x2, y2, val2) = args[1]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


if __name__ == "__main__":
    # turn all letters into numbers
    heightmap = [[ord(j) for j in i] for i in pull_input_directly(2022, 12)[:-1]]

    # hard code start and end because I can
    start = (20, 0, 97)
    end = (20, 46, 122)

    # convert weird resulting numbers for "S" and "E" to numbers better suited for this graph traversal
    heightmap[start[0]][start[1]] = ord("a")
    heightmap[end[0]][end[1]] = ord("z")

    G = nx.DiGraph()
    # add nodes
    for i, row in enumerate(heightmap):
        for j, val in enumerate(row):
            G.add_node((i, j, val))

    # add edges
    for node in G.nodes:
        i = node[0]
        j = node[1]
        val = node[2]
        neighbor_coords = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for znode in G.nodes:
            if (znode[0], znode[1]) in neighbor_coords and znode[2] <= val + 1:
                if node[0] == 21 and node[1] == 20:
                    print("d")
                G.add_edge(node, znode)

    part1_path = nx.astar_path(G, source=start, target=end, heuristic=dist)

    print(len(part1_path) - 1)

    ## PART 2 ##
    all_paths = []
    for node in G.nodes:
        if node[2] == ord("a"):
            try:
                all_paths.append(len(nx.astar_path(G, source=node, target=end, heuristic=dist)) - 1)
            except networkx.exception.NetworkXNoPath:
                continue

    print(min(all_paths))


