

if __name__ == "__main__":
    with open("day1_input.txt", "r") as f:
        depths = f.read()
        depths = depths.split("\n")

    depths = [int(i) for i in depths]

    diffs = [depths[i + 1] - depths[i] for i in range(0, len(depths) - 1)]
    depth_increases = len([i for i in diffs if i > 0])
    print(f"depth increases: {depth_increases}")

    # part 2 - window method

    windows = [sum(depths[i:i+3]) for i in range(0, len(depths) - 2)]
    window_diffs = [windows[i + 1] - windows[i] for i in range(0, len(windows) - 1)]
    window_depth_increases = len([i for i in window_diffs if i > 0])
    print(f"window depth increases: {window_depth_increases}")