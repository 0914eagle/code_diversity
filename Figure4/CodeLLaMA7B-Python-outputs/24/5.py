def largest_divisor(n: int) -> int:
    
    # Your code here
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i


if