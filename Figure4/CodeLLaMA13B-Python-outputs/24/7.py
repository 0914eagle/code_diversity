def largest_divisor(n: int) -> int:
    
    i = int(n ** 0.5)
    while n % i != 0:
        i -= 1
    return i


if __name__ == "__main__":
    import do