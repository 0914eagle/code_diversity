
def get_unit_digit(num: int) -> int:
    return abs(num) % 10

def multiply(a: int, b: int) -> int:
    unit_a = get_unit_digit(a)
    unit_b = get_unit_digit(b)
    return unit_a * unit_b

a, b = map(int, input().split())
print(multiply(a, b))
