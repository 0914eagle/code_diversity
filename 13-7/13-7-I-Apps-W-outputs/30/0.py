
import sys

def solve(n, s):
    permutations = 0
    for i in range(1, n + 1):
        permutations += 1
        s = apply_permutation(s, i)
        if is_good_sequence(s):
            permutations -= 1
    return permutations % 998244353

def apply_permutation(s, permutation):
    new_s = []
    for i in range(len(s)):
        new_s.append(s[permutation - 1][i])
    return new_s

def is_good_sequence(s):
    first_elements, second_elements = [], []
    for pair in s:
        first_elements.append(pair[0])
        second_elements.append(pair[1])
    return not (is_sorted(first_elements) or is_sorted(second_elements))

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return True
    return False

n = int(input())
s = []
for i in range(n):
    a, b = map(int, input().split())
    s.append((a, b))
print(solve(n, s))

