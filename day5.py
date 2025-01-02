from functools import cmp_to_key


class Order:
    def __init__(self, smaller, bigger):
        self.smaller = smaller
        self.bigger = bigger


def is_bigger(a: int, compare_to: []):
    relevant_order = [order for order in ordering if order.bigger == a]
    for b in compare_to:
        for o in relevant_order:
            if b == o.smaller:
                return True
    return False


def compare(a: int, b: int):
    for o in ordering:
        if a == o.bigger and b == o.smaller:
            return 1
        if a == o.smaller and b == o.bigger:
            return -1
    return 0


def part_1():
    correct_orders = []
    result = 0
    for order in orders:
        is_correct = True
        for i in range(len(order)-1):
            if is_bigger(order[i], order[i+1:]):
                is_correct = False
                break
        if is_correct:
            correct_orders.append(order)
    for i in range(len(correct_orders)):
        result += correct_orders[i][int(len(correct_orders[i])/2)]
    return result


def part_2():
    incorrect_orders = []
    result = 0
    for order in orders:
        is_correct = True
        for i in range(len(order)-1):
            if is_bigger(order[i], order[i+1:]):
                is_correct = False
                break
        if not is_correct:
            incorrect_orders.append(order)
    for incorrect_order in incorrect_orders:
        order = list(sorted(incorrect_order, key=cmp_to_key(compare)))
        result += order[int(len(order)/2)]
    return result


def get_input():
    with open(path) as file:
        lines = file.read().splitlines()
        idx = 0
        while lines[idx] != "":
            ordering.append(
                Order(int(lines[idx].split('|')[0]), int(lines[idx].split('|')[1])))
            idx += 1
        idx += 1
        while idx < len(lines):
            orders.append(list(map(int, lines[idx].split(','))))
            idx += 1
    return ordering, orders


if __name__ == '__main__':
    path = "inputs/day5"
    print("==== AOC 2024 DAY05 =====")
    ordering = []
    orders = []
    get_input()
    print(f"Part1 solution: {part_1()}")
    print(f"Part2 solution: {part_2()}")
