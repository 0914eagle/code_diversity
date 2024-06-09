
import sys
import math

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return n, a, b

def f(l, r, a, b):
    return sum(a[l:r+1] * b[l:r+1])

def solve(n, a, b):
    # Calculate the sum of all possible pairs of elements
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            pairs.append((i, j, f(i, j, a, b)))
    
    # Sort the pairs in descending order of their sum
    pairs.sort(key=lambda x: x[2], reverse=True)
    
    # Create a new array with the elements of b in the sorted order
    new_b = [0] * n
    for i, j, _ in pairs:
        new_b[i] = b[i]
        new_b[j] = b[j]
    
    # Calculate the final sum
    sum = 0
    for i in range(n):
        sum += a[i] * new_b[i]
    
    return sum % 998244353

if __name__ == '__main__':
    n, a, b = get_input()
    print(solve(n, a, b))

