from utils.utils import pull_input_directly
import numpy as np
from itertools import permutations

def get_distance(_galaxies, multiplier=1):
    distance = 0
    for a, b in permutations(galaxies, r=2):
        extra_x = sum([z in range(min(a[0], b[0]), max(a[0], b[0])) for z in empty_x]) * multiplier
        extra_y = sum([z in range(min(a[1], b[1]), max(a[1], b[1])) for z in empty_y]) * multiplier

        distance += (abs(a[0] - b[0]) + abs(a[1] - b[1]) + extra_x + extra_y)

    return distance

if __name__ == "__main__":
    universe = np.array([[*x] for x in pull_input_directly(2023, 11)[:-1]])
    empty_x = [i for i, row in enumerate(universe) if "#" not in row]
    empty_y = [i for i, row in enumerate(universe.T) if "#" not in row]
    galaxies = list(zip(*np.where(universe=="#")))
    distance = get_distance(galaxies)
    print(f"PART 1: {int(distance / 2)}")
    distance2 = get_distance(galaxies, multiplier=999_999)
    print(f"PART 2: {int(distance2/2)}")

