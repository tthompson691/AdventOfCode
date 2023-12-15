import numpy as np
import pandas as pd

from utils import pull_input_directly

if __name__ == "__main__":
    moves = pull_input_directly(2022, 9)[:-1]

    grid = np.zeros([500, 500], dtype=np.int8)
    dfgrid = pd.DataFrame({i: [None] * 500 for i in range(500)})
    headx = heady = 250
    tailx = taily = 250

    grid[headx, heady] = 2

    ### PART 1 ###
    for i, move in enumerate(moves):
        dfgrid.iloc[headx, heady] = "H"
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

            grid[tailx, taily] = 1
            dfgrid.iloc[tailx, taily] = "T"
            dfgrid.iloc[headx, heady] = "H"

    print(np.sum(grid))

    ### PART 2 ###
    grid = np.zeros([500, 500], dtype=np.int8)
    dfgrid = pd.DataFrame({i: [None] * 500 for i in range(500)})
    knots = [[250, 250] for _ in range(10)]

    for i, move in enumerate(moves):
        direction = move.split(" ")[0]
        steps = int(move.split(" ")[1])

        for step in range(steps):
            for k in knots:
                dfgrid.iloc[k[0], k[1]] = None

            # move head
            if direction == "L":
                knots[0][1] -= 1
            elif direction == "R":
                knots[0][1] += 1
            elif direction == "U":
                knots[0][0] -= 1
            elif direction == "D":
                knots[0][0] += 1

            # does tail need to move?
            for j in range(1, 10):
                if abs(knots[j - 1][0] - knots[j][0]) > 1 or abs(knots[j - 1][1] - knots[j][1]) > 1:
                    diffx = knots[j - 1][1] - knots[j][1]
                    diffy = knots[j - 1][0] - knots[j][0]

                    if diffx < 0:
                        knots[j][1] -= 1
                    elif diffx > 0:
                        knots[j][1] += 1

                    if diffy < 0:
                        knots[j][0] -= 1
                    elif diffy > 0:
                        knots[j][0] += 1

            for z, k in enumerate(knots):
                dfgrid.iloc[k[0], k[1]] = z

            grid[knots[-1][0], knots[-1][1]] = 1

    print(np.sum(grid))
