
def solve(n, scores):
    scores = sorted(scores, reverse=True)
    count = 0
    for i in range(n):
        if scores[i] == 0:
            break
        count += n - i
    return count

