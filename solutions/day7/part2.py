from solutions.common.load_lines import load_lines


def main():
    lines = list(map(lambda l : l.strip(), load_lines(7)))
    diagram = [[ch == '^' or ch == 'S' for ch in line] for line in lines]
    cache: dict[tuple[int, int], int] = {}
    # by starting from the bottom, 
    # the cache will always be filled with the values for the lines below when moving above
    for i in reversed(range(len(diagram))):
        for j in range(len(diagram[i])):
            if diagram[i][j]:
                # the number of paths that can be taken from one splitter is the sum of the left and right paths
                # n(i, j) = n(i, j - 1) + n(i, j + 1)
                index_left = get_index_of_first_splitter_below(diagram, i, j - 1)
                index_right = get_index_of_first_splitter_below(diagram, i, j + 1)
                left_result = 1 if index_left == -1 else cache[(index_left, j - 1)]
                right_result = 1 if index_right == -1 else cache[(index_right, j + 1)]
                cache[(i, j)] = left_result + right_result
    start_index = lines[0].index('S')
    print(cache[0, start_index])


def get_index_of_first_splitter_below(lines: list[list[bool]], i: int, j: int):
    for index in range(i+1, len(lines)):
        if lines[index][j]:
            return index
    return -1