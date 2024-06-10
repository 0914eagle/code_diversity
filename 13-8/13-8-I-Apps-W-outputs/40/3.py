
import math
import sys

def get_input():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    return n, k, p

def get_expected_value(p, k):
    expected_value = 0
    for i in range(k):
        expected_value += p[i] * (i + 1)
    return expected_value

def get_max_expected_value(p, k):
    max_expected_value = 0
    for i in range(len(p) - k + 1):
        max_expected_value = max(max_expected_value, get_expected_value(p[i:i+k], k))
    return max_expected_value

def main():
    n, k, p = get_input()
    print(get_max_expected_value(p, k))

if __name__ == '__main__':
    main()

