from math import lcm

from utils.utils import pull_input_directly

if __name__ == "__main__":
    inp = pull_input_directly(2023, 8)[:-1]

    steps = inp[0]

    desert_map = {
        node.split(" = ")[0]: {"L": node.split(",")[0][-3:], "R": node.split(", ")[1][:-1]}
        for node in inp[2:]
    }

    curnode = "AAA"
    steps_taken = 0
    while curnode != "ZZZ":
        next_step = steps[steps_taken % len(steps)]
        curnode = desert_map[curnode][next_step]
        steps_taken += 1

    print(f"PART 1: {steps_taken}")

    nodes = [n for n in desert_map if n[-1] == "A"]
    all_steps = []
    for node in nodes:
        steps_taken = 0
        curnode = node
        while curnode[-1] != "Z":
            next_step = steps[steps_taken % len(steps)]
            curnode = desert_map[curnode][next_step]
            steps_taken += 1

        all_steps.append(steps_taken)
    print(f"PART 2: {lcm(*all_steps)}")
