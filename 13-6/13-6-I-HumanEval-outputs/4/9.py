
def hex_key(num: str) -> int:
    
    prime_digits = set([2, 3, 5, 7, 11, 13])
    count = 0
    for digit in num:
        if digit in prime_digits:
            count += 1
    return count

