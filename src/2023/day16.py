from utils import pull_input_directly
import numpy as np
from joblib import Parallel, delayed
from tqdm import tqdm

def light_step(cur_space, beam):
    up = (-1, 0, "u")
    down = (1, 0, "d")
    left = (0, -1, "l")
    right = (0, 1, "r")
    action, split = {
        "|": {
            "l": (up, down),    # with split
            "r": (up, down),    # with split
            "u": (up, None),
            "d": (down, None)
        },
        "-": {
            "l": (left, None),
            "r": (right, None),
            "u": (right, left),     # with split
            "d": (right, left)      # with split
        },
        "/": {
            "l": (down, None),
            "r": (up, None),
            "u": (right, None),
            "d": (left, None)
        },
        "\\": {
            "l": (up, None),
            "r": (down, None),
            "u": (left, None),
            "d": (right, None)
        },
        ".": {
            "l": (left, None),
            "r": (right, None),
            "u": (up, None),
            "d": (down, None)
        },
    }[cur_space][beam[2]]

    return *action, split

def do_the_thing(beams):
    energized = np.zeros(shape=cave.shape, dtype=bool)
    total_energize = [0, 1]
    while len(set(total_energize)) != 1:
        newbeams = []
        for beam in beams:
            x, y, direction = beam
            energized[x, y] = True
            dx, dy, newdir, newbeam = light_step(cur_space=cave[x, y], beam=beam)
            beam[0] += dx
            beam[1] += dy
            beam[2] = newdir
            if newbeam:
                nx, ny, ndir = newbeam
                newbeams.append([nx + x, ny + y, ndir])

        beams += newbeams

        # remove dead beams
        beams = [
            b for b in beams
            if b[0] in range(cave.shape[0])
               and b[1] in range(cave.shape[1])
        ]

        if len(total_energize) < 50:
            total_energize.append(np.sum(energized))
        else:
            total_energize = total_energize[-49:] + [np.sum(energized)]

    return total_energize[-1]

if __name__ == "__main__":
    cave = np.array([[*x] for x in pull_input_directly(2023, 16, mode="sample")])

    # p1 = do_the_thing([[0, 0, "r"]])
    #
    # print(f"PART 1: {p1}")

    max_x = cave.shape[0] - 1
    max_y = cave.shape[1] - 1
    starting_beams = (
            [[[x, 0, "r"]] for x in range(max_x+1)]
            + [[[x, max_y, "l"]] for x in range(max_x+1)]
            + [[[0, y, "d"]]for y in range(max_y+1)]
            + [[[max_x, y, "u"]] for y in range(max_y+1)]
    )
    # res = Parallel(n_jobs=-1)(delayed(do_the_thing)(x) for x in tqdm(starting_beams))
    res = []
    for s in tqdm(starting_beams):
        res.append(do_the_thing(s))

    print(max(res))




