from solutions.common.load_lines import load_lines

def main():
    lines = load_lines(1)
    lock_position = 50
    lock_postitions = 100
    zeros_hit = 0
    for line in lines:
        sign = 1 if line[0] == "R" else -1
        value = int(line[1:])
        lock_position = (lock_position + sign * value) % lock_postitions
        if lock_position == 0:
            zeros_hit += 1

    print(zeros_hit)