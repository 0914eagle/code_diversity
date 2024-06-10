
def is_simple_power(x: int, n: int) -> bool:
    if x < 1 or n < 1:
        return False
    
    while x % n == 0:
        x //= n
        
    return x == 1

# Test the function with provided test cases
print(is_simple_power(1, 4))
print(is_simple_power(2, 2))
print(is_simple_power(8, 2))
print(is_simple_power(3, 2))
print(is_simple_power(3, 1))
print(is_simple_power(5, 3))
