
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_divisors(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 1
    return count * 2 - 1

def solve(n):
    prime_count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            prime_count += 1
    return prime_count

if __name__ == '__main__':
    n = int(input())
    print(solve(n))

