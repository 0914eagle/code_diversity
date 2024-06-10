
def multiply(a: int, b: int) -> int:
    return abs(a % 10) * abs(b % 10)

# Read input integers
a, b = map(int, input().split())

# Calculate and print the product of unit digits
print(multiply(a, b))
