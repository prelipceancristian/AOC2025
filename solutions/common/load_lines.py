def load_lines(day: int, is_example: bool = False) -> list[str]:
    base_file_path = "./inputs/examples" if is_example else "./inputs/mine"
    file_path = f"{base_file_path}/day{day}.txt"
    with open(file_path, "r") as f:
        lines = f.readlines()
        return lines
