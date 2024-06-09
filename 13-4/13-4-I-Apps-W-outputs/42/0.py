
def solve(S):
    N = len(S)
    counts = [0] * N
    counts[0] = 1
    counts[N-1] = 1
    for i in range(10**100):
        for j in range(N):
            if S[j] == "L":
                counts[j-1] += counts[j]
            else:
                counts[j+1] += counts[j]
        counts[0] = 0
        counts[N-1] = 0
    return " ".join(map(str, counts))

