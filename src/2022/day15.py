from re import findall

from utils.utils import pull_input_directly

if __name__ == "__main__":
    coords = [tuple(map(int, findall(r"-*\d+", i))) for i in pull_input_directly(2022, 15)[:-1]]

    rows = {}
    for c in coords:
        sx, sy, bx, by = c
        dx = abs(bx - sx)
        dy = abs(by - sy)
        manhattan = dx + dy
        counts_list = list(range(0, dy + 1)) + list(range(dy, -1, -1))
        for i, row in enumerate(range(sy - manhattan, sy + manhattan + 1)):
            try:
                rows[row].append(range(sx - i, sx + i + 1))
            except KeyError:
                rows[row] = [range(sx - i, sx + i + 1)]

    rows
