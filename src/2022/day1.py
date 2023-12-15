from more_itertools import locate

from utils import pull_input_directly

if __name__ == "__main__":
    inp = [""] + pull_input_directly(2022, 1)
    elves = []
    blank_idxs = list(locate(inp, lambda x: x == ""))

    for i, blank_i in enumerate(blank_idxs):
        if i == len(blank_idxs) - 1:
            break

        elves.append(sum(int(j) for j in inp[blank_i + 1 : blank_idxs[i + 1]]))

    elves.sort(reverse=True)
    print(sum(elves[:3]))
