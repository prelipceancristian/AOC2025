from solutions.common.load_lines import load_comma_separated_entries

def get_factors(n: int):
    k = 1
    while k < n:
        if n % k == 0:
            yield k
        k += 1


def main():
    entries = load_comma_separated_entries(2)
    correct_entries: list[int] = []
    for entry in entries:
        range_start_str, range_end_str = entry.split('-', 2)
        range_start = int(range_start_str)
        range_end = int(range_end_str)
        
        # lengths are different at most by one. split into two separate cases, 
        # so the lengths are equal in each case
        cases: list[tuple[int, int]] = []
        if len(range_end_str) != len(range_start_str):
            cases.append((range_start, int(len(range_start_str) * '9')))
            cases.append((10 ** len(range_start_str), range_end))
        else:
            cases.append((range_start, range_end))

        local_correct_entries: list[int] = []
        for case in cases:
            start_length = len(str(case[0]))
            potential_length_list = get_factors(start_length)
            for potential_length in potential_length_list:
                candidate_chunk_str = str(case[0])[:potential_length]
                candidate_chunk = int(candidate_chunk_str)
                while True:
                    candidate_chunk_str = str(candidate_chunk)
                    candidate = int((start_length // potential_length) * candidate_chunk_str)
                    if case[0] <= candidate <= case[1]:
                        if not candidate in local_correct_entries:
                            local_correct_entries.append(candidate)
                    candidate_chunk += 1
                    if candidate > case[1]:
                        break
        correct_entries += local_correct_entries
            
    # print(correct_entries)
    print(sum(correct_entries))
