
import math

def get_expected_payment(N, L, R):
    expected_payment = 0
    for i in range(N):
        for j in range(i+1, N):
            if L[i] > L[j] and R[i] > R[j]:
                expected_payment += R[i] - L[i] + 1
            elif L[i] > L[j] and R[i] < R[j]:
                expected_payment += R[i] - L[i] + 1 + R[j] - L[j]
            elif L[i] < L[j] and R[i] > R[j]:
                expected_payment += R[i] - L[i] + 1 + R[j] - L[j]
            else:
                expected_payment += R[i] - L[i] + 1 + R[j] - L[j] + (R[j] - L[j] + 1)
    return expected_payment / (N * (N - 1) / 2)

def main():
    N = int(input())
    L = []
    R = []
    for i in range(N):
        L_i, R_i = map(float, input().split())
        L.append(L_i)
        R.append(R_i)
    print(get_expected_payment(N, L, R))

if __name__ == '__main__':
    main()

