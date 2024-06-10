
import math

def get_expected_damages(N, L, R):
    expected_damages = 0
    for i in range(N):
        for j in range(i+1, N):
            expected_damages += (max(L[i], L[j]) - min(R[i], R[j])) * (R[i] - L[i]) * (R[j] - L[j])
    return expected_damages / (N * (N - 1) / 2)

def main():
    N = int(input())
    L = []
    R = []
    for i in range(N):
        L.append(float(input()))
        R.append(float(input()))
    expected_damages = get_expected_damages(N, L, R)
    print(expected_damages)

if __name__ == '__main__':
    main()

