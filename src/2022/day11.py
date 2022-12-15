from utils.utils import pull_input_directly
from numpy import prod

class Monkey:
    def __init__(self, starting_items, iftrue=None, iffalse=None, operation=None, divisor=None):
        self.items = starting_items
        self.truemonkey = iftrue
        self.falsemonkey = iffalse
        self.operation = operation
        self.total_items_inspected = 0
        self.divisor = divisor

    def check_items(self, div_by_three=True, divisor=None):
        self.total_items_inspected += len(self.items)
        for item in self.items:
            item = self.operation(item)
            if div_by_three:
                item //= 3
            else:
                item %= divisor

            if item % self.divisor == 0:
                self.truemonkey.items.append(item)
            else:
                self.falsemonkey.items.append(item)

        self.items = []


def reset_monkeys(test=False):
    if not test:
        m0 = Monkey(
            starting_items=[62, 92, 50, 63, 62, 93, 73, 50],
            operation=lambda x: x * 7,
            divisor=2
        )
        m1 = Monkey(
            starting_items=[51, 97, 74, 84, 99],
            operation=lambda x: x + 3,
            divisor=7
        )
        m2 = Monkey(
            starting_items=[98, 86, 62, 76, 51, 81, 95],
            operation=lambda x: x + 4,
            divisor=13
        )
        m3 = Monkey(
            starting_items=[53, 95, 50, 85, 83, 72],
            operation=lambda x: x + 5,
            divisor=19
        )
        m4 = Monkey(
            starting_items=[59, 60, 63, 71],
            operation=lambda x: x * 5,
            divisor=11
        )
        m5 = Monkey(
            starting_items=[92, 65],
            operation=lambda x: x ** 2,
            divisor=5
        )
        m6 = Monkey(
            starting_items=[78],
            operation=lambda x: x + 8,
            divisor=3
        )
        m7 = Monkey(
            starting_items=[84, 93, 54],
            operation=lambda x: x + 1,
            divisor=17
        )
        m0.truemonkey = m7
        m0.falsemonkey = m1

        m1.truemonkey = m2
        m1.falsemonkey = m4

        m2.truemonkey = m5
        m2.falsemonkey = m4

        m3.truemonkey = m6
        m3.falsemonkey = m0

        m4.truemonkey = m5
        m4.falsemonkey = m3

        m5.truemonkey = m6
        m5.falsemonkey = m3

        m6.truemonkey = m0
        m6.falsemonkey = m7

        m7.truemonkey = m2
        m7.falsemonkey = m1

        return [m0, m1, m2, m3, m4, m5, m6, m7]
    else:
        # test monkeys from the example######################################
        tm0 = Monkey(
            starting_items=[79, 98],
            operation=lambda x: x * 19,
            divisor=23
        )
        tm1 = Monkey(
            starting_items=[54, 65, 75, 74],
            operation=lambda x: x + 6,
            divisor=19
        )
        tm2 = Monkey(
            starting_items=[79, 60, 97],
            operation=lambda x: x ** 2,
            divisor=13
        )
        tm3 = Monkey(
            starting_items=[74],
            operation=lambda x: x + 3,
            divisor=17
        )
        tm0.truemonkey = tm2
        tm0.falsemonkey = tm3

        tm1.truemonkey = tm2
        tm1.falsemonkey = tm0

        tm2.truemonkey = tm1
        tm2.falsemonkey = tm3

        tm3.truemonkey = tm0
        tm3.falsemonkey = tm1

        return [tm0, tm1, tm2, tm3]


def calculate_monkey_business(_monkeys, num_rounds, divide_by_three):
    divisor = prod([m.divisor for m in _monkeys])
    for i in range(num_rounds):
        # if i in [1, 20, 1000]:
        #     print([f"{monkey.total_items_inspected} " for monkey in _monkeys])
        for monkey in _monkeys:
            monkey.check_items(div_by_three=divide_by_three, divisor=divisor)

    _monkeys.sort(key=lambda x: x.total_items_inspected, reverse=True)
    return _monkeys[0].total_items_inspected * _monkeys[1].total_items_inspected


if __name__ == "__main__":
    monkeys = reset_monkeys(test=True)

    print(calculate_monkey_business(_monkeys=monkeys, num_rounds=20, divide_by_three=True))

    monkeys = reset_monkeys(test=True)

    print(calculate_monkey_business(_monkeys=monkeys, num_rounds=10000, divide_by_three=False))




