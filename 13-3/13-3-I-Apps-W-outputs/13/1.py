
def f1(n, k, a, b):
    mod = 10**9 + 7
    count = 0
    for i in range(10**n):
        num = str(i)
        block = [int(num[j:j+k]) for j in range(0, n, k)]
        if block[0] != b[0]:
            count += 1
        if all(block[i] % a[i] == 0 for i in range(1, len(block))):
            count += 1
    return count % mod

