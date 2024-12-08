from utils.utils import read_input
from itertools import product


def reverse_engineer(answer, operands):
    if len(operands) == 0:
        if answer == 0:
            return True
        else:
            return False

    if answer % operands[-1] == 0:
        res = reverse_engineer(answer / operands[-1], operands[:-1])

    if answer - operands[-1] >= 0:
        res = reverse_engineer(answer - operands[-1], operands[:-1])

    return res

def part_2_forwards_engineer(answer, operands):
    operation_combos = product(["*", "+", "||"], repeat=len(operands) - 1)
    for op_combo in operation_combos:
        total = operands[0]
        for i, op in enumerate(op_combo):
            if op == "*":
                total *= operands[i+1]
            elif op == "+":
                total += operands[i+1]
            elif op == "||":
                total = int(str(total) + str(operands[i+1]))

        if total == answer:
            return True

    return False






equations = read_input(2024, 7, source="sample")

p1_ans = 0
p2_ans = 0
for equation in equations:
    answer, operands = equation.split(": ")
    operands = list(map(int, operands.split(" ")))
    answer = int(answer)
    if reverse_engineer(answer, operands):
        p1_ans += answer

    if part_2_forwards_engineer(answer, operands):
        p2_ans += answer


print(f"PART 1: {p1_ans}")
print(f"PART 2: {p2_ans}")


