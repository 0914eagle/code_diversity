
def recover_array(b):
    n = len(b) // 2
    a = [0] * n
    prime_numbers = [2]
    for i in range(3, 2750132, 2):
        if all(i % p != 0 for p in prime_numbers):
            prime_numbers.append(i)
    for i in range(n):
        if b[i] in prime_numbers:
            a[i] = prime_numbers.index(b[i]) + 2
        else:
            a[i] = b[i + n] // b[i]
    return a

