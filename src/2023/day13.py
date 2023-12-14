import numpy as np

from utils.utils import pull_input_directly


def check_for_mirrors(pattern, smudges=0):
    mirror_found = False
    val = 0
    # check rows
    for i in range(pattern.shape[0] - 1):
        num_rows = min(i + 1, pattern.shape[0] - i - 1)
        if (
            len(
                np.where(
                    pattern[i - num_rows + 1 : i + 1]
                    != np.flipud(pattern[i + 1 : i + 1 + num_rows])
                )[0]
            )
            == smudges
        ):
            val = 100 * (i + 1)
            mirror_found = True
            break

    if mirror_found:
        return val

    # check columns
    for i in range(pattern.shape[1] - 1):
        num_cols = min(i + 1, pattern.shape[1] - i - 1)
        if (
            len(
                np.where(
                    pattern[:, i - num_cols + 1 : i + 1]
                    != np.fliplr(pattern[:, i + 1 : i + 1 + num_cols])
                )[0]
            )
            == smudges
        ):
            val = i + 1
            break

    return val


if __name__ == "__main__":
    inp = [x.split("\\n") for x in pull_input_directly(2023, 13, delimiter="\\n\\n")]
    inp[-1] = inp[-1][:-1]
    patterns = [np.array([[*x] for x in y]) for y in inp]

    p1_res = [check_for_mirrors(p) for p in patterns]
    print(f"PART 1: {sum(p1_res)}")

    p2 = sum([check_for_mirrors(p, smudges=1) for p in patterns])
    print(f"PART 2: {p2}")
