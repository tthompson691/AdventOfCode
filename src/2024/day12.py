import numpy as np

from utils.utils import read_input


def check_corners(i, j):
    # Identify a corner by looking at a 2x2 subarray around the current location
    # Num sides always = num corners in a shape
    global CORNERS
    plant = FULL_GARDEN[i, j]
    for di in [-1, 1]:
        for dj in [-1, 1]:
            sub_garden = {(i, j), (i + di, j), (i, j + dj), (i + di, j + dj)}
            if (
                len([x for x in sub_garden if FULL_GARDEN[*x] == plant]) in (1, 3)
                and sub_garden not in CORNERS
            ):
                CORNERS.append(sub_garden)
            elif (
                len([x for x in sub_garden if FULL_GARDEN[*x] == plant]) == 2
                and FULL_GARDEN[i + di, j + dj] == plant
            ):
                # edge case where two different regions of the same plant are
                # cattycorner to each other
                CORNERS.append(sub_garden)


def expand(i, j):
    global PERIMETER, AREA, COMPLETED_LOCS
    COMPLETED_LOCS.append((i, j))
    AREA += 1
    sub_perimeter = 4
    plant = FULL_GARDEN[i, j]
    for di in [-1, 1]:
        if (i + di, j) in COMPLETED_LOCS:
            sub_perimeter -= 1
        elif FULL_GARDEN[i + di, j] == plant:
            sub_perimeter -= 1
            expand(i + di, j)

    for dj in [-1, 1]:
        if (i, j + dj) in COMPLETED_LOCS:
            sub_perimeter -= 1
        elif FULL_GARDEN[i, j + dj] == plant:
            sub_perimeter -= 1
            expand(i, j + dj)

    check_corners(i, j)

    PERIMETER += sub_perimeter


garden = np.array([list(line) for line in read_input(2024, 12, source="real")])
# add a buffer around the entire garden perimeter so we don't have to worry about indexing errors
FULL_GARDEN = np.zeros((garden.shape[0] + 2, garden.shape[1] + 2), dtype=str)
FULL_GARDEN[1:-1, 1:-1] = garden

p1_price = p2_price = 0

for plant in np.unique(garden):
    plant_locs = list(map(tuple, np.argwhere(plant == FULL_GARDEN)))
    COMPLETED_LOCS = []
    while len(COMPLETED_LOCS) != len(plant_locs):
        next_plant = list(set(plant_locs).difference(set(COMPLETED_LOCS)))[0]
        PERIMETER = 0
        AREA = 0
        CORNERS = []
        expand(*next_plant)
        p1_price += PERIMETER * AREA
        p2_price += AREA * len(CORNERS)


print(f"PART 1: {p1_price}")
print(f"PART 2: {p2_price}")
