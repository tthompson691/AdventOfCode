import re

from utils.utils import read_input


def read_instruction_set(statement):
    instructions = re.findall(r"mul\(\d+,\d+\)", statement)
    total = 0
    for instruction in instructions:
        digits = re.findall(r"\d+", instruction)
        total += int(digits[0]) * int(digits[1])

    return total


inp = "".join(read_input(2024, 3, source="real"))

print(f"PART 1: {read_instruction_set(inp)}")

conditionals = inp.split("do()")
culled_conditionals = [c.split("don't()")[0] for c in conditionals]

print(f"PART 2: {sum([read_instruction_set(cc) for cc in culled_conditionals])}")
