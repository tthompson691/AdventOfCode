from itertools import combinations

import matplotlib.pyplot as plt
from shapely import Polygon
from shapely.geometry import box

from utils.utils import read_input


def calc_area(tile1, tile2):
    x1, y1 = tile1
    x2, y2 = tile2

    return abs(x1 - x2 + 1) * abs(y1 - y2 + 1)


def part1(tiles):
    tile_combos = list(combinations(tiles, 2))
    rectangle_areas = sorted(
        [((t1, t2), calc_area(t1, t2)) for t1, t2 in tile_combos], key=lambda x: x[1], reverse=True
    )
    print(f"Part 1: {rectangle_areas[0][1]}")

    tiles = tiles + [tiles[0]]  # close the loop
    floor = Polygon(tiles)
    x, y = floor.exterior.xy
    plt.plot(x, y)
    plt.show()

    for (v1, v2), rectangle_area in rectangle_areas:
        x1, y1 = v1
        x2, y2 = v2
        rectangle = box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
        if floor.contains(rectangle):
            print(f"Part 2: {rectangle_area}")
            break


# def part2(tiles):
#     # lol I knew part 1 wouldn't scale
#     # max_c = max(x for x, y in tiles) + 1
#     # max_r = max(y for x, y in tiles) + 1
#     # floor = np.zeros((max_r, max_c), dtype=int)
#     tiles = tiles + [tiles[0]]  # close the loop
#     # for i in range(len(tiles) - 1):
#     #     c1, r1 = tiles[i]
#     #     c2, r2 = tiles[i+1]
#     #     floor[r1, c1] = 1
#     #     floor[r2, c2] = 1

#     #     if c1 == c2:
#     #         floor[min(r1, r2)+1:max(r1, r2), c1] = 2
#     #     elif r1 == r2:
#     #         floor[r1, min(c1, c2)+1:max(c1, c2)] = 2  # fill in the rectangle
#     floor = Polygon(tiles)

#     floor


if __name__ == "__main__":
    tiles = [tuple(map(int, x.split(","))) for x in read_input(2025, 9, source="real")]
    part1(tiles)
    # part2(tiles)
