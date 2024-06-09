
def solve(k, n):
    num_digits = len(str(n))
    min_diff = num_digits
    for i in range(1, num_digits+1):
        for j in range(10**i):
            num = j * 10**(num_digits-i)
            if sum(int(digit) for digit in str(num)) >= k:
                diff = abs(num - n)
                if diff < min_diff:
                    min_diff = diff
                    break
    return min_diff

