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


inp = read_input(2024, 5, source="sample")
rules = [tuple(map(int, r.split("|"))) for r in inp[: inp.index("")]]
updates = [list(map(int, u.split(","))) for u in inp[inp.index("") + 1 :]]

first_pages = [rule[0] for rule in rules]
second_pages = [rule[1] for rule in rules]

first_page = list(set(first_pages).difference(set(second_pages)))[0]
LAST_PAGE = list(set(second_pages).difference(set(first_pages)))[0]
ALL_PAGES = list(set(first_pages).union(set(second_pages)))
RULE_DICT = {fp: [r[1] for r in rules if r[0] == fp] for fp in first_pages}


order = tree_search_order([first_page])

for update in updates:
    order_indexes = [order.index(v) for v in update]
    if all([order_indexes[i] > order_indexes[i - 1] for i in range(1, len(order_indexes))]):
        print(f"{update} is valid!")
