from collections import deque

from utils.utils import read_input


def p1_press_one_button(button_pressed, current_state=None, num_presses=0):
    flipper_dict = {".": "#", "#": "."}

    for i in button_pressed:
        current_state[i] = flipper_dict[current_state[i]]

    return current_state, num_presses + 1


def part1(machines):
    res = 0
    for machine in machines:
        queue = deque([(["."] * len(machine["lights"]), 0)])  # (current_state, num_presses)
        state_achieved = False
        achieved_states = []

        while not state_achieved:
            state, past_presses = queue.popleft()
            for button in machine["buttons"]:
                new_state, num_presses = p1_press_one_button(
                    button_pressed=button, current_state=state.copy(), num_presses=past_presses
                )

                if new_state in achieved_states:
                    continue

                achieved_states.append(new_state)
                if new_state == machine["lights"]:
                    res += num_presses
                    state_achieved = True
                    break
                queue.extend([(new_state.copy(), num_presses)])

    print(f"Part 1: {res}")


def p2_press_one_button(button_pressed, current_state=None, num_presses=0):
    for i in button_pressed:
        current_state[i] += 1

    return current_state, num_presses + 1


def part2(machines):
    # regular BFS doesn't scale :(
    return


if __name__ == "__main__":
    data = read_input(2025, 10, source="real")
    machines = []
    for row in data:
        stuff = row.split()
        machines.append(
            {
                "lights": [x for x in stuff[0][1:-1]],
                "buttons": [
                    (x,) if not isinstance(x, tuple) else x
                    for x in [eval(button) for button in stuff[1:-1]]
                ],
                "joltage": eval(stuff[-1].replace("{", "[").replace("}", "]")),
            }
        )

    part1(machines)
    part2(machines)
