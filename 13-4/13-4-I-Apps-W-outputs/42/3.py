
def solve(S):
    N = len(S)
    squares = [0] * N
    for i in range(N):
        if S[i] == "L":
            squares[i] += 1
        else:
            squares[i-1] += 1
    return " ".join(str(x) for x in squares)

