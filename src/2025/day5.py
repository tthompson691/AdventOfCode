from utils.utils import read_input


def part1(fresh_ranges, ingredient_ids):
    res = sum(
        [
            any([ingredient_id in range(x, y + 1) for x, y in fresh_ranges])
            for ingredient_id in ingredient_ids
        ]
    )
    print(f"Part 1: {res}")


def part2(fresh_ranges):
    fresh_ranges = sorted(fresh_ranges, key=lambda x: (x[0], x[1]))
    consolidated_ranges = []
    for i, (lower, upper) in enumerate(fresh_ranges):
        if i == 0:
            consol_lower = lower
            consol_upper = upper
            continue
        if lower > consol_upper:
            consolidated_ranges.append((consol_lower, consol_upper))
            consol_lower = lower
            consol_upper = upper
        elif upper > consol_upper:
            consol_upper = upper

    consolidated_ranges.append((consol_lower, consol_upper))

    res = sum([y - x + 1 for x, y in consolidated_ranges])
    print(f"Part 2: {res}")


if __name__ == "__main__":
    data = read_input(2025, 5, source="real")

    fresh_ranges = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in data[0 : data.index("")]]
    ingredient_ids = [int(x) for x in data[data.index("") + 1 :]]
    part1(fresh_ranges, ingredient_ids)
    part2(fresh_ranges)
