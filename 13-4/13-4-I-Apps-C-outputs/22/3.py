
def expected_damages(N, L, R):
    total_damages = 0
    for i in range(N):
        for j in range(i+1, N):
            if L[i] < L[j]:
                total_damages += R[j] - R[i]
            elif L[i] > L[j]:
                total_damages += R[i] - R[j]
    return total_damages / N ** 2

