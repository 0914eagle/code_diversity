
import math

def get_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    divisors.sort()
    return divisors

def get_expected_value(n, k):
    divisors = get_divisors(n)
    p = 1
    q = 1
    for i in range(k):
        p *= divisors[i % len(divisors)]
        q *= n
    return p * pow(q, -1, 1000000007) % 1000000007

def main():
    n, k = map(int, input().split())
    print(get_expected_value(n, k))

if __name__ == '__main__':
    main()

