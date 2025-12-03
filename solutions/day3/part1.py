from solutions.common.load_lines import load_lines

def main():
    banks = load_lines(3)
    jolts: list[int] = []
    for bank in banks:
        jolt = get_bank_jolt(bank)
        jolts.append(jolt)
    print(jolts)
    print(sum(jolts))

def get_bank_jolt(bank: str) -> int:
    jolt_levels = ['9', '8', '7', '6', '5', '4', '3', '2', '1']
    for left_jolt_level in jolt_levels:
        left_jolt_index = bank.find(left_jolt_level)
        if left_jolt_index in [len(bank) - 1, -1]:
            continue
        for right_jolt_level in jolt_levels:
            right_jolt_index = bank.find(right_jolt_level, left_jolt_index + 1)
            if right_jolt_index == -1:
                continue
            # both left and right found, this is largest
            return int(left_jolt_level + right_jolt_level)
    # unlikely
    raise ValueError(f"No valid jolt pair found in bank: {bank!r}")
