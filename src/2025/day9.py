from itertools import combinations

from shapely import Polygon
from shapely.geometry import box

from utils.utils import read_input


def calc_area(tile1, tile2):
    x1, y1 = tile1
    x2, y2 = tile2

    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def both_parts(tiles):
    tile_combos = list(combinations(tiles, 2))
    rectangle_areas = sorted(
        [((t1, t2), calc_area(t1, t2)) for t1, t2 in tile_combos], key=lambda x: x[1], reverse=True
    )
    print(f"Part 1: {rectangle_areas[0][1]}")

    tiles = tiles + [tiles[0]]  # close the loop
    floor = Polygon(tiles)

    for (v1, v2), rectangle_area in rectangle_areas:
        x1, y1 = v1
        x2, y2 = v2
        rectangle = box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
        if floor.covers(rectangle):
            print(f"Part 2: {rectangle_area}")
            break


if __name__ == "__main__":
    tiles = [tuple(map(int, x.split(","))) for x in read_input(2025, 9, source="real")]
    both_parts(tiles)
