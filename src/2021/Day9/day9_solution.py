from utils import read_input
import numpy as np


class Basin:
    def __init__(self, i, j):
        self.start_i = i
        self.start_j = j
        self.start = BasinPoint(i, j)
        self.points = [self.start]
        self.all_contained_coords = [(i, j)]

    def expand_up(self, point_i, point_j):
        if point_i > 0 and (point_i - 1, point_j) not in self.all_contained_coords:
            if array[point_i - 1][point_j] != 9:
                self.points.append(BasinPoint(point_i - 1, point_j))
                self.all_contained_coords.append((point_i - 1, point_j))

        return True

    def expand_down(self, point_i, point_j):
        if (
            point_i < array.shape[0] - 1
            and (point_i + 1, point_j) not in self.all_contained_coords
        ):
            if array[point_i + 1][point_j] != 9:
                self.points.append(BasinPoint(point_i + 1, point_j))
                self.all_contained_coords.append((point_i + 1, point_j))

        return True

    def expand_left(self, point_i, point_j):
        if point_j > 0 and (point_i, point_j - 1) not in self.all_contained_coords:
            if array[point_i][point_j - 1] != 9:
                self.points.append(BasinPoint(point_i, point_j - 1))
                self.all_contained_coords.append((point_i, point_j - 1))

        return True

    def expand_right(self, point_i, point_j):
        if (
            point_j < array.shape[1] - 1
            and (point_i, point_j + 1) not in self.all_contained_coords
        ):
            if array[point_i][point_j + 1] != 9:
                self.points.append(BasinPoint(point_i, point_j + 1))
                self.all_contained_coords.append((point_i, point_j + 1))

        return True

    def do_all_the_expanding(self):
        while not all(point.has_expanded for point in self.points):
            for point in self.points:
                if not point.has_expanded:
                    ex_u = self.expand_up(point.i, point.j)
                    ex_d = self.expand_down(point.i, point.j)
                    ex_l = self.expand_left(point.i, point.j)
                    ex_r = self.expand_right(point.i, point.j)

                point.has_expanded = True


class BasinPoint:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.has_expanded = False


def check_neighbors(i, j, array):
    nu = nd = nl = nr = None

    if i > 0:
        nu = array[i - 1][j]

    if i < array.shape[0] - 1:
        nd = array[i + 1][j]

    if j > 0:
        nl = array[i][j - 1]

    if j < array.shape[1] - 1:
        nr = array[i][j + 1]

    neighbors = [z for z in [nu, nd, nl, nr] if z is not None]

    return not any(array[i][j] >= q for q in neighbors)


if __name__ == "__main__":
    height_map = read_input("day9_input.txt")

    array = np.array([list(map(int, list(i))) for i in height_map])
    risk_levels = []
    all_basins = []

    for i, x in enumerate(array):
        for j, y in enumerate(x):
            is_low_point = check_neighbors(i, j, array)
            if is_low_point:
                risk_levels.append(1 + y)
                all_basins.append(Basin(i, j))
                # print("debug")

    print(f"RISK SUM: {sum(risk_levels)}")

    for basin in all_basins:
        basin.do_all_the_expanding()

    all_basin_sizes = [len(basin.points) for basin in all_basins]
    all_basin_sizes.sort()

    top_3 = all_basin_sizes[-3:]

    product = np.prod(top_3)

    print(f"product: {product}")
