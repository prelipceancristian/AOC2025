from solutions.common.load_lines import load_lines
import math

def main():
    lines = load_lines(6)
    nums: list[list[int]] = []
    for line in lines[:len(lines) - 1]:
        line_nums = list(map(lambda x: int(x), line.split()))
        nums.append(line_nums)

    operators = lines[-1].split()
    column_results: list[int] = []
    for index in range(len(nums[0])):
        operator = operators[index]
        members = [nums[i][index] for i in range(len(nums))]
        column_result = sum(members) if operator == '+' else math.prod(members)
        column_results.append(column_result)

    print(sum(column_results))