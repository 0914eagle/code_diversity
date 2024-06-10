
import math

def get_probability(p, k, n):
    probability = 1
    for i in range(k):
        probability *= p[i] / n
    return probability

def get_expected_value(p, k, n):
    expected_value = 0
    for i in range(k):
        expected_value += (i + 1) * p[i] / n
    return expected_value

def get_max_expected_value(p, k, n):
    max_expected_value = 0
    for i in range(n - k + 1):
        probability = get_probability(p, k, n)
        expected_value = get_expected_value(p, k, n)
        if expected_value > max_expected_value:
            max_expected_value = expected_value
    return max_expected_value

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    print(get_max_expected_value(p, k, n))

if __name__ == '__main__':
    main()

