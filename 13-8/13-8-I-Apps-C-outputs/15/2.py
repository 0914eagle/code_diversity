
import sys

def get_unsorted_sequences(sequence):
    n = len(sequence)
    unsorted_sequences = 0
    for i in range(n):
        for j in range(i+1, n):
            if sequence[i] > sequence[j]:
                unsorted_sequences += 1
    return unsorted_sequences

def get_entirely_unsorted_sequences(sequence):
    n = len(sequence)
    entirely_unsorted_sequences = 0
    for i in range(n):
        for j in range(i+1, n):
            if sequence[i] > sequence[j]:
                entirely_unsorted_sequences += 1
    return entirely_unsorted_sequences

def main():
    n = int(input())
    sequence = list(map(int, input().split()))
    print(get_unsorted_sequences(sequence) % (10**9 + 9))

if __name__ == '__main__':
    main()

