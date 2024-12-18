from collections import deque

import numpy as np

from utils.utils import read_input


def get_valid_neighbors(heading):
    return {
        (0, 1): [(1, 0), (-1, 0), (0, 1)],
        (0, -1): [(1, 0), (-1, 0), (0, -1)],
        (1, 0): [(1, 0), (0, 1), (0, -1)],
        (-1, 0): [(-1, 0), (0, 1), (0, -1)],
    }[heading]


maze = np.array([list(x) for x in read_input(2024, 16, source="real")])

start = np.argwhere(maze == "S")[0]
end = np.argwhere(maze == "E")[0]
heading = (0, 1)
nodes = deque([(start[0], start[1], heading, 0, [])])
best_score = 0
visited = {}
while nodes:
    i, j, heading, score, history = nodes.pop()
    visited[i, j, heading] = score

    if score > best_score and best_score != 0:
        continue

    if maze[i, j] == "E" and (score <= best_score or best_score == 0):
        if score < best_score or best_score == 0:
            winning_paths = history
            best_score = score
            continue
        elif score == best_score:
            winning_paths.extend(history)
            continue

    for di, dj in get_valid_neighbors(heading):
        if maze[i + di, j + dj] in [".", "E"] and (
            (i + di, j + dj, heading) not in visited or visited[i + di, j + dj, heading] > score
        ):
            if (di, dj) == heading:
                nodes.append((i + di, j + dj, heading, score + 1, history + [(i + di, j + dj)]))
            else:
                nodes.append((i + di, j + dj, (di, dj), score + 1001, history + [(i + di, j + dj)]))


print(f"PART 1: {best_score}")
print(f"PART 2: {len(set(winning_paths)) + 1}")
