
def get_expected_damages(N, L, R):
    expected_damages = 0
    for i in range(N):
        for j in range(i+1, N):
            expected_damages += max(0, R[i] - L[j]) + max(0, R[j] - L[i])
    return expected_damages / N ** 2

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

