
def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    return divisors

def get_probabilities(divisors, n):
    probabilities = []
    for divisor in divisors:
        probabilities.append(divisors.count(divisor) / len(divisors))
    return probabilities

def get_expected_value(divisors, probabilities, n):
    expected_value = 0
    for i in range(len(divisors)):
        expected_value += divisors[i] * probabilities[i]
    return expected_value

def main():
    n, k = map(int, input().split())
    divisors = get_divisors(n)
    probabilities = get_probabilities(divisors, n)
    expected_value = get_expected_value(divisors, probabilities, n)
    print(int(expected_value % (10**9 + 7)))

if __name__ == '__main__':
    main()

