import re

if __name__ == "__main__":
    with open(
        "C:\\Users\\tthompson2\\Documents\\REPOS\\AdventOfCode\\src\\2023\\day12samp.txt"
    ) as f:
        spring_rows = f.read().splitlines()

    for row in spring_rows:
        bad_springs = re.findall(r"\?+|\#+", row)
        numbers = list(map(int, row.split(" ")[-1].split(",")))

        numbers
