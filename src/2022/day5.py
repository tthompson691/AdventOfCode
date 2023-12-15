import re

from utils import pull_input_directly


def generate_top_crate_string(stacks):
    return "".join(stacks[i][-1] for i in stacks)


def part1(stacks, moves):
    for move in moves:
        for _ in range(move[0]):
            stacks[move[2]].append(stacks[move[1]].pop())

    return generate_top_crate_string(stacks)


def part2(stacks, moves):
    for move in moves:
        stacks[move[2]] += stacks[move[1]][-move[0] :]
        stacks[move[1]] = stacks[move[1]][: -move[0]]

    return generate_top_crate_string(stacks)


if __name__ == "__main__":
    inp = pull_input_directly(2022, 5, delimiter=None)

    moves = [
        list(map(int, [i for i in re.findall(r"\d+", j)]))
        for j in inp.split("\\n\\n")[1].split("\\n")
    ][:-1]

    # hard code the stacks like a real winner
    stacks = {
        1: ["C", "Z", "N", "B", "M", "W", "Q", "V"],
        2: ["H", "Z", "R", "W", "C", "B"],
        3: ["F", "Q", "R", "J"],
        4: ["Z", "S", "W", "H", "F", "N", "M", "T"],
        5: ["G", "F", "W", "L", "N", "Q", "P"],
        6: ["L", "P", "W"],
        7: ["V", "B", "D", "R", "G", "C", "Q", "J"],
        8: ["Z", "Q", "N", "B", "W"],
        9: ["H", "L", "F", "C", "G", "T", "J"],
    }

    part1_ans = part1(stacks, moves)

    part2_ans = part2(stacks, moves)

    print(part2_ans)
