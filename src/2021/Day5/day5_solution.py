import pandas as pd
from utils import read_input


def parse_cloud_string(cloud):
    points = cloud.split(" -> ")
    return (
        tuple([int(x) for x in points[0].split(",")]),
        tuple([int(x) for x in points[1].split(",")]),
    )


def determine_all_points(point1, point2):
    x1 = point1[0]
    x2 = point2[0]

    y1 = point1[1]
    y2 = point2[1]

    x_diff = x1 - x2
    y_diff = y1 - y2

    if x_diff != 0 and y_diff == 0:
        point_range = range(min(x1, x2), max(x1, x2) + 1)
        all_points = [(x, y1) for x in point_range]
    elif y_diff != 0 and x_diff == 0:
        point_range = range(min(y1, y2), max(y1, y2) + 1)
        all_points = [(x1, y) for y in point_range]
    else:
        if x1 > x2:
            x_point_range = range(x1, x2 - 1, -1)
        else:
            x_point_range = range(x1, x2 + 1)

        if y1 > y2:
            y_point_range = range(y1, y2 - 1, -1)
        else:
            y_point_range = range(y1, y2 + 1)

        x_and_y = list(zip(x_point_range, y_point_range))
        all_points = [(x, y) for x, y in x_and_y]

    return all_points


if __name__ == "__main__":
    clouds = read_input("day5_input.txt")
    points_dict = dict()
    for cloud in clouds:
        point1, point2 = parse_cloud_string(cloud)
        all_cloud_points = determine_all_points(point1, point2)
        for cloud_point in all_cloud_points:
            if cloud_point in points_dict:
                points_dict[cloud_point] += 1
            else:
                points_dict[cloud_point] = 1

    overlapped_points = 0
    for k in points_dict:
        if points_dict[k] > 1:
            overlapped_points += 1

    print(f"PART 1: {overlapped_points}")
