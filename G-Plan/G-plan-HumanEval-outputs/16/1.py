
def closest_integer(value: str) -> int:
    def round_away_from_zero(num: float) -> int:
        return int(num + 0.5) if num > 0 else int(num - 0.5)

    float_value = float(value)
    floor_value = int(float_value)
    ceil_value = floor_value + 1

    if abs(float_value - floor_value) == abs(float_value - ceil_value):
        return ceil_value if float_value > 0 else floor_value
    else:
        return ceil_value if abs(float_value - ceil_value) < abs(float_value - floor_value) else floor_value

if __name__ == "__main__":
    value = input().strip()
    print(closest_integer(value))
