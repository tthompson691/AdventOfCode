from utils.utils import read_input
import numpy as np
import pandas as pd



if __name__ == "__main__":
    moves = read_input("day9inp.txt")

    grid = np.zeros([500, 500], dtype=np.int8)
    dfgrid = pd.DataFrame(
        {
            i: [None] * 500
            for i in range(500)
        }
    )
    headx = heady = 250
    tailx = taily = 250

    grid[headx, heady] = 2

    for i, move in enumerate(moves):
        grid[headx, heady] = 0 if grid[headx, heady] != 1 else 1
        dfgrid.iloc[headx, heady]
        dfgrid.iloc[headx, heady] = "H"

        prev_dir = moves[i-1].split(" ")[0] if i > 0 else None
        direction = move.split(" ")[0]
        steps = int(move.split(" ")[1])

        for step in range(steps):
            dfgrid.iloc[headx, heady] = None
            dfgrid.iloc[tailx, taily] = None
            # move head
            if direction == "L":
                heady -= 1
            elif direction == "R":
                heady += 1
            elif direction == "U":
                headx -= 1
            elif direction == "D":
                headx += 1

            # does tail need to move?
            if abs(headx - tailx) > 1 or abs(heady - taily) > 1:
                if direction == "L":
                    tailx = headx
                    taily = heady + 1
                elif direction == "R":
                    tailx = headx
                    taily = heady - 1
                elif direction == "U":
                    tailx = headx + 1
                    taily = heady
                elif direction == "D":
                    tailx = headx - 1
                    taily = heady


            grid[headx, heady] = 0

            grid[tailx, taily] = 1
            dfgrid.iloc[tailx, taily] = "T"
            dfgrid.iloc[headx, heady] = "H"


    print(np.where(grid==1))


