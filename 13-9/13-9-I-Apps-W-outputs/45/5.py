
def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    return divisors

def get_expected_value(n, k):
    divisors = get_divisors(n)
    total = sum(divisors)
    return (total * k) // len(divisors)

def main():
    n, k = map(int, input().split())
    expected_value = get_expected_value(n, k)
    print(expected_value)

if __name__ == '__main__':
    main()

