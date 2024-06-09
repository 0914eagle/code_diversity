
def is_hill_number(n):
    if n < 2:
        return True
    prev_digit = None
    is_rising = False
    for digit in str(n):
        if prev_digit is None:
            prev_digit = digit
            continue
        if prev_digit == digit:
            is_rising = False
        elif prev_digit < digit:
            if is_rising:
                return False
            is_rising = True
        else:
            return False
        prev_digit = digit
    return True

def count_hill_numbers(n):
    count = 0
    for i in range(1, n+1):
        if is_hill_number(i):
            count += 1
    return count

