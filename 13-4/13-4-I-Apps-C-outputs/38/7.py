
def is_hill_number(n):
    if n < 1:
        return False
    digits = [int(d) for d in str(n)]
    if len(digits) == 1:
        return True
    if digits[0] > digits[1]:
        return False
    for i in range(1, len(digits) - 1):
        if digits[i] > digits[i + 1]:
            return False
    if digits[len(digits) - 1] < digits[len(digits) - 2]:
        return False
    return True

def count_hill_numbers(n):
    count = 0
    for i in range(1, n + 1):
        if is_hill_number(i):
            count += 1
    return count

