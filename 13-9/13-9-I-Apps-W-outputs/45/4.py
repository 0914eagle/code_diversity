
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
    probabilities = [1 / len(divisors)] * len(divisors)
    expected_value = 0
    for i in range(k):
        expected_value += sum(probabilities)
        probabilities = [probabilities[i] / len(divisors) for i in range(len(divisors))]
    return expected_value

def get_result(n, k):
    expected_value = get_expected_value(n, k)
    gcd = math.gcd(expected_value, 1000000007)
    return int((expected_value // gcd) * pow(gcd, -1, 1000000007))

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(get_result(n, k))

