import numpy as np

from utils.utils import read_input


def part1(manifold):
    start = np.where(manifold == "S")
    manifold[start[0] + 1, start[1]] = "|"
    splitters_activated = 0
    for i, row in enumerate(manifold):
        if "S" in row:
            continue
        incoming_beams = [(i - 1, c) for c in np.where(manifold[i - 1] == "|")[0]]
        for incoming_beam in incoming_beams:
            if manifold[i, incoming_beam[1]] == ".":
                manifold[i, incoming_beam[1]] = "|"
            elif manifold[i, incoming_beam[1]] == "^":
                splitters_activated += 1
                manifold[i, incoming_beam[1] - 1] = "|"
                manifold[i, incoming_beam[1] + 1] = "|"

    print(f"Part 1: {splitters_activated}")


def part2(manifold, i, j, cache):
    if (i, j) in cache:
        return cache[i, j]

    if i == manifold.shape[0] - 1:
        return 1
    if manifold[i + 1, j] == ".":
        cache[i, j] = part2(manifold, i + 1, j, cache)
        return cache[i, j]
    elif manifold[i + 1, j] == "^":
        cache[i, j] = part2(manifold, i + 1, j - 1, cache) + part2(manifold, i + 1, j + 1, cache)
        return cache[i, j]


if __name__ == "__main__":
    data = read_input(2025, 7, source="real")
    manifold = np.array([[x for x in line] for line in data])
    manifold2 = manifold.copy()
    part1(manifold)
    start = np.where(manifold2 == "S")
    res = part2(manifold2, start[0][0], start[1][0], {})
    print(f"Part 2: {res}")
