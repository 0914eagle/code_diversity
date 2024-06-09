
def count_xorangles(n):
    count = 0
    for a in range(1, n+1):
        for b in range(a+1, n+1):
            c = n - a - b
            if a ^ b ^ c == 0:
                count += 1
    return count

