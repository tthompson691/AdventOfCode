from utils.utils import read_input
import numpy as np

if __name__ == "__main__":
    moves = read_input("day9tstinp.txt")

    grid = np.zeros([15, 15], dtype=np.int8)

    headx = heady = 7
    tailx = taily = 7

    grid[headx, heady] = 2

    for i, move in enumerate(moves):
        grid[headx, heady] = 0
        prev_dir = moves[i-1].split(" ")[0] if i > 0 else None
        direction = move.split(" ")[0]
        steps = int(move.split(" ")[1])

        change_dir = (prev_dir != direction) or (prev_dir is not None)
        skip = 1 if change_dir else 0

        if direction == "L":
            heady -= steps
            grid[headx, heady] = 2
            grid[headx, (taily - steps - skip + 1):taily] = 1
        elif direction == "R":
            pass
        elif direction == "U":
            pass
        elif direction == "D":
            headx += steps
            grid[headx, heady] = 2
            taily = heady if change_dir else taily
            grid[(tailx + skip):headx-1, taily] = 1
            # grid[]


        move

