from solutions.common.load_lines import load_lines


def main():
    lines = list(map(lambda l : l.strip(), load_lines(7)))
    beams = [True if lines[0][i] == 'S' else False for i in range(len(lines[0]))]
    split_count = 0
    for line in lines[1:]:
        beams_copy = beams.copy() # should be enough
        for i in range(len(beams)):
            if line[i] == '^' and beams[i]: # there's a beam above the ^
                beams_copy[i - 1] = True
                beams_copy[i + 1] = True
                beams_copy[i] = False
                split_count += 1
        beams = beams_copy
    print(split_count)
            