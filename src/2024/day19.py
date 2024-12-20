from utils.utils import read_input


def check_valid_towel(towel, remaining_pattern):
    len_towel = len(towel)
    return remaining_pattern[:len_towel] == towel


inp = read_input(2024, 19, source="real")
all_towels = inp[0].split(", ")
patterns = inp[2:]


for part in 1, 2:
    viable_patterns = 0
    for pattern in patterns:
        is_viable = False
        viable_subpatterns = 0
        cache = {}
        histories = []
        visited = []
        towels = [(towel, len(towel)) for towel in all_towels if check_valid_towel(towel, pattern)]
        while towels:
            towel, pattern_index = towels.pop()
            if pattern_index == len(pattern):
                viable_subpatterns += 1
                is_viable = True
            for t in all_towels:
                if check_valid_towel(t, pattern[pattern_index:]):
                    if pattern_index + len(t) not in cache:
                        cache[pattern_index + len(t)] = 1
                        towels.append((t, pattern_index + len(t)))
                    else:
                        cache[pattern_index + len(t)] += 1
        viable_patterns += viable_subpatterns

    print(f"PART {part}: {viable_patterns}")


## I got part 1 by myself with the above solution
## Below solves both parts and looks essentially identical to MC's solution
## I definitely cheated off his code, then attempted to recreate it with my
## own take on it, and backed into the exact same solution. Just gotta give
## credit where credit is due.


def pattern_match(pattern, towels, cache={}):
    if pattern in cache:
        return cache[pattern]

    if not pattern:
        return 1

    cache[pattern] = sum(
        pattern_match(pattern[len(t) :], towels, cache) for t in towels if pattern.startswith(t)
    )

    return cache[pattern]


p1 = p2 = 0
for pattern in patterns:
    viable_patterns = 0
    res = pattern_match(pattern, all_towels)
    if res:
        p1 += 1
        p2 += res

print(f"PART 1: {p1}")
print(f"PART 2: {p2}")
