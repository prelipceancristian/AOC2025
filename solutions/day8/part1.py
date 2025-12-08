import math
from solutions.common.load_lines import load_lines


def main():
    lines = load_lines(8)
    coords_list = list(map(get_coords, lines))
    distances: list[list[float]] = calculate_distances(coords_list)
    networks: list[set[tuple[int, int, int]]] = []
    for coord in coords_list:
        networks.append({coord})
    for _ in range(1000):
        i, j = get_closest_points(distances)
        first_coord = coords_list[i]
        second_coord = coords_list[j]
        distances[i][j] = float('inf')
        first_network = next(filter(lambda s: first_coord in s, networks))
        second_network = next(filter(lambda s: second_coord in s, networks))
        if first_network == second_network:
            continue # is this enough?
        result_network = first_network.union(second_network)
        networks.remove(first_network)
        networks.remove(second_network)
        networks.append(result_network)
        print(len(result_network))

    # for net in networks:
    #     print(net)
    ordered_lengths = sorted(map(len, networks), reverse=True)
    result = math.prod(ordered_lengths[:3])
    print(result)


def get_coords(line: str) -> tuple[int, int, int]:
    coords = line.split(',')
    return (int(coords[0]), int(coords[1]), int(coords[2]))


def calculate_distances(coords_list: list[tuple[int, int, int]]) -> list[list[float]]:
    distances: list[list[float]] = [[0 for _ in coords_list] for _ in coords_list]
    for i in range(len(coords_list)):
        for j in range(0, i + 1):
            distances[i][j] = float('inf') if i == j else get_distance(coords_list[i], coords_list[j])

    return distances


def get_distance(x: tuple[int, int, int], y: tuple[int, int, int]) -> float:
    return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 + (x[2] - y[2]) ** 2


def get_closest_points(distances: list[list[float]]) -> tuple[int, int]:
    i_min, j_min = 0, 0
    min_distance = distances[0][0]
    for i in range(len(distances)):
        for j in range(i):
            if distances[i][j] < min_distance:
                min_distance = distances[i][j]
                i_min = i
                j_min = j
    return (i_min, j_min)