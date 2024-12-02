from collections import Counter

from utils.utils import read_input

if __name__ == "__main__":
    inp = read_input(2024, 1, source="real")

    inp = [tuple(map(int, x.split("   "))) for x in inp]
    l_list = [x[0] for x in inp]
    r_list = [x[1] for x in inp]
    pairs = zip(sorted(l_list), sorted(r_list))
    p1 = sum([abs(x[1] - x[0]) for x in pairs])
    print(f"PART 1: {p1}")

    r_list_counts = Counter(r_list)
    p2 = sum([v * r_list_counts[v] for v in l_list])
    print(f"PART 2: {p2}")
