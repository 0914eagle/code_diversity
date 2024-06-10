
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def smallest_subset_with_gcd_one(n, arr):
    g = arr[0]
    for i in range(1, n):
        g = gcd(g, arr[i])
        if g == 1:
            return i + 1
    return -1

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = smallest_subset_with_gcd_one(n, arr)
    print(result)
