
def solve(b, d, c, l):
    answers = []
    for i in range(1, min(b, d, c) + 1):
        for j in range(1, min(b, d, c) + 1):
            for k in range(1, min(b, d, c) + 1):
                if i + j + k == l and i * b + j * d + k * c == l:
                    answers.append([i, j, k])
    return sorted(answers)

