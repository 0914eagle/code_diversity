
def solve(n):
    lucky_digits = ["4", "7"]
    lucky_numbers = []
    for i in range(1, n+1):
        if all(digit in lucky_digits for digit in str(i)):
            lucky_numbers.append(i)
    return lucky_numbers.index(n) + 1

