
def closest_integer(value: str) -> int:
    def round_away_from_zero(num: float) -> int:
        return int(num + 0.5) if num > 0 else int(num - 0.5)

    num = float(value)
    floor_val = int(num)
    ceil_val = floor_val + 1

    if abs(num - floor_val) == abs(num - ceil_val):
        return ceil_val if num > 0 else floor_val
    else:
        return ceil_val if abs(num - ceil_val) < abs(num - floor_val) else floor_val

if __name__ == "__main__":
    value = input().strip()
    result = closest_integer(value)
    print(result)
