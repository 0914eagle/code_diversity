
def solve(S):
    N = len(S)
    children = [0] * N
    children[0] = 1
    children[N-1] = 1
    for i in range(10**100):
        for j in range(N):
            if S[j] == "L":
                children[j-1] += children[j]
            else:
                children[j+1] += children[j]
        children[0] = 0
        children[N-1] = 0
    return " ".join(str(x) for x in children)

