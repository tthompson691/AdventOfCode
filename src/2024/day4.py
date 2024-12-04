import numpy as np

from utils.utils import read_input


def search_left(i, j):
    if j >= 3 and "".join(WORD_SEARCH[i, j - 3 : j + 1]) == "SAMX":
        return 1
    else:
        return 0


def search_right(i, j):
    if j <= COLS - 4 and "".join(WORD_SEARCH[i, j : j + 4]) == "XMAS":
        return 1
    else:
        return 0


def search_up(i, j):
    if i >= 3 and "".join(WORD_SEARCH[i - 3 : i + 1, j]) == "SAMX":
        return 1
    else:
        return 0


def search_down(i, j):
    if i <= ROWS - 4 and "".join(WORD_SEARCH[i : i + 4, j]) == "XMAS":
        return 1
    else:
        return 0


def search_upleft(i, j):
    if i >= 3 and j >= 3 and "".join(WORD_SEARCH[i - x, j - x] for x in range(4)) == "XMAS":
        return 1
    else:
        return 0


def search_upright(i, j):
    if i >= 3 and j <= COLS - 4 and "".join(WORD_SEARCH[i - x, j + x] for x in range(4)) == "XMAS":
        return 1
    else:
        return 0


def search_downright(i, j):
    if (
        i <= ROWS - 4
        and j <= COLS - 4
        and "".join(WORD_SEARCH[i + x, j + x] for x in range(4)) == "XMAS"
    ):
        return 1
    else:
        return 0


def search_downleft(i, j):
    if i <= ROWS - 4 and j >= 3 and "".join(WORD_SEARCH[i + x, j - x] for x in range(4)) == "XMAS":
        return 1
    else:
        return 0


def run_all_searches(i, j):
    return sum(
        [
            search_left(i, j),
            search_right(i, j),
            search_up(i, j),
            search_down(i, j),
            search_upleft(i, j),
            search_upright(i, j),
            search_downright(i, j),
            search_downleft(i, j),
        ]
    )


def p2_search(i, j):
    if "".join(WORD_SEARCH[i + x, j + x] for x in range(-1, 2)) in ["MAS", "SAM"] and "".join(
        WORD_SEARCH[i - x, j + x] for x in range(-1, 2)
    ) in ["MAS", "SAM"]:
        return 1
    else:
        return 0


WORD_SEARCH = np.array([list(x) for x in read_input(2024, 4, source="real")])
ROWS, COLS = WORD_SEARCH.shape

print(f"PART 1: {sum([run_all_searches(i, j) for i, j in np.argwhere(WORD_SEARCH=='X')])}")


p2_search_points = [
    x for x in np.argwhere(WORD_SEARCH == "A") if 0 < x[0] < ROWS - 1 and 0 < x[1] < COLS - 1
]

print(f"PART 2: {sum([p2_search(i, j) for i, j in p2_search_points])}")
