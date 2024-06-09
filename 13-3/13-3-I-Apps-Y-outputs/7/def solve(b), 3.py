
def solve(b):
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
            for j in range(i+1, n):
                if b[i] % b[j] == 0 and b[j] != b[i]:
                    a[i] = b[j]
                    break
    return a

