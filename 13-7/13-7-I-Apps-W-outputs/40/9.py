
def solve(s):
    n = len(s)
    score = 0
    for i in range(n):
        if s[i] == "g":
            if i % 2 == 0:
                score += 1
            else:
                score -= 1
        else:
            if i % 2 == 0:
                score -= 1
            else:
                score += 1
    return score

