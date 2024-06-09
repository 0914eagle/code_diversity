
def hex_key(num: str) -> int:
    
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    prime_digits = ['2', '3', '5', '7', 'B', 'D']
    prime_values = [2, 3, 5, 7, 11, 13]
    count = 0
    for digit in num:
        if digit in prime_digits and int(digit, 16) in prime_values:
            count += 1
    return count

