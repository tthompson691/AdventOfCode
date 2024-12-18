import networkx as nx
from networkx import NetworkXNoPath

from utils.utils import read_input


def dist(a, b):
    ax, ay = a
    bx, by = b
    return ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5


def update_graph(i, j, G, weight):
    if i + 1 < grid_size:
        G[i, j][i + 1, j]["weight"] = weight
    if j + 1 < grid_size:
        G[i, j][i, j + 1]["weight"] = weight
    if i - 1 >= 0:
        G[i, j][i - 1, j]["weight"] = weight
    if j - 1 >= 0:
        G[i, j][i, j - 1]["weight"] = weight

    return G


source = "real"

all_byte_falls = [tuple(map(int, x.split(","))) for x in read_input(2024, 18, source=source)]

grid_size = {"real": 71, "sample": 7}[source]

byte_falls = {
    "sample": all_byte_falls[:12],
    "real": all_byte_falls[:1024],
}[source]

### PART 1 ###
G = nx.grid_2d_graph(grid_size, grid_size, create_using=nx.DiGraph)

for i, j in G.nodes:
    weight = 1000 if (j, i) in byte_falls else 1
    G = update_graph(i, j, G, weight)

res = nx.astar_path(
    G, source=(0, 0), target=(grid_size - 1, grid_size - 1), heuristic=dist, cutoff=1000
)
print(f"PART 1: {len(res) - 1}")

### PART 2 ###
p2_byte_falls = {
    "sample": all_byte_falls[12:],
    "real": all_byte_falls[1024:],
}[source]

for x, y in p2_byte_falls:
    G = update_graph(y, x, G, 1000)
    try:
        res = nx.astar_path(
            G, source=(0, 0), target=(grid_size - 1, grid_size - 1), heuristic=dist, cutoff=1000
        )
    except NetworkXNoPath:
        print(f"PART 2: {x},{y}")
        break
