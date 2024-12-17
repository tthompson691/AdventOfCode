from collections import deque

import numpy as np

from utils.utils import read_input

# def highlight_path(maze, path):
#     for i, j in path:
#         maze[i, j] = "X"

#     print(maze)

# def step_once(i, j, score, visited, heading=None):
#     global FINAL_SCORES
#     if maze[i, j] == "E":
#         FINAL_SCORES.append((score, visited))

#     for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#         if maze[i + di, j + dj] in [".", "E"] and (i + di, j + dj) not in visited:
#             # visited.append((i + di, j + dj))
#             if heading and (di, dj) != heading:
#                 step_once(
# i + di, j + dj, score=score+1001, visited=visited + [(i+di, j+dj)], heading=(di, dj))
#             else:
#                 step_once(
# i + di, j + dj, score=score+1, visited=visited + [(i+di, j+dj)], heading=(di, dj))


#     return


def dist(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


FINAL_SCORES = []
maze = np.array([list(x) for x in read_input(2024, 16, source="sample")])

# G = nx.from_numpy_array(
#     maze,
#     create_using=nx.DiGraph,
#     edge_attr="value"
# )


start = np.argwhere(maze == "S")[0]
end = np.argwhere(maze == "E")[0]
nodes = deque([start[0], start[1], (0, 1), 0])
best_score = 0
# astar = nx.astar_path(G, source=tuple(start), target=tuple(end), heuristic=dist)
while nodes:
    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for node in nodes:
        pass


# step_once(*start, score=0, visited=[tuple(start)], heading=(0, 1))
# print(f"PART 1: {min(x[0] for x in FINAL_SCORES)}")
