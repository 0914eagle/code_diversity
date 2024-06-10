
import sys

def get_input():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    return n, k, p

def get_expected_value(p, k):
    expected_value = 0
    for i in range(k):
        expected_value += p[i]
    return expected_value

def get_max_expected_value(n, k, p):
    max_expected_value = 0
    for i in range(n - k + 1):
        expected_value = get_expected_value(p[i:i+k], k)
        if expected_value > max_expected_value:
            max_expected_value = expected_value
    return max_expected_value

def main():
    n, k, p = get_input()
    print(get_max_expected_value(n, k, p))

if __name__ == '__main__':
    main()

