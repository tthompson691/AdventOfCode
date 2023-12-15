import re

from utils import pull_input_directly


def determine_card_value(num_winners):
    if num_winners != 0:
        return 2 ** (num_winners - 1)
    else:
        return 0


if __name__ == "__main__":
    cards = pull_input_directly(2023, 4)[:-1]

    total_value = 0
    card_dict = {}
    for card in cards:
        winners, ours = card.split(" | ")
        card_num = int(re.findall("[0-9]+", winners.split(": ")[0])[0])
        card_dict[card_num] = {}
        winners = set(map(int, re.findall("[0-9]+", winners.split(": ")[1])))
        ours = set(map(int, re.findall("[0-9]+", ours)))
        num_winners = len(winners.intersection(ours))
        total_value += determine_card_value(num_winners)

        card_dict[card_num]["total_owned"] = 1
        card_dict[card_num]["num_winners"] = num_winners

    print(f"PART 1: {total_value}")

    for card in card_dict:
        for x in range(card + 1, card + 1 + card_dict[card]["num_winners"]):
            card_dict[x]["total_owned"] += card_dict[card]["total_owned"]

    p2_sum = sum([v["total_owned"] for _, v in card_dict.items()])
    print(f"PART 2: {p2_sum}")
