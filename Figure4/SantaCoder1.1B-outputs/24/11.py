def largest_divisor(n: int) -> int:
    
    if n % 2 == 0:
        return n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return i
    return n


