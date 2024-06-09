
def solve(S):
    N = len(S)
    count = 0
    for i in range(N-1):
        if S[i] == '0' and S[i+1] == '1':
            count += 1
    return count

