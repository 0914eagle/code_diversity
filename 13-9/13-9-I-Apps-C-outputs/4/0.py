
import sys

def get_entirely_unsorted_sequences(arr):
    n = len(arr)
    count = 0
    for i in range(1, n + 1):
        for perm in permutations(arr, i):
            if not is_sorted(perm):
                count += 1
    return count % (10**9 + 9)

def is_sorted(arr):
    n = len(arr)
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def permutations(arr, k):
    if k == 0:
        return [[]]
    else:
        permutations_list = []
        for i in range(len(arr)):
            for perm in permutations(arr[:i] + arr[i + 1:], k - 1):
                permutations_list.append([arr[i]] + perm)
        return permutations_list

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_entirely_unsorted_sequences(arr))

