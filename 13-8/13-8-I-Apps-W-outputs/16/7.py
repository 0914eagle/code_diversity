
def get_prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def get_gcd(k_list):
    gcd = 1
    for k in k_list:
        gcd = max(gcd, k)
    return gcd

def count_elegant_numbers(n):
    count = 0
    for i in range(2, n+1):
        factors = get_prime_factors(i)
        k_list = [f for f in factors if f != 2 and f != 3 and f != 5]
        if get_gcd(k_list) == 1:
            count += 1
    return count

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(count_elegant_numbers(n))

if __name__ == '__main__':
    main()

