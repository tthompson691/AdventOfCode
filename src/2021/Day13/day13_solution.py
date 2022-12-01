from utils import read_input
import numpy as np


def fold(paper, axis, val):
    if axis == "x":
        dots = [(dot[0], dot[1]) for dot in np.argwhere(paper) if dot[1] > val]
        for dot in dots:
            diff = abs(val - dot[1])
            paper[dot[0], (dot[1] - diff * 2)] = 1
        del_range = list(range(val, paper.shape[1]))
        paper = np.delete(paper, del_range, 1)
    elif axis == "y":
        dots = [(dot[0], dot[1]) for dot in np.argwhere(paper) if dot[0] > val]
        for dot in dots:
            diff = abs(val - dot[0])
            paper[(dot[0] - diff * 2), dot[1]] = 1
        del_range = list(range(val, paper.shape[0]))
        paper = np.delete(paper, del_range, 0)

    return paper


if __name__ == "__main__":
    inp = read_input("day13_input.txt")
    coords = [
        (int(i.split(",")[1]), int(i.split(",")[0]))
        for i in inp
        if "fold" not in i and i != ""
    ]
    instructions = [
        (
            i.split("fold along ")[1].split("=")[0],
            int(i.split("fold along ")[1].split("=")[1]),
        )
        for i in inp
        if "fold" in i
    ]

    max_x = max(i[0] for i in coords)
    max_y = max(i[1] for i in coords)

    paper = np.zeros([max_x + 1, max_y + 1], dtype=int)

    for coord in coords:
        paper[coord[0], coord[1]] = 1

    # part 1
    paper = fold(paper, instructions[0][0], instructions[0][1])
    print(f"part 1: {np.count_nonzero(paper)}")
    # part 2
    paper2 = np.zeros([max_x + 1, max_y + 1], dtype=int)

    for coord in coords:
        paper2[coord[0], coord[1]] = 1
    for instruction in instructions:
        paper2 = fold(paper2, instruction[0], instruction[1])
