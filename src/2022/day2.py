from utils import pull_input_directly


def part_1(rounds):
    newkeys = {
        "A": {"X": 4, "Y": 8, "Z": 3},
        "B": {"X": 1, "Y": 5, "Z": 9},
        "C": {"X": 7, "Y": 2, "Z": 6},
    }

    return sum(newkeys[r[0]][r[-1]] for r in rounds)


def part_2(rounds):
    rps_scores = {"X": 1, "Y": 2, "Z": 3}
    all_outcomes = {
        "X": {"A": "Z", "B": "X", "C": "Y", "val": 0},
        "Y": {"A": "X", "B": "Y", "C": "Z", "val": 3},
        "Z": {"A": "Y", "B": "Z", "C": "X", "val": 6},
    }

    return sum(rps_scores[all_outcomes[r[-1]][r[0]]] + all_outcomes[r[-1]]["val"] for r in rounds)


if __name__ == "__main__":
    rounds = pull_input_directly(2022, 2)[:-1]

    part1_score = part_1(rounds)

    part2_score = part_2(rounds)

    print(f"Part 1: {part1_score}")
    print(f"Part 2: {part2_score}")
