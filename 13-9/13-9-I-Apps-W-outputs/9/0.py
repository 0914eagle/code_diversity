
def solve(k, n):
    num_digits = len(str(n))
    min_digits = 0
    while num_digits > 0:
        if sum(int(d) for d in str(n)[:num_digits]) >= k:
            return min_digits
        min_digits += 1
        num_digits -= 1
    return -1

