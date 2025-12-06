import math
from solutions.common.load_lines import load_lines


def main():
    lines = load_lines(6)
    operators = lines[-1].split()
    nums: list[int] = []
    totals: list[int] = []
    for column_index in range(len(lines[0]) - 1):
        column = [lines[i][column_index] for i in range(len(lines))]
        if all(c.isspace() for c in column):
            totals.append(calculate_operation(nums, operators))
            continue
        n = determine_column_number(lines, column_index)
        nums.append(n)

    # for the last equation that was not processed
    totals.append(calculate_operation(nums, operators))
    print(sum(totals))

def determine_column_number(lines: list[str], column_index: int):
    n = 0
    for i in range(len(lines) - 1):
        ch = lines[i][column_index]
        if not ch.isspace():
            n = n * 10 + int(ch)
    return n

def calculate_operation(nums: list[int], operators: list[str]) -> int:
    operator = operators.pop(0)
    result = sum(nums) if operator == '+' else math.prod(nums)
    nums.clear()
    return result