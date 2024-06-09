
def solve(S):
    x = 0
    for i in S:
        if i == "I":
            x += 1
        else:
            x -= 1
    return max(x, 0)

