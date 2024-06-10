
def closest_integer(value: str) -> int:
    def round_away_from_zero(num: float) -> int:
        return int(num + 0.5) if num > 0 else int(num - 0.5)

    def closest_integer_rounding(value: float) -> int:
        floor_value = int(value)
        ceil_value = floor_value + 1
        if abs(value - floor_value) == abs(value - ceil_value):
            return ceil_value if value > 0 else floor_value
        return ceil_value if abs(value - ceil_value) < abs(value - floor_value) else floor_value

    float_value = float(value)
    return closest_integer_rounding(float_value) if '.' in value else int(value)

if __name__ == "__main__":
    value = input().strip()
    print(closest_integer(value))
