def fizz_buzz(n: int):
    
    if n < 1:
        return 0
    if n % 11 in (1, 3):
        return 1
    if n % 13 in (1, 3):
        return 2
    return 0


