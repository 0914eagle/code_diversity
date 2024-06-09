
def solve(n, k):
    for x in range(n):
        if sum(int(digit) for digit in str(x)) + sum(int(digit) for digit in str(x + 1)) + ... + sum(int(digit) for digit in str(x + k)) == n:
            return x
    return -1

