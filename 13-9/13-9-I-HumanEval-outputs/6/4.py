
def hex_key(num: str) -> int:
    
    prime_digits = [2, 3, 5, 7, 11, 13]
    count = 0
    for digit in num:
        if digit.isdigit():
            if int(digit) in prime_digits:
                count += 1
        elif digit.upper() == 'A':
            count += 1
        elif digit.upper() == 'B':
            count += 1
        elif digit.upper() == 'D':
            count += 1
    return count

