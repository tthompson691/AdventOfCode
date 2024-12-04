import re

from utils.utils import read_input


def read_instruction_set(statement):
    return sum(
        [int(l_num) * int(r_num) for l_num, r_num in re.findall(r"mul\((\d+),(\d+)\)", statement)]
    )


inp = "".join(read_input(2024, 3, source="real"))

print(f"PART 1: {read_instruction_set(inp)}")

culled_conditionals = [c.split("don't()")[0] for c in inp.split("do()")]

print(f"PART 2: {sum([read_instruction_set(cc) for cc in culled_conditionals])}")
