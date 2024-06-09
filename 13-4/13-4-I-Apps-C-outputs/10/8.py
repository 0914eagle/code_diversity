
import sys

def solve(N, S):
    mod = 1000000007
    count = 0
    for i in range(N):
        if S[i] == "A":
            count += (N-i) * (N-i-1) // 2
        elif S[i] == "B":
            count += (N-i) * (N-i-1) // 2
        else:
            count += (N-i) * (N-i-1) // 2
    return count % mod

if __name__ == "__main__":
    N = int(input())
    S = input()
    print(solve(N, S))

