def largest_divisor(n: int) -> int:
    
    divisor = n // 2
    while not n % divisor == 0:
        divisor -= 1
    return divisor


if __name__ == "__main__":
    import doctest
