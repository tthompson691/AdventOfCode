from utils import read_input
from numpy import median


def calculate_autocomplete_score(chars):
    auto_score_dict = {")": 1, "]": 2, "}": 3, ">": 4}
    final_score = 0

    for _char in chars:
        final_score = final_score * 5 + auto_score_dict[_char]

    return final_score


if __name__ == "__main__":
    subsystem = [list(i) for i in read_input("day10_input.txt")]
    pairs_dict = {"{": "}", "[": "]", "<": ">", "(": ")"}
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    line_scores = 0
    all_auto_scores = []
    for line in subsystem:
        stack = []
        line_corrupted = False
        for char in line:
            if char in pairs_dict.keys():
                stack.append(char)
            elif char in pairs_dict.values():
                if char != pairs_dict[stack[-1]]:
                    line_scores += scores[char]
                    line_corrupted = True
                    break
                else:
                    del stack[-1]

        if not line_corrupted:
            completion_chars = [pairs_dict[i] for i in reversed(stack)]
            all_auto_scores.append(calculate_autocomplete_score(completion_chars))

    print(f"total corrupted: {line_scores}")
    print(f"part 2: {median(all_auto_scores)}")
