
import math

def get_expected_damages(N, L, R):
    expected_damages = 0
    for i in range(N):
        for j in range(i+1, N):
            if L[i] < L[j] and R[i] < R[j]:
                expected_damages += R[j] - L[j]
            elif L[i] < L[j] and R[i] > R[j]:
                expected_damages += R[j] - L[j] + R[i] - L[i]
            elif L[i] > L[j] and R[i] < R[j]:
                expected_damages += R[i] - L[i] + R[j] - L[j]
            else:
                expected_damages += R[i] - L[i] + R[j] - L[j]
    return expected_damages / N**2

def main():
    N = int(input())
    L = []
    R = []
    for i in range(N):
        L_i, R_i = map(float, input().split())
        L.append(L_i)
        R.append(R_i)
    print(get_expected_damages(N, L, R))

if __name__ == '__main__':
    main()

