
def get_unit_digit(num: int) -> int:
    return abs(num) % 10

def multiply(a: int, b: int) -> int:
    unit_digit_a = get_unit_digit(a)
    unit_digit_b = get_unit_digit(b)
    result = unit_digit_a * unit_digit_b
    return result

# Input parsing
a, b = map(int, input().split())
print(multiply(a, b))
