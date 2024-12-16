import re

import numpy as np

from utils.utils import read_input


def determine_quadrant(x, y):
    if x == mid_x or y == mid_y:
        return None
    elif x < mid_x and y < mid_y:
        return 1
    elif x > mid_x and y < mid_y:
        return 2
    elif x > mid_x and y > mid_y:
        return 3
    elif x < mid_x and y > mid_y:
        return 4


source = "real"
if source == "real":
    floor_size_x = 101
    floor_size_y = 103
elif source == "sample":
    floor_size_x = 11
    floor_size_y = 7

robots = [re.findall(r"\-*\d+", x) for x in read_input(2024, 14, source=source)]
robots = [list(map(int, x)) for x in robots]

mid_x = floor_size_x // 2
mid_y = floor_size_y // 2
quadrants = {1: 0, 2: 0, 3: 0, 4: 0}

# Okay I guess I'll make an array
robots = [{"pos": robot[:2], "vel": robot[2:]} for robot in robots]

for seconds_passed in range(8000):
    print(seconds_passed)
    floor = np.zeros((floor_size_y, floor_size_x))
    for i in range(len(robots)):
        robot = robots[i]
        pos_x, pos_y = robot["pos"]
        vel_x, vel_y = robot["vel"]
        pos_x = (pos_x + vel_x * seconds_passed) % floor_size_x
        pos_y = (pos_y + vel_y * seconds_passed) % floor_size_y
        floor[pos_y, pos_x] = 1

        if seconds_passed == 100:
            quadrant = determine_quadrant(pos_x, pos_y)
            if quadrant:
                quadrants[quadrant] += 1

    if seconds_passed == 100:
        print(f"PART 1: {quadrants[1] * quadrants[2] * quadrants[3] * quadrants[4]}")

    for row in floor:
        print("".join(["#" if x == 1 else " " for x in row]))


print("PART 2: Scroll until we see it")
