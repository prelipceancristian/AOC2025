from solutions.common.load_lines import load_lines


def main():
    lines = load_lines(5)
    line_break_index = lines.index("\n")
    range_lines = lines[:line_break_index]
    ingredient_lines = lines[line_break_index+1:]
    ranges = list(map(line_to_range, range_lines))
    fresh_counter = 0
    for ingredient_line in ingredient_lines:
        ingredient = int(ingredient_line)
        for range in ranges:
            if range[0] <= ingredient <= range[1]:
                fresh_counter += 1
                break
    print(fresh_counter)


def line_to_range(line: str) -> tuple[int, int]:
    splitted = line.split('-')
    lower_bound = int(splitted[0])
    higher_bound = int(splitted[1])
    return (lower_bound, higher_bound)