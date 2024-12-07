from utils.utils import read_input
from itertools import product, pairwise


def reverse_engineer(answer, operands, res=0):
    running_total = answer
    if len(operands) == 0:
        if running_total == 0:
            return res + 1
        else:
            return res

    if running_total % operands[-1] == 0:
        res = reverse_engineer(running_total / operands[-1], operands[:-1], res=res)

    if running_total - operands[-1] >= 0:
        res = reverse_engineer(running_total - operands[-1], operands[:-1], res=res)

    if len(operands) >= 2:
        new_operand = int(str(operands[-2]) + str(operands[-1]))
        new_operands = operands[:-2] + [new_operand]
        res = reverse_engineer(running_total, new_operands, res=res)


    return res



equations = read_input(2024, 7, source="sample")

p1_ans = 0
for equation in equations:
    answer, operands = equation.split(": ")
    operands = list(map(int, operands.split(" ")))
    answer = int(answer)
    res = reverse_engineer(answer, operands)

    if res > 0:
        print(equation)
        p1_ans += answer


print(f"PART 1: {p1_ans}")


