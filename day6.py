

def get_input(path):
    result = []
    with open(path) as file:
        for line in file.read().splitlines():
           result.append((line.split(':')))
    return result

def part1_calc_possible_results_rec(remaining_numbers: [], possible_results: [], subtotal = 0):
    if len(remaining_numbers) == 0:
        possible_results.append(subtotal)
        return
    part1_calc_possible_results_rec(remaining_numbers[1:], possible_results, subtotal + remaining_numbers[0])
    part1_calc_possible_results_rec(remaining_numbers[1:], possible_results, subtotal * remaining_numbers[0])

def part_1(commands):
    result = 0
    for command in commands:
        test_value, formula = command
        test_value = int(test_value)
        possible_results = []
        part1_calc_possible_results_rec(list(map(int, formula[1:].split(' '))), possible_results)
        if test_value in possible_results:
            result += test_value
    return result


def part2_calc_possible_results_rec(remaining_numbers: [], possible_results: [], subtotal = 0):
    if len(remaining_numbers) == 0:
        possible_results.append(subtotal)
        return
    part2_calc_possible_results_rec(remaining_numbers[1:], possible_results, subtotal + remaining_numbers[0])
    part2_calc_possible_results_rec(remaining_numbers[1:], possible_results, subtotal * remaining_numbers[0])
    part2_calc_possible_results_rec(remaining_numbers[1:], possible_results, int(str(subtotal) + str(remaining_numbers[0])))


def part_2(commands):
    result = 0
    for command in commands:
        test_value, formula = command
        test_value = int(test_value)
        possible_results = []
        part2_calc_possible_results_rec(list(map(int, formula[1:].split(' '))), possible_results)
        if test_value in possible_results:
            result += test_value
    return result



if __name__ == '__main__':
    print(f"Part1 example solution: {part_1(get_input("inputs/day6Test"))}")
    print(f"Part1 solution: {part_1(get_input("inputs/day6"))}")
    print(f"Part2 example solution: {part_2(get_input("inputs/day6Test"))}")
    print(f"Part2 solution: {part_2(get_input("inputs/day6"))}")