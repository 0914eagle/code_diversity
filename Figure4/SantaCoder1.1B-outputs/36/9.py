def fizz_buzz(n: int):
    
    if n < 100:
        return 0
    if n % 11 == 7 or n % 13 == 7:
        return 1
    return 0


