import numpy as np

from utils.utils import read_input


def find_next_steps(i, j, cur_val, part):
    global P1_SCORE, P2_SCORE, PEAKS_FOUND
    if cur_val == 9:
        if part == 1 and (i, j) not in PEAKS_FOUND:
            PEAKS_FOUND.append((i, j))
            P1_SCORE += 1
        elif part == 2:
            P2_SCORE += 1

    for di in [-1, 1]:
        if 0 <= i + di < MAP_ROWS and VOL_MAP[i + di, j] == cur_val + 1:
            find_next_steps(i + di, j, cur_val=cur_val + 1, part=part)

    for dj in [-1, 1]:
        if 0 <= j + dj < MAP_COLS and VOL_MAP[i, j + dj] == cur_val + 1:
            find_next_steps(i, j + dj, cur_val=cur_val + 1, part=part)

    return


VOL_MAP = np.array([list(x) for x in read_input(2024, 10, source="real")], dtype=int)
MAP_ROWS = VOL_MAP.shape[0]
MAP_COLS = VOL_MAP.shape[1]

trailheads = np.argwhere(VOL_MAP == 0)
P1_SCORE = 0
P2_SCORE = 0

for trailhead in trailheads:
    old_score = P1_SCORE
    PEAKS_FOUND = []
    for part in 1, 2:
        find_next_steps(*trailhead, cur_val=0, part=part)

print(f"PART 1: {P1_SCORE}")
print(f"PART 2: {P2_SCORE}")
