
import sys
import math

def get_subsequences(arr, k):
    n = len(arr)
    subsequences = []
    for i in range(n-k+1):
        subsequences.append(arr[i:i+k])
    return subsequences

def get_beauty(arr):
    n = len(arr)
    beauty = 0
    for i in range(n-1):
        for j in range(i+1, n):
            beauty += abs(arr[i] - arr[j])
    return beauty

def get_sum_of_beauty(arr, k):
    subsequences = get_subsequences(arr, k)
    sum_of_beauty = 0
    for subsequence in subsequences:
        sum_of_beauty += get_beauty(subsequence)
    return sum_of_beauty

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(get_sum_of_beauty(arr, k) % 998244353)

if __name__ == '__main__':
    main()

