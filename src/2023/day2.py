from utils import pull_input_directly

if __name__ == "__main__":
    bag = pull_input_directly(2023, 2)[:-1]
    colors = ["red", "green", "blue"]
    limits = {"red": 12, "green": 13, "blue": 14}
    total_sum_p1 = 0
    total_sum_p2 = 0
    for game in bag:
        maxes = {}
        game = game.replace(",", ";")
        game_no, cubes = game.split(": ")
        game_no = int(game_no.split(" ")[-1])
        cubes = [(int(x.split(" ")[0]), x.split(" ")[1]) for x in cubes.split("; ")]
        for color in colors:
            maxes[color] = max([x[0] for x in cubes if x[1] == color])

        if all([maxes[c] <= limits[c] for c in colors]):
            total_sum_p1 += game_no

        total_sum_p2 += maxes["red"] * maxes["green"] * maxes["blue"]

    print(f"PART 1: {total_sum_p1}")
    print(f"PART 2: {total_sum_p2}")
