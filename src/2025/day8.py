from itertools import combinations

import networkx as nx

from utils.utils import read_input


def calc_distance(box1, box2):
    x1, y1, z1 = box1
    x2, y2, z2 = box2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5


def bothparts(boxes):
    G = nx.Graph()
    for box in boxes:
        G.add_node(box)

    box_pairs = [(box1, box2, calc_distance(box1, box2)) for box1, box2 in combinations(boxes, 2)]
    box_pairs = sorted(box_pairs, key=lambda x: x[2])

    for i, (box1, box2, dist) in enumerate(box_pairs):
        G.add_edge(box1, box2, weight=dist)
        circuits = list(nx.connected_components(G))

        if len(circuits) == 1:
            print(f"Part 2: {box1[0] * box2[0]}")
            break

        if i == 1000:
            sorted_circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
            res = len(sorted_circuits[0]) * len(sorted_circuits[1]) * len(sorted_circuits[2])
            print(f"Part 1: {res}")


if __name__ == "__main__":
    boxes = [tuple(map(int, r.split(","))) for r in read_input(2025, 8, source="real")]
    bothparts(boxes)
