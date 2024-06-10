
import math
import sys

def get_expected_damages(N, L, R):
    expected_damages = 0
    for i in range(N):
        for j in range(i+1, N):
            if L[i] > L[j]:
                expected_damages += L[i] - L[j]
            if R[i] < R[j]:
                expected_damages += R[j] - R[i]
    return expected_damages / N ** 2

def main():
    N = int(input())
    L = []
    R = []
    for i in range(N):
        l, r = map(float, input().split())
        L.append(l)
        R.append(r)
    print(get_expected_damages(N, L, R))

if __name__ == '__main__':
    main()

