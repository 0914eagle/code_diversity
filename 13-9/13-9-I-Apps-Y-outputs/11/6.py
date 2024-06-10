
import sys
import itertools

def generate_monotonic_renumerations(a):
    n = len(a)
    b = [0] * n
    for i in range(1, n):
        if a[i] != a[i-1]:
            b[i] = b[i-1] + 1
        else:
            b[i] = b[i-1]
    return b

def count_monotonic_renumerations(a):
    n = len(a)
    count = 0
    for perm in itertools.permutations(range(n)):
        b = generate_monotonic_renumerations(a[perm])
        if b == [0] * n:
            count += 1
    return count

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(count_monotonic_renumerations(a) % 998244353)

if __name__ == '__main__':
    main()

