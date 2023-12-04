import numpy as np

from utils.utils import pull_input_directly


def check_view(forest_array, i, j):
    try:
        score = list(list(forest_array) < forest[i, j]).index(False) + 1
    except ValueError:
        score = len(list(forest_array))

    return score


if __name__ == "__main__":
    forest = np.array([list(map(int, i)) for i in pull_input_directly(2022, 8)[:-1]])

    part1 = sum(
        any(
            [
                all(forest[i, :j] < forest[i, j]),
                all(forest[i, (j + 1) :] < forest[i, j]),
                all(forest[:i, j] < forest[i, j]),
                all(forest[(i + 1) :, j] < forest[i, j]),
            ]
        )
        for i in range(forest.shape[1])
        for j in range(forest.shape[0])
    )

    print(part1)

    part2 = max(
        check_view(list(reversed(forest[i, :j])), i, j)
        * check_view(forest[i, (j + 1) :], i, j)
        * check_view(list(reversed(forest[:i, j])), i, j)
        * check_view(forest[(i + 1) :, j], i, j)
        for i in range(1, forest.shape[1] - 1)
        for j in range(1, forest.shape[0] - 1)
    )

    print(part2)
