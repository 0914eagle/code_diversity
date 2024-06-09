
import sys

def solve(N, A):
    mod = 1000000007
    sum = 0
    for i in range(N-1):
        for j in range(i+1, N):
            sum = (sum + (A[i] * A[j]) % mod) % mod
    return sum

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))

