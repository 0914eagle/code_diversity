
def get_elegant_numbers(n):
    elegant_numbers = []
    for i in range(2, n+1):
        if gcd(i, get_prime_factors(i)) == 1:
            elegant_numbers.append(i)
    return len(elegant_numbers)

def get_prime_factors(n):
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            prime_factors.append(i)
            n //= i
    if n > 2:
        prime_factors.append(n)
    return prime_factors

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        print(get_elegant_numbers(n))

