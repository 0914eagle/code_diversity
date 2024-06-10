
import sys
import math

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def is_sorted(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                return False
    return True

def get_unsorted_sequences(a):
    sequences = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            sequences += 1
    return sequences

def main():
    n, a = get_input()
    print(get_unsorted_sequences(a) % (10**9 + 9))

if __name__ == '__main__':
    main()

