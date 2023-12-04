import random
import re
from string import ascii_letters

import numpy as np

from utils.utils import pull_input_directly


def get_neighbors(_array, indices):
    neighbors = []
    x_range = range(_array.shape[0])
    y_range = range(_array.shape[1])
    for i in indices:
        x, y = i
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if x + dx in x_range and y + dy in y_range:
                    neighbors.append((x + dx, y + dy))

    return list(set(neighbors).difference(set(indices)))


def generate_random_letters():
    return "".join(random.choices(ascii_letters, k=10))


if __name__ == "__main__":
    engine = np.array([[*x] for x in pull_input_directly(2023, 3)[:-1]])

    num_found = ""
    num_indices = []
    num_dict = {}
    ans = []
    star_indices = []
    for x in range(engine.shape[0]):
        for y in range(engine.shape[1]):
            val = engine[x][y]
            if val == "*":
                star_indices.append((x, y))
            if bool(re.search("[0-9]", val)):
                num_found += val
                num_indices += [(x, y)]
            else:
                if num_found != "":
                    num_dict[num_found + generate_random_letters()] = num_indices
                    neighbors = get_neighbors(engine, num_indices)
                    if any([engine[i][j] in "!@#$%^&*()_+=-/" for i, j in neighbors]):
                        ans.append(int(num_found))

                num_found = ""
                num_indices = []

    p2_sum = 0
    for star_index in star_indices:
        star_neighbors = get_neighbors(engine, [star_index])
        adjacent_nums = [
            num
            for num in num_dict
            if len(set(star_neighbors).intersection(set(num_dict[num]))) != 0
        ]
        if len(adjacent_nums) == 2:
            p2_sum += int(re.findall("[0-9]+", adjacent_nums[0])[0]) * int(
                re.findall("[0-9]+", adjacent_nums[1])[0]
            )

    print(f"PART 1: {sum(ans)}")
    print(f"PART 2: {p2_sum}")
