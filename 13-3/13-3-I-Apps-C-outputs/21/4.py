
def find_pattern(S):
    N = len(S)
    for i in range(N-3):
        for j in range(i+1, N-2):
            if S[i] == S[j] and S[i+1] == S[j+1] and S[i+2] == S[j+2]:
                return S[i], S[j]
    return -1

