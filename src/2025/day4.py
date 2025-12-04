import numpy as np

from utils.utils import read_input


def check_neighbors(x, y, warehouse):
    rolls = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if x + dx not in range(warehouse.shape[0]) or y + dy not in range(warehouse.shape[1]):
                continue

            if warehouse[x + dx, y + dy] == "@":
                rolls += 1

    return rolls


def process_warehouse(warehouse):
    accessible = []
    for x in range(warehouse.shape[0]):
        for y in range(warehouse.shape[1]):
            if warehouse[x, y] == "@" and check_neighbors(x, y, warehouse) < 5:
                accessible.append((x, y))

    return accessible


def day4(warehouse):
    accessible = process_warehouse(warehouse)
    print(f"Part 1: {len(accessible)}")


def day4_p2(warehouse):
    total_rolls_removed = 0
    while True:
        rolls_to_remove = process_warehouse(warehouse)
        if not rolls_to_remove:
            break

        total_rolls_removed += len(rolls_to_remove)
        for x, y in rolls_to_remove:
            warehouse[x, y] = "."

    print(f"Part 2: {total_rolls_removed}")


if __name__ == "__main__":
    data = read_input(2025, 4, source="real")
    warehouse = np.array([list(d) for d in data])
    day4(warehouse)
    day4_p2(warehouse)
