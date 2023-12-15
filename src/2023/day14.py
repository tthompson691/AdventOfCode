from collections import Counter

import numpy as np

from utils import pull_input_directly


def rocknroll(rocks, dir="N"):
    num_rotations = {"N": (0, 0), "E": (1, 3), "S": (2, 2), "W": (3, 1)}[dir]

    for _ in range(num_rotations[0]):
        rocks = np.rot90(rocks)

    for i, x in enumerate(rocks):
        for j, y in enumerate(x):
            if y == "O":
                empty_space = 0
                z = i - 1
                while rocks[z, j] == "." and z >= 0:
                    empty_space += 1
                    z -= 1

                if empty_space != 0:
                    rocks[i, j] = "."
                    rocks[i - empty_space, j] = "O"

    for _ in range(num_rotations[1]):
        rocks = np.rot90(rocks)

    return rocks


def calc_load(rocks):
    return sum([len(np.where(i == "O")[0]) * (rocks.shape[0] - n) for n, i in enumerate(rocks)])


if __name__ == "__main__":
    rocks = np.array([[*x] for x in pull_input_directly(2023, 14)[:-1]])

    print(f"PART 1: {calc_load(rocknroll(rocks))}")

    ## PART 2 ##
    rocks = np.array([[*x] for x in pull_input_directly(2023, 14)[:-1]])
    dirs = ["N", "W", "S", "E"]
    loads = []
    for _ in range(500):
        for dir in dirs:
            rocks = rocknroll(rocks, dir=dir)

        loads.append(calc_load(rocks))

    # we don't need to loop a billion times, we just need to loop enough to establish
    # a pattern. After investigating my input, I get a pattern of length 34. We can
    # extrapolate the billionth rock configuration from there

    occurrences = {k: v for k, v in Counter(loads).items() if v > 1}
    pat_length = 34
    for i, load in enumerate(loads):
        if load in occurrences:
            # begin pattern
            pat_start_i = i
            pattern = loads[i : i + pat_length]
            break

    print(f"PART 2: {pattern[(1_000_000_000 - pat_start_i - 1) % pat_length]}")
