import numpy as np

from utils.utils import read_input


def find_next_steps(i, j):
    global P1_SCORE, P2_SCORE, PEAKS_FOUND
    cur_val = VOL_MAP[i, j]
    if cur_val == 9:
        if PART == 1 and (i, j) not in PEAKS_FOUND:
            PEAKS_FOUND.append((i, j))
            P1_SCORE += 1
        elif PART == 2:
            P2_SCORE += 1

    for di in [-1, 1]:
        if 0 <= i + di < MAP_ROWS and VOL_MAP[i + di, j] == cur_val + 1:
            find_next_steps(i + di, j)

    for dj in [-1, 1]:
        if 0 <= j + dj < MAP_COLS and VOL_MAP[i, j + dj] == cur_val + 1:
            find_next_steps(i, j + dj)

    return


VOL_MAP = np.array([list(x) for x in read_input(2024, 10, source="real")], dtype=int)
MAP_ROWS = VOL_MAP.shape[0]
MAP_COLS = VOL_MAP.shape[1]

trailheads = np.argwhere(VOL_MAP == 0)
P1_SCORE = 0
P2_SCORE = 0

for trailhead in trailheads:
    PEAKS_FOUND = []
    for PART in 1, 2:
        find_next_steps(*trailhead)

print(f"PART 1: {P1_SCORE}")
print(f"PART 2: {P2_SCORE}")
