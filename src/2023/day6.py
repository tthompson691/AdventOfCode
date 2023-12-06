import numpy as np
import pandas as pd


def calc_distances_traveled(max_time, record_distance):
    return sum(
        [
            button_time * (max_time - button_time) > record_distance
            for button_time in range(max_time + 1)
        ]
    )


if __name__ == "__main__":
    races = pd.DataFrame({"time": [49, 87, 78, 95], "distance": [356, 1378, 1502, 1882]})

    races["wins"] = races.apply(lambda x: calc_distances_traveled(x["time"], x["distance"]), axis=1)
    print(f"PART 1: {np.prod(races['wins'])}")

    max_time = 49877895
    record_distance = 356137815021882

    crossover_found = False
    button_hold_time = 0
    while not crossover_found:
        distance = button_hold_time * (max_time - button_hold_time)
        if distance > record_distance:
            crossover_found = True
        else:
            button_hold_time += 1

    configs = max_time - (2 * button_hold_time) + 1

    print(f"PART 2: {configs}")
