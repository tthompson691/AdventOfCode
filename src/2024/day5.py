from utils.utils import read_input


def tree_search_order(ordered_pages_searched):
    cur_page = ordered_pages_searched[-1]
    if cur_page == LAST_PAGE:
        if set(ordered_pages_searched) == set(ALL_PAGES):
            return ordered_pages_searched
    else:
        for next_page in RULE_DICT[cur_page]:
            res = tree_search_order(ordered_pages_searched + [next_page])
            if res:
                return res


inp = read_input(2024, 5, source="real")
rules = [tuple(map(int, r.split("|"))) for r in inp[: inp.index("")]]
updates = [list(map(int, u.split(","))) for u in inp[inp.index("") + 1 :]]
p1_sum = p2_sum = 0
for update in updates:
    applicable_rules = [rule for rule in rules if all([r in update for r in rule])]
    first_pages = [rule[0] for rule in applicable_rules]
    second_pages = [rule[1] for rule in applicable_rules]

    first_page = list(set(first_pages).difference(set(second_pages)))[0]
    LAST_PAGE = list(set(second_pages).difference(set(first_pages)))[0]
    ALL_PAGES = list(set(first_pages).union(set(second_pages)))
    RULE_DICT = {fp: [r[1] for r in applicable_rules if r[0] == fp] for fp in first_pages}

    order = tree_search_order([first_page])
    if order == update:
        p1_sum += update[len(update) // 2]
    else:
        p2_sum += order[len(order) // 2]

print(f"PART 1: {p1_sum}")
print(f"PART 2: {p2_sum}")
