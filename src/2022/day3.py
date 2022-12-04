from utils.utils import pull_input_directly
import string


def get_common_item(sack):
    comp1 = set(sack[:int((len(sack) / 2))])
    comp2 = set(sack[int((len(sack) / 2)):])

    return list(comp1.intersection(comp2))[0]


if __name__ == "__main__":
    sacks = pull_input_directly(2022, 3)[:-1]
    triple_sacks = [sacks[i:i+3] for i in range(0, len(sacks), 3)]
    vals = {j: i + 1 for i, j in enumerate(string.ascii_letters)}
    badges = [list(set(ts[0]).intersection(set(ts[1])).intersection(set(ts[2])))[0] for ts in triple_sacks]

    # part 1
    print(sum(vals[get_common_item(sack)] for sack in sacks))
    # part 2
    print(sum(vals[b] for b in badges))


