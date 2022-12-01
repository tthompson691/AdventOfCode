from utils import read_input
import numpy as np
import networkx as nx


def get_neighbors(pos):
    i = pos[0]
    j = pos[1]
    nu = nd = nl = nr = None
    # up
    if i > 0:
        nu = (i - 1, j)
    # down
    if i < big_cavern.shape[0] - 1:
        nd = (i + 1, j)
    # left
    if j > 0:
        nl = (i, j - 1)
    # right
    if j < big_cavern.shape[1] - 1:
        nr = (i, j + 1)
    return [neighbor for neighbor in [nu, nd, nl, nr] if neighbor is not None]


def risk(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


if __name__ == "__main__":
    cavern_list = [list(map(int, i)) for i in read_input("day15_input.txt")]
    cavern = np.array(cavern_list)

    # other_caverns = [np.where(((cavern + i) % 10) == 0, 1, (cavern + i) % 10) for i in range(1, 5)]
    other_caverns = {0: cavern}
    for i in range(1, 9):
        other_caverns[i] = np.where(
            ((other_caverns[i - 1] + 1) % 10) == 0, 1, (other_caverns[i - 1] + 1) % 10
        )

    # construct horizontal cavern sections first
    fat_rows = []
    for i in range(0, 5):
        fat_rows.append(
            np.concatenate([other_caverns[j] for j in range(i, i + 5)], axis=1)
        )

    big_cavern = np.concatenate(fat_rows)

    G = nx.DiGraph()

    # populate nodes
    for i, x in enumerate(big_cavern):
        for j, y in enumerate(x):
            G.add_node((i, j))

    # populate edges
    for node in G.nodes:
        neighbors = get_neighbors(node)
        for neighbor in neighbors:
            G.add_edge(node, neighbor, weight=big_cavern[neighbor] + big_cavern[node])

    a = nx.astar_path(
        G,
        (0, 0),
        (big_cavern.shape[0] - 1, big_cavern.shape[1] - 1),
        heuristic=risk,
        weight="weight",
    )

    risk_total = 0
    for g in a[1:]:
        risk_total += big_cavern[g]

    print(f"part 1: {risk_total}")
