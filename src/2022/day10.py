import numpy as np

from utils.utils import pull_input_directly

if __name__ == "__main__":
    inp = pull_input_directly(2022, 10)[:-1]
    cycles = 0
    x = 1
    total_sig_strength = 0
    screen = np.zeros([6, 40], dtype=np.int8)
    row = 0
    for i in inp:
        spritepos = [x - 1, x, x + 1]
        if "noop" in i:
            if cycles % 40 in spritepos:
                screen[row, cycles % 40] = 1

            cycles += 1
            row = cycles // 40
            if cycles in [20, 60, 100, 140, 180, 220]:
                total_sig_strength += x * cycles

        else:
            if cycles % 40 in spritepos:
                screen[row, cycles % 40] = 1

            cycles += 1
            row = cycles // 40
            if cycles in [20, 60, 100, 140, 180, 220]:
                total_sig_strength += x * cycles

            if cycles % 40 in spritepos:
                screen[row, cycles % 40] = 1

            cycles += 1
            row = cycles // 40
            if cycles in [20, 60, 100, 140, 180, 220]:
                total_sig_strength += x * cycles

            x += int(i.split(" ")[-1])

    print(total_sig_strength)
