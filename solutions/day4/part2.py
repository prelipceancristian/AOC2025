from solutions.common.load_lines import load_lines
from solutions.day4.part1 import count_neighbors, load_map

def main():
    lines = load_lines(4)
    map = load_map(lines)
    map_copy = load_map(lines)
    valid = 0
    total_valid = 0
    while True:
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j]:
                    count = count_neighbors(i, j, map)
                    if count < 4:
                        valid += 1
                        map_copy[i][j] = False
        map = map_copy
        if valid == 0:
            break
        total_valid += valid
        valid = 0
    print(total_valid)