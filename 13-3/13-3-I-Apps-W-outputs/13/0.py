
def count_good_phone_numbers(n, k, a, b):
    modulo = 10**9 + 7
    count = 0
    for i in range(10**k):
        curr = str(i)
        if len(curr) < k:
            curr = '0' * (k - len(curr)) + curr
        block = [int(curr[j]) for j in range(k)]
        if block[0] != b[0]:
            count += 1
        if all(block[j] % a[j] == 0 for j in range(1, k)):
            count += 1
    return count % modulo

