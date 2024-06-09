
import sys
import math

def f1(a, b):
    # Calculate the sum of the products of a and b
    sum_ab = 0
    for i in range(len(a)):
        sum_ab += a[i] * b[i]
    
    # Calculate the sum of the products of a and its reversed version
    sum_ab_rev = 0
    for i in range(len(a)):
        sum_ab_rev += a[i] * b[len(a) - i - 1]
    
    # Return the minimum of the two sums
    if sum_ab < sum_ab_rev:
        return sum_ab
    else:
        return sum_ab_rev

def f2(a, b):
    # Calculate the sum of the products of a and b
    sum_ab = 0
    for i in range(len(a)):
        sum_ab += a[i] * b[i]
    
    # Calculate the sum of the products of a and its sorted version
    sum_ab_sorted = 0
    b_sorted = sorted(b)
    for i in range(len(a)):
        sum_ab_sorted += a[i] * b_sorted[i]
    
    # Return the minimum of the two sums
    if sum_ab < sum_ab_sorted:
        return sum_ab
    else:
        return sum_ab_sorted

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(min(f1(a, b), f2(a, b)) % 998244353)

