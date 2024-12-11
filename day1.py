def part_1(list1, list2):
    result = 0
    for i in range(len(list1)):
        min1 = min(list1)
        min2 = min(list2)
        list1.remove(min1)
        list2.remove(min2)
        result += abs(min1 - min2)
    return result


def part_2(list1, list2):
    result = 0
    for locationId in list1:
        result += locationId * list2.count(locationId)
    return result


def get_input(is_test=False):
    list1 = []
    list2 = []
    with open('inputs/day1' + ("Test" if is_test else "")) as file:
        for line in file.readlines():
            list1.append(int(line.split(" ")[0]))
            list2.append(int(line.split(" ")[-1]))
    return list1, list2


if __name__ == '__main__':
    l1, l2 = get_input()
    print(f"Part1 solution: {part_1(l1.copy(), l2.copy())}")
    print(f"Part2 solution: {part_2(l1, l2)}")
