from solutions.common.load_lines import load_lines
from solutions.day8.part1 import calculate_distances, get_closest_points, get_coords


def main():
    lines = load_lines(8)
    coords_list = list(map(get_coords, lines))
    distances: list[list[float]] = calculate_distances(coords_list)
    networks: list[set[tuple[int, int, int]]] = []
    for coord in coords_list:
        networks.append({coord})
    last_coord_1 = coords_list[0]
    last_coord_2 = coords_list[0]
    while len(networks) != 1:
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
        last_coord_1 = first_coord
        last_coord_2 = second_coord
        print(len(result_network))

    # for net in networks:
    #     print(net)
    print(last_coord_1, last_coord_2)