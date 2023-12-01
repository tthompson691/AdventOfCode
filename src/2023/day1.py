from utils.utils import pull_input_directly
import re

if __name__ == "__main__":
    calibration = pull_input_directly(2023, 1)[:-1]
    total_sum = 0
    for line in calibration:
        digits = re.findall("[0-9]", line)
        total_sum += int("".join([digits[0], digits[-1]]))

    print(f"PART 1: {total_sum}")

    ## PART 2 ##
    total_sum = 0
    wordnums = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    re_pattern = "|".join(wordnums) + "|[0-9]"

    for line in calibration:
        digits = [wordnums.get(x) or x for x in re.findall(re_pattern, line)]
        total_sum += int("".join([digits[0], digits[-1]]))

    print(f"PART 2: {total_sum}")