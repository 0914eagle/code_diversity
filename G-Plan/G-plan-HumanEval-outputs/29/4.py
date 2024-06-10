
def is_simple_power(x: int, n: int) -> bool:
    if x == 1:
        return True
    if x < n:
        return False
    while x % n == 0:
        x //= n
    return x == 1

# Test cases
print(is_simple_power(1, 4))  # True
print(is_simple_power(2, 2))  # True
print(is_simple_power(8, 2))  # True
print(is_simple_power(3, 2))  # False
print(is_simple_power(3, 1))  # False
print(is_simple_power(5, 3))  # False
