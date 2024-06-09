
def solve(a):
    a_str = str(a)
    digits = [int(i) for i in a_str if i in '1689']
    if len(digits) < 4:
        return 0
    digits.sort()
    result = int(''.join(str(i) for i in digits))
    if result % 7 == 0:
        return result
    else:
        return 0

