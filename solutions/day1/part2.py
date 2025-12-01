from solutions.common.load_lines import load_lines

def main():
    lines = load_lines(1)
    lock_position = 50
    positions_count = 100
    zeros_hit = 0
    for line in lines:
        sign = 1 if line[0] == "R" else -1
        value = int(line[1:])
        for _ in range(value):
            lock_position += sign
            lock_position = lock_position % positions_count
            if lock_position == 0:
                zeros_hit += 1

    print(zeros_hit)