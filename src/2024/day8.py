from utils.utils import read_input
import numpy as np
from itertools import permutations

def calculate_antinodes(ant1, ant2):
    P2_ANTINODES.append(tuple(ant1))
    P2_ANTINODES.append(tuple(ant2))
    di = ant1[0] - ant2[0]
    dj = ant1[1] - ant2[1]
    multiplier = 1
    ant1_valid = True
    ant2_valid = True
    while ant1_valid or ant2_valid:
        antinode_1 = (ant1[0] + (di * multiplier), ant1[1] + (dj * multiplier))
        antinode_2 = (ant2[0] - (di * multiplier), ant2[1] - (dj * multiplier))
        if ant1_valid and 0 <= antinode_1[0] <= ROWS - 1 and 0 <= antinode_1[1] <= COLS - 1:
            if multiplier == 1:
                P1_ANTINODES.append(antinode_1)
                P2_ANTINODES.append(antinode_1)
            else:
                P2_ANTINODES.append(antinode_1)
        else:
            ant1_valid = False

        if ant2_valid and 0 <= antinode_2[0] <= ROWS - 1 and 0 <= antinode_2[1] <= COLS - 1:
            if multiplier == 1:
                P1_ANTINODES.append(antinode_2)
                P2_ANTINODES.append(antinode_2)
            else:
                P2_ANTINODES.append(antinode_2)
        else:
            ant2_valid = False

        multiplier += 1


ant_map = np.array([list(r) for r in read_input(2024, 8, source="real")])
ANTINODE_MAP = ant_map.copy()
ant_names = [x for x in np.unique(ant_map) if x != "."]

ROWS = len(ant_map)
COLS = len(ant_map[0])
P1_ANTINODES = []
P2_ANTINODES = []

p1_total = []

for ant_name in ant_names:
    ant_locs = np.argwhere(ant_map==ant_name)
    ant_pairs = list(permutations(ant_locs, 2))
    [calculate_antinodes(*ant_pair) for ant_pair in ant_pairs]

print(f"PART 1: {len(set(P1_ANTINODES))}")
print(f"PART 2: {len(set(P2_ANTINODES))}")
