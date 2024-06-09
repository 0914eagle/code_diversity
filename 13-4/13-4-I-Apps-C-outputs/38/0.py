
def is_hill_number(n):
    if n < 2:
        return True
    
    prev_digit = None
    is_rising = False
    is_falling = False
    
    for digit in str(n):
        if prev_digit is None:
            prev_digit = digit
            continue
        
        if digit == prev_digit:
            continue
        
        if digit > prev_digit:
            if is_falling:
                return False
            is_rising = True
        else:
            if is_rising:
                return False
            is_falling = True
        
        prev_digit = digit
    
    return True

def count_hill_numbers(n):
    count = 0
    for i in range(1, n+1):
        if is_hill_number(i):
            count += 1
    return count

