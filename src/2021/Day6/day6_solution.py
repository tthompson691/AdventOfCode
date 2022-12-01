from utils import read_input


def age_and_spawn_the_fish(fishes):
    baby_age = 8

    spawns = determine_num_spawns(fishes)

    for i, fish in enumerate(fishes):
        fishes[i] = calc_next_age(fish)

    for i in range(0, spawns):
        fishes.append(baby_age)

    return fishes


def calc_next_age(fish):
    spawn_time = 6
    if fish > 0:
        return fish - 1
    else:
        return spawn_time


def determine_num_spawns(fishes):
    return len([i for i in fishes if i == 0])


def p2_spawn_and_age_the_fish(fishes_dict):
    new_counts = {}
    new_counts[0] = fishes_dict[1]
    new_counts[1] = fishes_dict[2]
    new_counts[2] = fishes_dict[3]
    new_counts[3] = fishes_dict[4]
    new_counts[4] = fishes_dict[5]
    new_counts[5] = fishes_dict[6]
    new_counts[6] = fishes_dict[7] + fishes_dict[0]
    new_counts[7] = fishes_dict[8]
    new_counts[8] = fishes_dict[0]

    return new_counts


if __name__ == "__main__":
    fishes = [int(i) for i in read_input("day6_input.txt")[0].split(",")]

    days = 256
    # PART 1
    # for i in range(0, days):
    #     print(f"DAY {i}")
    #     fishes = age_and_spawn_the_fish(fishes)
    #
    # print(f"FINAL: {len(fishes)}")

    # PART 2
    fishes_dict = {}
    for i in range(0, 9):
        fishes_dict[i] = len([f for f in fishes if f == i])

    for i in range(0, days):
        fishes_dict = p2_spawn_and_age_the_fish(fishes_dict)

    print(f"PART 2: {sum([fishes_dict[i] for i in fishes_dict])}")
