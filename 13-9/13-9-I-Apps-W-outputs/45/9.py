
def get_coprime_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    return divisors

def get_expected_value(n, k):
    divisors = get_coprime_divisors(n)
    P = 1
    Q = 1
    for _ in range(k):
        divisor = divisors[int(len(divisors) * random.random())]
        P *= divisor
        Q *= n // divisor
    return P * pow(Q, -1, 1000000007) % 1000000007

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(get_expected_value(n, k))

