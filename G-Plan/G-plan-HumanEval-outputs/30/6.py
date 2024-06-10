
from typing import List

def has_even_digit(num: int) -> bool:
    return any(int(digit) % 2 == 0 for digit in str(num))

def unique_digits(x: List[int]) -> List[int]:
    return sorted([num for num in x if not has_even_digit(num)])

# Test the function with example inputs
if __name__ == "__main__":
    x = list(map(int, input().strip().split()))
    result = unique_digits(x)
    print(result)
