
def solve(n, k):
    count = 0
    num = 0
    while count < k:
        num += 1
        if num % n != 0:
            count += 1
    return num

