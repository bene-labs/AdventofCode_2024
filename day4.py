from typing import List


def part_1(lines: List[str], to_find = "XMAS"):
    result = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            result += count_matches_from(lines, x, y, to_find)
    return result


def count_matches_from(lines: List[str], x: int, y: int, to_find="XMAS"):
    height = len(lines)
    width = len(lines[y])
    matches = 8

    for i in range(len(to_find)):
        if y + i >= height or lines[y+i][x] != to_find[i]:
            matches -= 1
            break
    for i in range(len(to_find)):
        if y - i < 0 or lines[y-i][x] != to_find[i]:
            matches -= 1
            break
    for i in range(len(to_find)):
        if x + i >= width or lines[y][x+i] != to_find[i]:
            matches -= 1
            break
    for i in range(len(to_find)):
        if x - i < 0 or lines[y][x-i] != to_find[i]:
            matches -= 1
            break
    for i in range(len(to_find)):
        if y + i >= height or x + i >= width or lines[y+i][x+i] != to_find[i]:
            matches -= 1
            break
    for i in range(len(to_find)):
        if y + i >= height or x - i < 0 or lines[y + i][x - i] != to_find[i]:
            matches -= 1
            break
    for i in range(len(to_find)):
        if y - i < 0 or x + i >= width or lines[y-i][x+i] != to_find[i]:
            matches -= 1
            break
    for i in range(len(to_find)):
        if y - i < 0 or x - i < 0 or lines[y-i][x-i] != to_find[i]:
            matches -= 1
            break

    return matches


def part_2(lines: List[str]):
    result = 0
    for y in range(1, len(lines) - 1):
        for x in range(1, len(lines[y]) - 1):
            if is_xmas(lines, x, y):
                result += 1
    return result


def is_xmas(lines: List[str], x: int, y: int):
    return (lines[y][x] == 'A' and
            ((lines[y-1][x-1] == 'M' and lines[y+1][x+1] == 'S') or
             (lines[y-1][x-1] == 'S' and lines[y+1][x+1] == 'M')) and
            ((lines[y + 1][x - 1] == 'M' and lines[y - 1][x + 1] == 'S') or
             (lines[y + 1][x - 1] == 'S' and lines[y - 1][x + 1] == 'M')))


def get_test_input():
    with open('inputs/day4Test') as file:
        return file.read().splitlines()


def get_input():
    with open('inputs/day4') as file:
        return file.read().splitlines()


if __name__ == '__main__':
    test_puzzle = get_test_input()
    puzzle = get_input()
    print("==== AOC 2024 DAY04 =====")
    print(f"Part1 example solution: {part_1(test_puzzle)}")
    print(f"Part1 solution: {part_1(puzzle)}")

    print(f"Part2 example solution: {part_2(test_puzzle)}")
    print(f"Part2 solution: {part_2(puzzle)}")
