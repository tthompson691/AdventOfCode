from utils.utils import read_input


def check_repeats(val, part):
    if len(val) == 1:
        return 0

    range_start = {1: len(val) // 2, 2: 1}[part]
    for stepsize in range(range_start, (len(val) // 2) + 1):
        splits = [val[a : a + stepsize] for a in range(0, len(val), stepsize)]
        if len(set(splits)) == 1:
            return int(val)

    return 0


def day2(input_data, part):
    id_ranges = [
        range(int(x.split("-")[0]), int(x.split("-")[1]) + 1) for x in input_data.split(",")
    ]
    res = sum([check_repeats(str(y), part) for x in id_ranges for y in x])

    print(f"Part {part}: {res}")


if __name__ == "__main__":
    input_data = read_input(2025, 2, source="real")[0]
    for part in (1, 2):
        day2(input_data, part)
