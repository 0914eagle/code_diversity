
def max_x(S):
    x = 0
    for s in S:
        if s == "I":
            x += 1
        else:
            x -= 1
    return max(x, 0)

