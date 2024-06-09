
def solve(b):
    n = len(b) // 2
    a = [0] * n
    prime_numbers = [2]
    for i in range(3, 2750132, 2):
        if is_prime(i):
            prime_numbers.append(i)
    for i in range(n):
        if b[i] in prime_numbers:
            a[i] = b[i]
        else:
            for j in range(i+1, n):
                if b[j] % b[i] == 0 and b[j] != b[i]:
                    a[i] = b[j]
                    break
    return a

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

