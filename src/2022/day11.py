from numpy import prod


class Monkey:
    def __init__(self, starting_items, operation, divisor):
        self.items = starting_items
        self.truemonkey = None
        self.falsemonkey = None
        self.operation = operation
        self.total_items_inspected = 0
        self.divisor = divisor

    def check_items(self, part_1_or_2=1, divisor=None):
        self.total_items_inspected += len(self.items)
        for item in self.items:
            item = self.operation(item)
            if part_1_or_2 == 1:
                item //= 3
            else:
                item %= divisor

            if item % self.divisor == 0:
                self.truemonkey.items.append(int(item))
            else:
                self.falsemonkey.items.append(int(item))

        self.items = []


def reset_monkeys():
    m0 = Monkey(
        starting_items=[62, 92, 50, 63, 62, 93, 73, 50], operation=lambda x: x * 7, divisor=2
    )
    m1 = Monkey(starting_items=[51, 97, 74, 84, 99], operation=lambda x: x + 3, divisor=7)
    m2 = Monkey(starting_items=[98, 86, 62, 76, 51, 81, 95], operation=lambda x: x + 4, divisor=13)
    m3 = Monkey(starting_items=[53, 95, 50, 85, 83, 72], operation=lambda x: x + 5, divisor=19)
    m4 = Monkey(starting_items=[59, 60, 63, 71], operation=lambda x: x * 5, divisor=11)
    m5 = Monkey(starting_items=[92, 65], operation=lambda x: x**2, divisor=5)
    m6 = Monkey(starting_items=[78], operation=lambda x: x + 8, divisor=3)
    m7 = Monkey(starting_items=[84, 93, 54], operation=lambda x: x + 1, divisor=17)
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


def calculate_monkey_business(_monkeys, num_rounds, part_1_or_2):
    divisor = prod([m.divisor for m in _monkeys])
    for _ in range(num_rounds):
        for monkey in _monkeys:
            monkey.check_items(part_1_or_2=part_1_or_2, divisor=divisor)

    _monkeys.sort(key=lambda x: x.total_items_inspected, reverse=True)
    return _monkeys[0].total_items_inspected * _monkeys[1].total_items_inspected


if __name__ == "__main__":
    monkeys = reset_monkeys()

    print(calculate_monkey_business(_monkeys=monkeys, num_rounds=20, part_1_or_2=1))

    monkeys = reset_monkeys()

    print(calculate_monkey_business(_monkeys=monkeys, num_rounds=10000, part_1_or_2=2))
