from utils.utils import pull_input_directly, read_input
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import copy

def show_cave_plot(cave):
    global cmap, norm, ax
    cmap = colors.ListedColormap(['white', 'orange', 'blue'])
    bounds = [0, 3, 7, 9]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    fig, ax = plt.subplots()
    ax.imshow(cave, cmap=cmap, norm=norm)
    plt.show()
    plt.close()


def fill_cave(cave):
    sand = 0
    while True:
        sand_r = 0
        sand_c = 500
        try:
            while True:
                # try vertical drop
                if cave[sand_r + 1, sand_c] == 0:
                    sand_r += 1
                # try left drop
                elif cave[sand_r + 1, sand_c - 1] == 0:
                    sand_r += 1
                    sand_c -= 1
                # try right drop
                elif cave[sand_r + 1, sand_c + 1] == 0:
                    sand_r += 1
                    sand_c += 1
                else:
                    # sand rests
                    cave[sand_r, sand_c] = 5
                    sand += 1
                    break

        except IndexError:
            # part 1 condition - we have reached the void
            show_cave_plot(cave)
            print(sand)
            break

        if sand_r == 0 and sand_c == 500:
            # part 2 condition
            show_cave_plot(cave)
            print(sand)
            break


if __name__ == "__main__":
    inp = pull_input_directly(2022, 14)[:-1]
    all_wallnodes = [[tuple(map(int, j.split(","))) for j in i.split(" -> ")] for i in inp]

    max_r = max(max(i[1] for i in j) for j in all_wallnodes)

    p1_cave = np.zeros([max_r + 1, 1000], dtype=np.int8)

    for wallnodes in all_wallnodes:
        for i in range(1, len(wallnodes)):
            c1, r1 = wallnodes[i - 1]
            c2, r2 = wallnodes[i]

            if c1 != c2:
                c1, c2 = sorted([c1, c2])
                p1_cave[r1, c1:c2+1] = 9
            elif r1 != r2:
                r1, r2 = sorted([r1, r2])
                p1_cave[r1:r2+1, c1] = 9

    p2_cave = copy.deepcopy(p1_cave)
    floor = np.zeros([2, p2_cave.shape[1]])
    floor[1, :] = 9
    p2_cave = np.vstack([p2_cave, floor])

    fill_cave(p1_cave)
    fill_cave(p2_cave)





