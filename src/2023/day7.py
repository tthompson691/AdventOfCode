from collections import Counter

import pandas as pd

from utils import pull_input_directly


def score_single_hand(_hand, part=1):
    if part == 1:
        _card_counts = list(Counter(_hand).values())
    else:
        num_jokers = Counter(_hand)["J"]
        handscore = score_single_hand(_hand.replace("J", ""))
        possible_scores = [0, 1, 2, 4, 6, 7]
        if num_jokers in range(1, 5):
            if handscore != 3:
                return possible_scores[possible_scores.index(handscore) + num_jokers]
            else:
                return 5
        elif num_jokers == 5:
            return 7
        else:
            return handscore

    if 5 in _card_counts:
        # 5 of a kind
        return 7
    elif 4 in _card_counts:
        # 4 of a kind
        return 6
    elif set(_card_counts) == {2, 3}:
        # full house
        return 5
    elif 3 in _card_counts:
        # 3 of a kind
        return 4
    elif Counter(_card_counts)[2] == 2:
        # 2 pair
        return 3
    elif 2 in _card_counts:
        # pair
        return 2
    elif 1 in _card_counts:
        # high card
        return 1

    return 0


def determine_hand_ranks(_hands, part=1):
    score_dict = {7: [], 6: [], 5: [], 4: [], 3: [], 2: [], 1: []}
    for _hand in _hands:
        score_dict[score_single_hand(_hand, part=part)].append(_hand)

    for score in score_dict:
        if len(score_dict[score]) > 1:
            score_dict[score] = break_ties(score_dict[score], part=part)

    return score_dict


def break_ties(_hands, part=1):
    heirarchy = "AKQJT98765432" if part == 1 else "AKQT98765432J"

    df = (
        pd.DataFrame({"hand": _hands})
        .assign(**{str(i): [heirarchy.index(h[i]) for h in _hands] for i in range(5)})
        .sort_values(by=list(map(str, range(5))), ascending=True)
        .reset_index(drop=True)
    )
    return df["hand"].tolist()


def get_sum(hand_ranks):
    final_hand_ranks = [y for x in hand_ranks.values() for y in x if x != []]
    final_hand_ranks.reverse()
    return sum([(i + 1) * hand_dict[h] for i, h in enumerate(final_hand_ranks)])


if __name__ == "__main__":
    inp = pull_input_directly(2023, 7)[:-1]
    res = {}
    hands = [h.split(" ")[0] for h in inp]
    bids = [int(h.split(" ")[1]) for h in inp]
    hand_dict = dict(zip(hands, bids))
    p1 = determine_hand_ranks(hands)
    p2 = determine_hand_ranks(hands, part=2)

    print(f"PART 1: {get_sum(p1)}")
    print(f"PART 2: {get_sum(p2)}")
