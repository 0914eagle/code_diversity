
def is_elegant(n):
    factors = []
    while n > 1:
        p = next_prime(n)
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        factors.append(exponent)
    return len(set(factors)) == len(factors)

def next_prime(n):
    if n == 2:
        return 3
    else:
        for i in range(n + 1, n * 2):
            if all(i % p != 0 for p in range(2, int(n ** 0.5) + 1)):
                return i

def count_elegant(n):
    count = 0
    for i in range(2, n + 1):
        if is_elegant(i):
            count += 1
    return count

if __name__ == '__main__':
    num_test_cases = int(input())
    for i in range(num_test_cases):
        n = int(input())
        print(count_elegant(n))

