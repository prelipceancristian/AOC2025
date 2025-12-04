from solutions.common.load_lines import load_lines

def main():
    lines = load_lines(4)
    map = load_map(lines)
    valid = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j]:
                count = count_neighbors(i, j, map)
                if count < 4:
                    valid += 1
    print(valid)

def load_map(lines: list[str]) -> list[list[bool]]:
    result: list[list[bool]] = [
        [ch == '@' for ch in line]
        for line in lines
    ]
    return result

def count_neighbors(i: int, j: int, map: list[list[bool]]) -> int:
    count = 0
    for offset_x in range(-1, 2):
        for offset_y in range(-1, 2):
            x = i + offset_x
            y = j + offset_y
            if x in range(0, len(map)) and y in range(0, len(map[i])) and not (offset_x == offset_y and offset_x == 0):
                if map[x][y]:
                    count += 1
    return count
