
def solve(n, k):
    count = 0
    num = 1
    while count < k:
        if num % n != 0:
            count += 1
        num += 1
    return num - 1

