
import math
import sys

def get_expected_value(p):
    return sum(p) / len(p)

def get_max_expected_value(p, k):
    if k == 1:
        return get_expected_value(p)
    
    max_value = 0
    for i in range(len(p) - k + 1):
        max_value = max(max_value, get_expected_value(p[i:i+k]))
    
    return max_value

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    
    print(get_max_expected_value(p, k))

if __name__ == '__main__':
    main()

