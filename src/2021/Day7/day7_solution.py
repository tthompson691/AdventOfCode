from utils import read_input


if __name__ == "__main__":
    positions = read_input("day7_input.txt")[0].split(",")
    positions = [int(i) for i in positions]

    min_pos = min(positions)
    max_pos = max(positions)
    all_options = []
    for pos in range(min_pos, max_pos + 1):
        fuel = sum(sum(range(1, abs(i - pos) + 1)) for i in positions)
        all_options.append(fuel)

    print(f"ANSWER: {min(all_options)}")
