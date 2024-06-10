
def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    return sorted(divisors, reverse=True)

def get_expected_value(n, k):
    divisors = get_divisors(n)
    probabilities = [1 / len(divisors)] * len(divisors)
    expected_value = 0
    for i in range(k):
        index = random.randint(0, len(divisors) - 1)
        expected_value += divisors[index] * probabilities[index]
    return expected_value

def main():
    n, k = map(int, input().split())
    print(int(get_expected_value(n, k) % 1000000007))

if __name__ == '__main__':
    main()

