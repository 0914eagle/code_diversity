
import sys

def get_sorted_sequences(arr):
    n = len(arr)
    sorted_seqs = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                sorted_seqs += 1
    return sorted_seqs

def get_entirely_unsorted_sequences(arr):
    n = len(arr)
    unsorted_seqs = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] != arr[j]:
                unsorted_seqs += 1
    return unsorted_seqs

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    sorted_seqs = get_sorted_sequences(arr)
    unsorted_seqs = get_entirely_unsorted_sequences(arr)
    print((unsorted_seqs - sorted_seqs) % (10**9 + 9))

if __name__ == '__main__':
    main()

