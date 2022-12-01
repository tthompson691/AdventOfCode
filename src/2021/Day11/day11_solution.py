from utils import read_input
import numpy as np


def receive_energy(octos: np.array):
    octos = (octos + 1) % 10
    new_flashers = {
        (i, j) for i, x in enumerate(octos) for j, y in enumerate(x) if y == 0
    }
    while len(new_flashers) != 0:
        flashers = {
            (i, j) for i, x in enumerate(octos) for j, y in enumerate(x) if y == 0
        }
        for i, x in enumerate(octos):
            for j, y in enumerate(octos):
                if octos[i, j] != 0:
                    # up left
                    if (
                        i > 0
                        and j > 0
                        and octos[i - 1, j - 1] == 0
                        and octos[i, j] != 0
                        and (i - 1, j - 1) in new_flashers
                    ):
                        octos[i, j] = (octos[i, j] + 1) % 10

                    # up
                    if (
                        i > 0
                        and octos[i - 1, j] == 0
                        and octos[i, j] != 0
                        and (i - 1, j) in new_flashers
                    ):
                        octos[i, j] = (octos[i, j] + 1) % 10

                    # up right
                    if (
                        i > 0
                        and j < octos.shape[1] - 1
                        and octos[i - 1, j + 1] == 0
                        and octos[i, j] != 0
                        and (i - 1, j + 1) in new_flashers
                    ):
                        octos[i, j] = (octos[i, j] + 1) % 10

                    # left
                    if (
                        j > 0
                        and octos[i, j - 1] == 0
                        and octos[i, j] != 0
                        and (i, j - 1) in new_flashers
                    ):
                        octos[i, j] = (octos[i, j] + 1) % 10

                    # right
                    if (
                        j < octos.shape[1] - 1
                        and octos[i, j + 1] == 0
                        and octos[i, j] != 0
                        and (i, j + 1) in new_flashers
                    ):
                        octos[i, j] = (octos[i, j] + 1) % 10

                    # down left
                    if (
                        i < octos.shape[0] - 1
                        and j > 0
                        and octos[i + 1, j - 1] == 0
                        and octos[i, j] != 0
                        and (i + 1, j - 1) in new_flashers
                    ):
                        octos[i, j] = (octos[i, j] + 1) % 10

                    # down
                    if (
                        i < octos.shape[0] - 1
                        and octos[i + 1, j] == 0
                        and octos[i, j] != 0
                        and (i + 1, j) in new_flashers
                    ):
                        octos[i, j] = (octos[i, j] + 1) % 10

                    # down right
                    if (
                        i < octos.shape[0] - 1
                        and j < octos.shape[1] - 1
                        and octos[i + 1, j + 1] == 0
                        and octos[i, j] != 0
                        and (i + 1, j + 1) in new_flashers
                    ):
                        octos[i, j] = (octos[i, j] + 1) % 10

        new_flashers = {
            (i, j) for i, x in enumerate(octos) for j, y in enumerate(x) if y == 0
        } - flashers

    num_flashers = len(
        {(i, j) for i, x in enumerate(octos) for j, y in enumerate(x) if y == 0}
    )

    return octos, num_flashers


if __name__ == "__main__":
    octopi = np.array([list(map(int, i)) for i in read_input("day11_input.txt")])
    total_flashes = 0
    for i in range(0, 100):
        octopi, num_flashes = receive_energy(octopi)
        total_flashes += num_flashes

    print(f"TOTAL FLASHES: {total_flashes}")

    octopi = np.array([list(map(int, i)) for i in read_input("day11_input.txt")])

    counter = 0
    while not all([x for y in octopi == 0 for x in y]):
        octopi, num_flashes = receive_energy(octopi)
        counter += 1

    print(f"STEP: {counter}")
