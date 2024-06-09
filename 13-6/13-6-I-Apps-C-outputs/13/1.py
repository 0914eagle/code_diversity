
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

def count_unsorted_sequences(a):
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if is_sorted([a[i], a[j], a[k]]):
                    count += 1
    return count % (10**9 + 9)

def main():
    n, a = get_input()
    print(count_unsorted_sequences(a))

if __name__ == '__main__':
    main()

