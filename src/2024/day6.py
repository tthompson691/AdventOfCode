import numpy as np
from joblib import Parallel, delayed

from utils.utils import read_input


def simulate_patrol(guard_map):
    spots_patrolled = 0
    num_repeats = 0
    while True:
        position = np.argwhere(guard_map == "^")[0]
        guard_map[*position] = "X"
        try:
            stop_point = np.argwhere(guard_map[: position[0], position[1]] == "#")[-1][-1]
        except IndexError:
            guard_map[: position[0], position[1]] = "X"
            spots_patrolled = np.count_nonzero(guard_map == "X")
            break

        guard_map[stop_point + 1 : position[0], position[1]] = "X"
        if (
            np.count_nonzero(guard_map == "X") == spots_patrolled
            and len(guard_map[stop_point + 1 : position[0], position[1]]) != 0
        ):
            num_repeats += 1
            if num_repeats == 4:
                # loop found
                # Honestly, I don't know why this works, but it does
                return "Loopy"

        spots_patrolled = np.count_nonzero(guard_map == "X")

        position = (stop_point + 1, position[1])
        guard_map[*position] = "^"
        guard_map = np.rot90(guard_map)

    return spots_patrolled


def p2(empty_spot):
    # Can you say brute force?
    modded_guard_map = original_guard_map.copy()
    modded_guard_map[*empty_spot] = "#"
    if simulate_patrol(modded_guard_map) == "Loopy":
        return 1
    else:
        return 0


original_guard_map = np.array([list(x) for x in read_input(2024, 6, source="real")])

print(f"PART 1: {simulate_patrol(original_guard_map.copy())}")

p2_res = Parallel(n_jobs=-1)(
    delayed(p2)(empty_spot) for empty_spot in np.argwhere(original_guard_map == ".")
)


print(f"PART 2: {sum(p2_res)}")
