import re

from utils.utils import read_input


def get_combo_operand(x):
    return {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: registers["A"],
        5: registers["B"],
        6: registers["C"],
    }[x]


def adv(x):
    global registers
    registers["A"] = int(registers["A"] / (2 ** get_combo_operand(x)))


def bxl(x):
    global registers
    registers["B"] = registers["B"] ^ x


def bst(x):
    global registers
    registers["B"] = get_combo_operand(x) % 8


def jnz(x):
    global instruction_pointer
    if registers["A"] != 0:
        instruction_pointer = x
    else:
        instruction_pointer += 2


def bxc(x):
    global registers
    registers["B"] = registers["B"] ^ registers["C"]


def out(x):
    return get_combo_operand(x) % 8


def bdv(x):
    global registers
    registers["B"] = int(registers["A"] / (2 ** get_combo_operand(x)))


def cdv(x):
    global registers
    registers["C"] = int(registers["A"] / (2 ** get_combo_operand(x)))


inp = read_input(2024, 17, source="real")

registers = {
    re.findall(r"Register ([ABC])\:", x)[0]: int(re.findall(r": (\d+)", x)[0]) for x in inp[:3]
}
commands = list(map(int, inp[4].strip("Program: ").split(",")))
instruction_pointer = 0

func_factory = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

p1 = ""
while instruction_pointer < len(commands):
    opcode, operand = commands[instruction_pointer], commands[instruction_pointer + 1]

    res = func_factory[opcode](operand)
    if res is not None:
        p1 += str(res) + ","

    if opcode != 3:
        instruction_pointer += 2

print(f"PART 1: {p1[:-1]}")
