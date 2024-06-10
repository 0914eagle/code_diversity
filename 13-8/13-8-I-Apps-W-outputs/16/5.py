
def get_prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

def is_elegant(n):
    factors = get_prime_factors(n)
    gcd = 1
    for f in factors:
        gcd = gcd * f
    return gcd == 1

def count_elegant_numbers(n):
    count = 0
    for i in range(2, n + 1):
        if is_elegant(i):
            count += 1
    return count

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(count_elegant_numbers(n))

if __name__ == '__main__':
    main()

