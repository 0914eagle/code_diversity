
def solve(n):
    for x in range(1, n+1):
        k = 1
        sum = x
        while sum < n:
            k += 1
            sum += 2**(k-1) * x
            if sum > n:
                break
        if sum == n:
            return x
    return -1

