from utils.utils import read_input
import numpy as np


def part1(manifold):
    start = np.where(manifold == 'S')
    manifold[start[0] + 1, start[1]] = '|'
    splitters_activated = 0
    for i, row in enumerate(manifold):
        if "S" in row:
            continue
        incoming_beams = [(i-1, c) for c in np.where(manifold[i-1] == "|")[0]]
        for incoming_beam in incoming_beams:
            if manifold[i, incoming_beam[1]] == '.':
                manifold[i, incoming_beam[1]] = '|'
            elif manifold[i, incoming_beam[1]] == '^':
                splitters_activated += 1
                manifold[i, incoming_beam[1]-1] = '|'
                manifold[i, incoming_beam[1]+1] = '|'

    print(f"Part 1: {splitters_activated}")


def part2(manifold):
    stack = [np.where(manifold == "S"[0])]
    timelines = 0
    while stack:
        position = stack.pop()
        # print(position)
        if position[0] == manifold.shape[0] - 1:
            timelines += 1
            continue
        if manifold[position[0] + 1, position[1]] == '.':
            stack.append((position[0] + 1, position[1]))
        elif manifold[position[0] + 1, position[1]] == '^':
            stack.append((position[0] + 1, position[1] - 1))
            stack.append((position[0] + 1, position[1] + 1))

    print(f"Part 2: {timelines}")


if __name__ == "__main__":
    data = read_input(2025, 7, source="real")
    manifold = np.array([[x for x in line] for line in data])
    
    # part1(manifold)
    part2(manifold)