
import sys
import math

def f1(a, b):
    # Calculate the sum of the products of the elements of a and b
    sum_ab = 0
    for i in range(len(a)):
        sum_ab += a[i] * b[i]
    return sum_ab

def f2(a, b):
    # Calculate the sum of the products of the elements of a and b, but with the elements of b rearranged
    sum_ab_rearranged = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            sum_ab_rearranged += a[i] * b[j]
    return sum_ab_rearranged

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(f2(a, b) % 998244353)

