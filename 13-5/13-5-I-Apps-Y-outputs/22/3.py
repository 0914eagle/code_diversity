
import sys
import math

def f1(a, b):
    # Calculate the sum of the products of elements in a and b
    sum = 0
    for i in range(len(a)):
        sum += a[i] * b[i]
    return sum

def f2(a, b):
    # Calculate the sum of the products of elements in a and b, but with the elements of b rearranged
    sum = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            sum += a[i] * b[j]
    return sum

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(f2(a, b) % 998244353)

