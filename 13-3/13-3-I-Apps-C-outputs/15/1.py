
def solve(a):
    str_a = str(a)
    digits = [int(digit) for digit in str_a if digit in "1689"]
    if len(digits) < 4:
        return 0
    digits.sort()
    result = int("".join(str(digit) for digit in digits))
    if result % 7 == 0:
        return result
    else:
        return 0

