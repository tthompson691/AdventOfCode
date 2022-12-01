from utils import read_input


def iter_paths(current_cave, nests, prev_caves=[], endpoints=0):
    for k in current_cave:
        if k != "prev caves" and k != "end":
            current_cave["prev caves"] = prev_caves + [k]
            # print(k)
            next_dict = {
                i: None
                for i in nests[k]
                if i.isupper() or (i.islower() and i not in current_cave["prev caves"])
            }
            if next_dict:
                if "end" in next_dict:
                    endpoints += 1
                next_dict["prev caves"] = current_cave["prev caves"]
                current_cave[k], endpoints = iter_paths(
                    next_dict,
                    nests,
                    prev_caves=current_cave["prev caves"],
                    endpoints=endpoints,
                )
            else:
                pass
    current_cave["prev caves"] = current_cave["prev caves"][:-1]
    return current_cave, endpoints


def check_if_double_cave(caves):
    caves = [i for i in caves if i.islower() and i != "start" and i != "end"]
    if caves:
        return not len(caves) == len(set(caves))
    else:
        return False


def iter_paths2(current_cave, nests, prev_caves=[], endpoints=0):
    for k in current_cave:
        if k != "prev caves" and k != "end":
            current_cave["prev caves"] = prev_caves + [k]
            doubled = check_if_double_cave(current_cave["prev caves"])
            next_dict = {
                i: None
                for i in nests[k]
                if i.isupper()
                or (i.islower() and i not in current_cave["prev caves"])
                or (i.islower() and not doubled)
            }

            if next_dict:
                if "end" in next_dict:
                    endpoints += 1
                next_dict["prev caves"] = current_cave["prev caves"]
                current_cave[k], endpoints = iter_paths2(
                    next_dict,
                    nests,
                    prev_caves=current_cave["prev caves"],
                    endpoints=endpoints,
                )
            else:
                pass
    current_cave["prev caves"] = current_cave["prev caves"][:-1]
    return current_cave, endpoints


if __name__ == "__main__":
    cave_pairs = [
        (i.split("-")[0], i.split("-")[1]) for i in read_input("day12_input.txt")
    ]
    unique_caves = {cave for cave_pair in cave_pairs for cave in cave_pair}
    nests = {
        cave: {
            i
            for cavey in cave_pairs
            for i in cavey
            if cave in cavey and i != cave and i != "start"
        }
        for cave in unique_caves
    }

    paths = {"start": None, "prev caves": []}

    paths_dict, num_paths = iter_paths(paths, nests)
    print(f"PART 1: {num_paths}")

    paths_dict2, num_paths2 = iter_paths2(paths, nests)
    print(f"PART 2: {num_paths2}")
