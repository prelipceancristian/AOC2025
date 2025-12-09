from solutions.common.load_lines import load_lines


def main():
    lines = load_lines(9)
    coords = list(map(get_coords, lines))
    max_p1: tuple[int, int] = coords[0]
    max_p2: tuple[int, int] = coords[1]
    max_area = get_area(max_p1, max_p2)
    for p1 in coords:
        for p2 in coords:
            area = get_area(p1, p2)
            if area > max_area:
                max_area = area
                max_p1 = p1
                max_p2 = p2
    print(max_area)


def get_coords(line: str) -> tuple[int, int]:
    splitted = line.split(',')
    return (int(splitted[0]), int(splitted[1]))


def get_area(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    return (abs(p1[0] - p2[0]) + 1) * (1 + abs(p1[1] - p2[1]))