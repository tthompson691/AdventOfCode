from datetime import datetime

import networkx as nx
import numpy as np
from networkx import NetworkXNoPath

from utils.utils import read_input


def dist(a, b):
    ax, ay = a
    bx, by = b
    return ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5


source = "real"

all_byte_falls = [tuple(map(int, x.split(","))) for x in read_input(2024, 18, source=source)]

grid_size = {"real": 71, "sample": 7}[source]
grid = np.ones([grid_size, grid_size], dtype=int)

if source == "sample":
    byte_falls = all_byte_falls[:12]
elif source == "real":
    byte_falls = all_byte_falls[:1024]

for x, y in byte_falls:
    grid[y, x] = 1000
### PART 1 ###
start = datetime.now()

G = nx.grid_2d_graph(grid_size, grid_size, create_using=nx.DiGraph)

for i, j in G.nodes:
    if i + 1 < grid_size:
        G[i, j][i + 1, j]["weight"] = grid[i + 1, j]
    if j + 1 < grid_size:
        G[i, j][i, j + 1]["weight"] = grid[i, j + 1]
    if i - 1 >= 0:
        G[i, j][i - 1, j]["weight"] = grid[i - 1, j]
    if j - 1 >= 0:
        G[i, j][i, j - 1]["weight"] = grid[i, j - 1]

res = nx.astar_path(
    G, source=(0, 0), target=(grid_size - 1, grid_size - 1), heuristic=dist, cutoff=1000
)

print(f"P1 runtime: {datetime.now() - start}")

print(f"PART 1: {len(res) - 1}")

### PART 2 ###
if source == "sample":
    p2_byte_falls = all_byte_falls[12:]
elif source == "real":
    p2_byte_falls = all_byte_falls[1024:]

for x, y in p2_byte_falls:
    grid[y, x] = 1000
    if y + 1 < grid_size:
        G[y, x][y + 1, x]["weight"] = 1000
    if x + 1 < grid_size:
        G[y, x][y, x + 1]["weight"] = 1000
    if y - 1 >= 0:
        G[y, x][y - 1, x]["weight"] = 1000
    if x - 1 >= 0:
        G[y, x][y, x - 1]["weight"] = 1000

    try:
        res = nx.astar_path(
            G, source=(0, 0), target=(grid_size - 1, grid_size - 1), heuristic=dist, cutoff=1000
        )
    except NetworkXNoPath:
        print(f"PART 2: {x},{y}")
        break
