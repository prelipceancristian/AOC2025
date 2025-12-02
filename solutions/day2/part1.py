from solutions.common.load_lines import load_comma_separated_entries


def main():
    entries = load_comma_separated_entries(2)
    correct_entries: list[int] = []
    for entry in entries:
        range_start_str, range_end_str = entry.split('-', 2)
        range_start = int(range_start_str)
        if len(range_start_str) % 2 == 1:
            range_start = 10 ** len(range_start_str)
            range_start_str = str(range_start)
        range_end = int(range_end_str)
        if range_start > range_end:
            continue
        halfed_range_start = int(range_start_str[:len(range_start_str) // 2])
        while True:
            candidate = int(f'{halfed_range_start}{halfed_range_start}')
            if range_start <= candidate <= range_end:
                correct_entries.append(candidate)
            if candidate > range_end:
                break
            halfed_range_start += 1
    print(sum(correct_entries))
