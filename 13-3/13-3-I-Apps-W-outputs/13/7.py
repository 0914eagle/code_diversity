
def count_good_phone_numbers(n, k, a, b):
    modulo = 10**9 + 7
    count = 0
    for i in range(10**k):
        current = str(i)
        if len(current) < k:
            current = '0' * (k - len(current)) + current
        block = [int(current[j * k:(j + 1) * k]) for j in range(n // k)]
        if all(block[i] % a[i] == 0 for i in range(n // k)) and not any(block[i] // a[i] == b[i] for i in range(n // k)):
            count += 1
    return count % modulo

