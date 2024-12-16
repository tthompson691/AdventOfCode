import numpy as np

from utils.utils import read_input


def determine_num_rotations(start_dir, end_dir):
    directions = ["^", ">", "v", "<"]
    return (directions.index(end_dir) - directions.index(start_dir)) % 4


def get_wall_distance_from_robot(robot_col):
    if len(np.argwhere(robot_col == "#")) > 1:
        0
    return np.argwhere(robot_col == "#")[-1][0] - np.argwhere(robot_col == "@")[0][0]


inp = read_input(2024, 15, source="real")
warehouse = np.array([list(x) for x in inp[: inp.index("")]])
movements = "".join(inp[inp.index("") + 1 :])
previous_movement = "^"
for movement in movements:
    for _ in range(determine_num_rotations(previous_movement, movement)):
        warehouse = np.rot90(warehouse)

    previous_movement = movement
    robot_pos = np.argwhere(warehouse == "@")[0]
    distance_to_wall = get_wall_distance_from_robot(warehouse[: robot_pos[0] + 1, robot_pos[1]])
    robot_los = warehouse[robot_pos[0] + distance_to_wall : robot_pos[0], robot_pos[1]]
    if "." not in robot_los:
        # movement failed
        continue

    i = np.argwhere(robot_los == ".")[-1][0]

    if i == -1:
        new_los = np.concatenate((robot_los[:i], np.array(["@"])))
    else:
        new_los = np.concatenate((robot_los[:i], robot_los[i + 1 :], np.array(["@"])))
    warehouse[robot_pos[0] + distance_to_wall : robot_pos[0], robot_pos[1]] = new_los
    warehouse[*robot_pos] = "."

for _ in range(determine_num_rotations(previous_movement, "^")):
    warehouse = np.rot90(warehouse)

gps = sum([100 * x + y for x, y in np.argwhere(warehouse == "O")])
print(f"PART 1: {gps}")
