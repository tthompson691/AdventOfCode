from utils.utils import pull_input_directly
import pandas as pd
import re

if __name__ == "__main__":
    with open("/Users/travisthompson/REPOS/AdventOfCode/src/2023/day5samp.txt", "r") as f:
        almanac_raw = f.read().splitlines()
        almanac_raw += [""]

    # almanac_raw = pull_input_directly(2023, 5)

    almanac = {}
    map_vals = []
    for line in almanac_raw:
        if "seeds" in line:
            seeds = list(map(int, re.findall("[0-9]+", line)))
            continue

        if "-to-" in line:
            map_title = line
        elif line != '':
            map_vals.append(list(map(int, re.findall("[0-9]+", line))))
        elif line == '' and map_vals != []:
            almanac[map_title] = pd.DataFrame(map_vals, columns=["destination", "source", "range"])
            map_vals = []

    min_loc = None
    for seed in seeds:
        seed_path = [seed]
        for _, mapper in almanac.items():
            cur_step = seed_path[-1]
            matching_range = mapper[
                (cur_step >= mapper["source"]) & (cur_step < mapper["source"] + mapper["range"])
            ].reset_index(drop=True)
            if not matching_range.empty:
                diff = cur_step - matching_range.loc[0, "source"]
                seed_path.append(matching_range.loc[0, "destination"] + diff)

        if not min_loc:
            min_loc = seed_path[-1]
        elif seed_path[-1] < min_loc:
            min_loc = seed_path[-1]

    print(f"PART 1: {min_loc}")

    p2_seeds = [(seeds[x], seeds[x+1]) for x in range(0, len(seeds)-1, 2)]

    p2_ans = None
    for seedrange in p2_seeds:
        sourcemin = seedrange[0]
        sourcemax = sum(seedrange) - 1
        for a, mapper in almanac.items():
            print(f"CHECKING {a}")
            matching_ranges = mapper[(
                    ((mapper["source"] <= sourcemin) & (mapper["source"] + mapper["range"]) >= sourcemin)
             | ((mapper["source"] <= sourcemax) & (mapper["source"] + mapper["range"] >= sourcemax))
            )].reset_index(drop=True)
            if not matching_ranges.empty:
                diff = matching_ranges.loc[0, "destination"] - matching_ranges.loc[0, "source"]
                if (
                        matching_ranges.loc[0, "source"]
                        <= sourcemin <
                        matching_ranges.loc[0, "source"] + matching_ranges.loc[0, "range"]
                ):
                    sourcemin = sourcemin + diff

                if (
                        matching_ranges.loc[0, "source"]
                        <= sourcemax <
                        matching_ranges.loc[0, "source"] + matching_ranges.loc[0, "range"]
                ):
                    sourcemax = sourcemax + diff
                sourcemin

        if not p2_ans:
            p2_ans = sourcemin
        elif sourcemin < p2_ans:
            p2_ans = sourcemin


            matching_ranges
    sourcemin


