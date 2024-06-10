
import math

def get_probabilities(p):
    probabilities = []
    for i in range(len(p)):
        probabilities.append(p[i] / sum(p))
    return probabilities

def get_expected_value(p, k):
    expected_value = 0
    for i in range(len(p) - k + 1):
        expected_value += p[i] * sum(range(i + 1, i + k + 1))
    return expected_value

def get_maximum_expected_value(p, k):
    probabilities = get_probabilities(p)
    maximum_expected_value = 0
    for i in range(len(p) - k + 1):
        expected_value = get_expected_value(probabilities[i:i+k], k)
        if expected_value > maximum_expected_value:
            maximum_expected_value = expected_value
    return maximum_expected_value

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    print(get_maximum_expected_value(p, k))

if __name__ == '__main__':
    main()

