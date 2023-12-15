from utils import pull_input_directly
import numpy as np

def next_step(val, dir):
    northturn = (-1, 0, "n")
    southturn = (1, 0, "s")
    eastturn = (0, 1, "e")
    westturn = (0, -1, "w")
    return {
        "|": {"s": southturn, "n": northturn},
        "-": {"e": eastturn, "w": westturn},
        "L": {"s": eastturn, "w": northturn},
        "F": {"n": eastturn, "w": southturn},
        "J": {"s": westturn, "e": northturn},
        "7": {"n": westturn, "e": southturn}
    }[val][dir]

if __name__ == "__main__":
    # with open("/Users/travisthompson/REPOS/AdventOfCode/src/2023/day10samp.txt", "r") as f:
    #     inp = np.array([[*x] for x in f.read().splitlines()])
    inp = np.array([[*x] for x in pull_input_directly(2023, 10)[:-1]])

    x, y = [i[0] for i in np.where(inp == "S")]

    dir = "s"
    steps_taken = 1
    x += 1
    while inp[x][y] != "S":
        dx, dy, dir = next_step(inp[x][y], dir)
        steps_taken += 1
        x += dx
        y += dy

    print(f"PART 1: {int(steps_taken / 2)}")


