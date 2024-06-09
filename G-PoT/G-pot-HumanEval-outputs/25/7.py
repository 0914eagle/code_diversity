
def multiply(a: int, b: int) -> int:
    
    return (abs(a) % 10) * (abs(b) % 10) % 10

# Test cases
print(multiply(148, 412))  # Output: 16
print(multiply(19, 28))    # Output: 72
print(multiply(2020, 1851))  # Output: 0
print(multiply(14, -15))   # Output: 20
