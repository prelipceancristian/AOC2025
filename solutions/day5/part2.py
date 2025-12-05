from solutions.common.load_lines import load_lines
from solutions.day5.part1 import line_to_range


def main():
    lines = load_lines(5)
    line_break_index = lines.index("\n")
    range_lines = lines[:line_break_index]
    ranges = list(map(line_to_range, range_lines))

    fully_merged = merge_overlapping_ranges(ranges)
    total = sum(map(lambda r: r[1] - r[0] + 1, fully_merged))
    print(total)


def is_overlap(range1: tuple[int, int], range2: tuple[int, int]) -> bool:
    return min(range1[1], range2[1]) >= max(range1[0], range2[0])

def merge_ranges(range1: tuple[int, int], range2: tuple[int, int]) -> tuple[int, int]:
    return (min(range1[0], range2[0]), max(range1[1], range2[1])) 

def try_merge(ranges: list[tuple[int, int]]):
    for i in range(len(ranges)):
        for j in range(i + 1, len(ranges)):
            if is_overlap(ranges[i], ranges[j]):
                merged = merge_ranges(ranges[i], ranges[j])
                ranges[i] = merged
                ranges.pop(j)
                return
            
def merge_overlapping_ranges(ranges: list[tuple[int, int]]):
    while True:
        length = len(ranges)
        try_merge(ranges)
        new_length = len(ranges)
        if length == new_length:
            return ranges
