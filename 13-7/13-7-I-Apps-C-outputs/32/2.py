
import sys

def get_subsequences(arr):
    subsequences = []
    for i in range(len(arr)):
        for subsequence in get_subsequences(arr[i+1:]):
            subsequences.append([arr[i]] + subsequence)
    if not arr:
        subsequences.append([])
    return subsequences

def get_lexicographically_sorted_subsequences(arr):
    subsequences = get_subsequences(arr)
    return sorted(subsequences, key=lambda x: (x[0], len(x)))

def get_hash(arr, b, m):
    hash_value = 0
    for i in range(len(arr)):
        hash_value = (hash_value * b + arr[i]) % m
    return hash_value

def main():
    n, k, b, m = map(int, input().split())
    arr = list(map(int, input().split()))
    subsequences = get_lexicographically_sorted_subsequences(arr)
    for i in range(k):
        print(get_hash(subsequences[i], b, m))

if __name__ == '__main__':
    main()

