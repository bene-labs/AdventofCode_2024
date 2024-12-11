import re


def part_1(instructions: str):
    result = 0
    for mul_instruction in re.findall(r"mul\([0-9]+,[0-9]+\)", instructions):
        num1, num2 = map(int, mul_instruction.removeprefix("mul(").removesuffix(")").split(","))
        result += num1 * num2
    return result


def part_2(instructions: str):
    result = 0
    active = True
    for valid_instruction in re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", instructions):
        if valid_instruction == "do()":
            active = True
            continue
        if valid_instruction == "don't()":
            active = False
            continue
        if not active:
            continue
        num1, num2 = map(int, valid_instruction.removeprefix("mul(").removesuffix(")").split(","))
        result += num1 * num2
    return result


def get_test_input():
    with open('inputs/day3Test') as file:
        return file.read()


def get_input():
    with open('inputs/day3') as file:
        return file.read()


if __name__ == '__main__':
    instruction = get_input()
    print(f"Part1 solution: {part_1(instruction)}")
    print(f"Part2 solution: {part_2(instruction)}")
