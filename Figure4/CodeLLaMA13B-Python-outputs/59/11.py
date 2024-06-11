def largest_prime_factor(n: int):
    
    largest = 0
    for i in range(2, n):
        if n % i == 0:
            largest = i
    return largest


if __name__ == "__main__":
    import doctest

