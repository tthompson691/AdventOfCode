from utils.utils import pull_input_directly, read_input
from collections import Counter

if __name__ == "__main__":
    mode = "real"
    if mode == "sample":
        inp = read_input("/Users/travisthompson/REPOS/AdventOfCode/src/2024/day1samp.txt", delimiter="\n")
    else:
        inp = pull_input_directly(2024, 1)[:-1]

    inp = [tuple(map(int, x.split("   "))) for x in inp]
    l_list = [x[0] for x in inp]
    r_list = [x[1] for x in inp]
    pairs = zip(sorted(l_list), sorted(r_list))
    p1 = sum([abs(x[1] - x[0]) for x in pairs])
    print(f"PART 1: {p1}")

    r_list_counts = Counter(r_list)
    p2 = sum([v * r_list_counts[v] for v in l_list])
    print(f"PART 2: {p2}")

