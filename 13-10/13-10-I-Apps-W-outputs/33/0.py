
import sys

def get_input():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    return n, k, a

def solve(n, k, a):
    pairs = [(a[i] * a[j], i, j) for i in range(n) for j in range(i+1, n)]
    pairs.sort()
    return pairs[k-1][0]

def main():
    n, k, a = get_input()
    print(solve(n, k, a))

if __name__ == '__main__':
    main()

