
def count_good_phone_numbers(n, k, a, b):
    modulo = 10**9 + 7
    count = 0
    for i in range(10**k):
        curr = str(i)
        if len(curr) < k:
            curr = '0' * (k - len(curr)) + curr
        block = [int(curr[j * k:(j + 1) * k]) for j in range(n // k)]
        if all(block[i] % a[i] == 0 for i in range(n // k)) and all(block[i] != b[i] for i in range(n // k)):
            count += 1
    return count % modulo

