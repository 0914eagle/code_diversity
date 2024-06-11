def largest_divisor(n: int) -> int:
    
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return i
    return n

