def fizz_buzz(n: int):
    
    if n % 11 in [1, 3]:
        return 1
    elif n % 13 in [1, 3]:
        return 2
    else:
        return 0


