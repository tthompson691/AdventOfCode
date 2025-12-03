from utils.utils import read_input


def calc_one_row(row, num_batteries):
    batteries = []
    for i in range(num_batteries, 0, -1):
        split_index = -i + 1
        if split_index != 0:
            max_battery = max(row[:split_index])
            batteries.append(max_battery)
        else:
            max_battery = max(row)
            batteries.append(max_battery)
            break
        row = row[row.index(max_battery) + 1 :]

    return int("".join([str(b) for b in batteries]))


def day3(input_data, part):
    res = 0
    num_batteries = {1: 2, 2: 12}[part]
    for row in input_data:
        res += calc_one_row(row, num_batteries)

    print(f"Part {part}: {res}")


if __name__ == "__main__":
    input_data = read_input(2025, 3, source="real")
    for part in (1, 2):
        day3(input_data, part=part)
