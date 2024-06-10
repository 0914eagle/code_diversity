
def multiply(a: int, b: int) -> int:
    return abs(a % 10) * abs(b % 10)

a, b = map(int, input().split())
print(multiply(a, b))
