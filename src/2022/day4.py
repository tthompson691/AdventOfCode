import re

from utils.utils import pull_input_directly

if __name__ == "__main__":
    inp = pull_input_directly(2022, 4)[:-1]

    nums = [list(map(int, re.split(",|-", i))) for i in inp]

    # Part 1
    print(
        sum(
            (
                len(set(range(num[0], num[1] + 1)).union(set(range(num[2], num[3] + 1))))
                == num[1] + 1 - num[0]
            )
            or (
                len(set(range(num[0], num[1] + 1)).union(set(range(num[2], num[3] + 1))))
                == num[3] + 1 - num[2]
            )
            for num in nums
        )
    )

    # Part 2
    print(
        sum(
            set(range(num[0], num[1] + 1)).intersection(set(range(num[2], num[3] + 1))) != set()
            for num in nums
        )
    )
