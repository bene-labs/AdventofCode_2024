
def part_1(reports):
    result = 0
    for seq in reports:
        if validate_sequence(seq):
            result += 1
    return result


def part_2(reports):
    result = 0
    for seq in reports:
        if validate_sequence(seq):
            result += 1
            continue
        valid = False
        for i in range(len(seq)):
            s = seq.copy()
            s.pop(i)
            if validate_sequence(s):
                valid = True
                break
        if valid:
            result += 1
    return result


def validate_sequence(seq):
    asc = None
    for nb1, nb2 in zip(seq, seq[1:]):
        if asc is None:
            asc = nb1 < nb2
        elif (asc and nb1 > nb2) or (not asc and nb1 < nb2):
            return False
        if not (0 < abs(nb1 - nb2) <= 3):
            return False
    return True


def get_input(is_test=False):
    list1 = []
    with open('inputs/day2' + ("Test" if is_test else "")) as file:
        for line in file.readlines():
            list1.append((list(map(int, line.split(" ")))))
    return list1


if __name__ == '__main__':
    print(part_1(get_input()))
    print(part_2(get_input()))
