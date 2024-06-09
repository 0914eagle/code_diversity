
def solve(S):
    N = len(S)
    counts = [0] * N
    counts[0] = 1
    counts[N-1] = 1
    for i in range(1, N-1):
        if S[i] == "L":
            counts[i-1] += counts[i]
        else:
            counts[i+1] += counts[i]
    return " ".join(str(count) for count in counts)

