import numpy as np


def check_for_mirrors(pattern):
    mirror_found = False
    val = 0
    # check rows
    for i in range(pattern.shape[0] - 1):
        num_rows = min(i + 1, pattern.shape[0] - i - 1)
        if np.all(
            pattern[i - num_rows + 1 : i + 1] == np.flipud(pattern[i + 1 : i + 1 + num_rows])
        ):
            val = 100 * (i + 1)
            mirror_found = True
            break

    if mirror_found:
        return val

    # check columns
    for i in range(pattern.shape[1] - 1):
        num_cols = min(i + 1, pattern.shape[1] - i - 1)
        if np.all(
            pattern[:, i - num_cols + 1 : i + 1] == np.fliplr(pattern[:, i + 1 : i + 1 + num_cols])
        ):
            val = i + 1
            break

    return val


if __name__ == "__main__":
    with open(r"C:\Users\tthompson2\Documents\REPOS\AdventOfCode\src\2023\day13samp.txt") as f:
        inp = [x.splitlines() for x in f.read().split("\n\n")]

    # inp = [x.split("\\n") for x in pull_input_directly(2023, 13, delimiter="\\n\\n")]
    # inp[-1] = inp[-1][:-1]
    patterns = [np.array([[*x] for x in y]) for y in inp]

    ### PART 1 ###
    p1_res = [check_for_mirrors(p) for p in patterns]
    print(f"PART 1: {sum(p1_res)}")

    ### PART 2 (incomplete)###
    p2 = 0
    for n, p in enumerate(patterns):
        mirror_found = False
        for i, x in enumerate(p):
            for j, y in enumerate(x):
                p[i, j] = {"#": ".", ".": "#"}[y]
                val = check_for_mirrors(p)
                if val != 0 and val != p1_res[n]:
                    p2 += val
                    mirror_found = True
                    break
                else:
                    p[i, j] = {"#": ".", ".": "#"}[p[i, j]]

            if mirror_found:
                break

        # if not mirror_found:
        #     p2 += p1_res[n]

    print(f"PART 2: {p2}")
