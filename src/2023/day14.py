import numpy as np

if __name__ == "__main__":
    with open(r"C:\Users\tthompson2\Documents\REPOS\AdventOfCode\src\2023\day14samp.txt") as f:
        rocks = np.array([[*x] for x in f.read().splitlines()])

    for i, x in enumerate(rocks):
        for j, y in enumerate(x):
            if y == "O":
                empty_space = 0
                z = i - 1
                while rocks[z, j] == "." and z >= 0:
                    empty_space += 1
                    z -= 1

                if empty_space != 0:
                    print("d")

    print("finished")
