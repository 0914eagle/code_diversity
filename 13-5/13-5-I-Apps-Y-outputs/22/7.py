
import sys
import math

def get_min_sum(a, b):
    n = len(a)
    # Calculate the sum of all possible pairs of elements in a and b
    all_pairs_sum = 0
    for i in range(n):
        for j in range(i+1, n):
            all_pairs_sum += a[i] * b[j] + a[j] * b[i]
    
    # Initialize the minimum sum to the sum of all possible pairs
    min_sum = all_pairs_sum
    
    # Iterate through all possible permutations of b
    for perm in permutations(b):
        # Calculate the sum of pairs for the current permutation of b
        curr_sum = 0
        for i in range(n):
            for j in range(i+1, n):
                curr_sum += a[i] * perm[j] + a[j] * perm[i]
        # Update the minimum sum if the current sum is smaller
        if curr_sum < min_sum:
            min_sum = curr_sum
    
    return min_sum % 998244353

def permutations(arr):
    if len(arr) <= 1:
        yield arr
    else:
        for i in range(len(arr)):
            for p in permutations(arr[:i] + arr[i+1:]):
                yield [arr[i]] + p

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_min_sum(a, b))

