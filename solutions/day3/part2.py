from solutions.common.load_lines import load_lines

def main():
    banks = load_lines(3)
    jolts: list[int] = []
    for bank in banks:
        jolt = get_bank_jolt(bank)
        jolts.append(jolt)
    # print(jolts)
    print(sum(jolts))

def get_bank_jolt(bank: str) -> int:
    result = get_bank_jolt_recursive(bank)
    if not result[0]:
        raise ValueError("Failed to find a combination of length 12")
    return int(result[1])

# could be optimized, as some numbers might not even appear in the bank
jolt_levels = ['9', '8', '7', '6', '5', '4', '3', '2', '1']
joltage_length = 12

def get_bank_jolt_recursive(bank: str, n: int = 0, start_index: int = -1) -> tuple[bool, str]:
    if n >= joltage_length:
        return (True, '')
    for jolt_level in jolt_levels:
        jolt_index = bank.find(jolt_level, start_index + 1)
        if jolt_index == -1 or jolt_index > len(bank) - joltage_length + n:
            continue
        # move onto the next position, limiting to search only from the last fixed index 
        result = get_bank_jolt_recursive(bank, n + 1, jolt_index)
        if not result[0]:
            continue
        return (True, jolt_level + result[1])
    return (False, '')
