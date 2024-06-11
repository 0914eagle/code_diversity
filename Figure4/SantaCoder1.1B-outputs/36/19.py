def fizz_buzz(n: int):
    
    return sum(1 for i in range(1, n) if i % 11 in (1, 3)) + sum(1 for i in range(1, n) if i % 13 in (1, 3))


if