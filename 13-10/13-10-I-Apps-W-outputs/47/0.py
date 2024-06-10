
import sys
import math

def get_beauty(arr, k):
    n = len(arr)
    beauty = 0
    for i in range(n - k + 1):
        for j in range(i + 1, n):
            beauty += abs(arr[i] - arr[j])
    return beauty

def get_subsequence_beauty(arr, k):
    n = len(arr)
    beauty = 0
    for i in range(n - k + 1):
        subsequence = arr[i:i+k]
        beauty += get_beauty(subsequence, k)
    return beauty

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(get_subsequence_beauty(arr, k) % 998244353)

if __name__ == '__main__':
    main()

