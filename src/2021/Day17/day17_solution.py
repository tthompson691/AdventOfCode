from utils import read_input


def get_min_x(x=0):
    i = 0
    while x < x1:
        x += i
        i += 1

    return i - 1


def get_valid_x_vel(min_x):
    x_vel = min_x
    valid_x_vel = []
    start = 0
    while x_vel < x2:
        speeds = list(range(x_vel, -1, -1))
        x_pos = [0]
        for i, speed in enumerate(speeds):
            x_pos.append(x_pos[i] + speed)

        valid_x = [x for x in x_pos if x1 <= x <= x2]
        if len(valid_x) != 0:
            valid_x_vel.append(x_vel)

        x_vel += 1

    valid_x_vel.append(x_vel)

    return valid_x_vel


def step(_x_vel, _y_vel):
    _pos = [0, 0]
    _path = [(0, 0)]
    while _pos[1] >= y2:
        _pos[0] += _x_vel
        _pos[1] += _y_vel

        _path.append((_pos[0], _pos[1]))

        if _pos in target_area:
            return _path

        if _x_vel != 0:
            _x_vel -= 1

        _y_vel -= 1

    return "miss"


if __name__ == "__main__":
    inp = read_input("day17_input.txt")[0]

    x1 = int(inp.split(": ")[1].split(", ")[0].split("x=")[1].split("..")[0])
    x2 = int(inp.split(": ")[1].split(", ")[0].split("x=")[1].split("..")[1])
    y1 = int(inp.split(": ")[1].split(", ")[1].split("y=")[1].split("..")[1])
    y2 = int(inp.split(": ")[1].split(", ")[1].split("y=")[1].split("..")[0])

    target_area = [[x, y] for x in range(x1, x2 + 1) for y in range(y2, y1 + 1)]

    min_x_vel = get_min_x()
    valid_x_vels = get_valid_x_vel(min_x_vel)
    max_ys = []
    probe_pos = [0, 0]
    good_launches = []
    for x_vel in valid_x_vels:
        target_found = target_overshot = False
        y_vel = y2
        first_shot = True
        while y_vel < -y2:
            probe_pos = [0, 0]
            path = step(x_vel, y_vel)

            if path != "miss":
                target_found = True
                max_ys.append(max([pos[1] for pos in path]))
                good_launches.append((x_vel, y_vel))

            if (target_found or first_shot) and path == "miss":
                target_overshot = True

            first_shot = False
            y_vel += 1

    print(f"part 1: {max(max_ys)}")
    print(f"part 2: {len(good_launches)}")
