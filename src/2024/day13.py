import re

from numpy import linalg

from utils.utils import read_input

claw_machines = [
    list(map(int, re.findall(r"[\+\=](\d+)", x)))
    for x in read_input(2024, 13, source="real")
    if x != ""
]
claw_machines = [claw_machines[i : i + 3] for i in range(0, len(claw_machines), 3)]


tokens = 0
for a_button, b_button, prize_loc in claw_machines:
    this_machine_tokens = 0
    is_possible = True
    prize_x, prize_y = prize_loc
    a_dx, a_dy = a_button
    b_dx, b_dy = b_button
    dx_lcm = a_dx * b_dx
    dy_lcm = a_dy * b_dy
    claw_x, claw_y = [0, 0]
    a_presses = b_presses = 0
    num_stops = 0

    # first check if you can get there by just pressing b
    # this will never happen with my input

    # push a until b works

    while True:
        a_presses += 1
        claw_x += a_dx
        claw_y += a_dy
        if a_presses > 100 or claw_x > prize_x or claw_y > prize_y:
            is_possible = False
            break

        if (
            (prize_x - claw_x) % b_dx == 0
            and (prize_y - claw_y) % b_dy == 0
            and (prize_x - claw_x) / b_dx == (prize_y - claw_y) / b_dy
        ):
            if (prize_x - claw_x) // b_dx > 100:
                continue
            else:
                b_presses = (prize_x - claw_x) // b_dx
                break

    if is_possible:
        this_machine_tokens = 3 * a_presses + b_presses

    if (
        a_presses * a_dx + b_presses * b_dx != prize_x
        or a_presses * a_dy + b_presses * b_dy != prize_y
    ) and is_possible:
        print("whats up?")
        a_presses

    tokens += this_machine_tokens
print(f"PART 1: {tokens}")
## part 2 (I know this would also work for part 1 but I'm keeping it as is)
tokens = 0
for a_button, b_button, prize_loc in claw_machines:
    # print(f"Trying claw machine {prize_loc}")
    this_machine_tokens = 0
    is_possible = True
    prize_x, prize_y = prize_loc
    prize_x += 10000000000000
    prize_y += 10000000000000
    a_dx, a_dy = a_button
    b_dx, b_dy = b_button
    dx_lcm = a_dx * b_dx
    dy_lcm = a_dy * b_dy
    a, b = linalg.solve([[a_dx, b_dx], [a_dy, b_dy]], [prize_x, prize_y])
    a = int(round(a, 0))
    b = int(round(b, 0))

    if a * a_dx + b * b_dx == prize_x and a * a_dy + b * b_dy == prize_y:
        tokens += 3 * a + b


print(f"PART 2: {tokens}")
