from utils.utils import read_input
import numpy as np

def multiply(operands):
    result = 1
    for op in operands:
        result *= op
    return result

def part1(data):
    data = [[x for x in line.split(" ") if x != ""] for line in data]
    numbers = [[int(x) for x in line] for line in data[:-1]]
    operators = data[-1]
    total = 0
    for i in range(len(numbers[0])):
        operands = [numbers[j][i] for j in range(len(numbers))]
        operator = operators[i]
        total += {
            "*": multiply,
            "+": sum,
        }[operator](operands)
    
    print(f"Part 1: {total}")

def part2(data):
    numbers = np.array([[x for x in line] for line in data])
    operands = []
    total = 0
    for c in range(numbers.shape[1]-1, -1, -1):
        if all(numbers[:-1, c] == " "):
            continue
        operands.append(int("".join(numbers[:-1, c]).strip()))
        if numbers[-1, c] == "*":
            total += multiply(operands)
            operands = []
        elif numbers[-1, c] == "+":
            total += sum(operands)
            operands = []

        
    print(f"Part 2: {total}")

if __name__ == "__main__":
    data = read_input(2025, 6, source="real")
    # part1(data)
    part2(data)