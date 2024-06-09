
def solve(a):
    str_a = str(a)
    digits = [int(digit) for digit in str_a if digit in "1689"]
    for i in range(len(digits)):
        for j in range(i+1, len(digits)):
            if (digits[i] * 10 + digits[j]) % 7 == 0:
                return int("".join(str(digit) for digit in [digits[i], digits[j]]))
    return 0

