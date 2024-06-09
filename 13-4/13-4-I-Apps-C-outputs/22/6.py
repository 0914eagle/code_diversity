
def solve(N, L_i, R_i):
    expected_damages = 0
    for i in range(N):
        for j in range(i+1, N):
            if L_i[j] > L_i[i]:
                expected_damages += R_i[i] - L_i[i]
            if R_i[j] < R_i[i]:
                expected_damages += R_i[i] - L_i[i]
    return expected_damages / N ** 2

