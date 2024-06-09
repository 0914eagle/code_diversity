
def solve(b, d, c, l):
    answers = []
    for i in range(1, 101):
        for j in range(1, 101):
            for k in range(1, 101):
                if i + j + k == l and i * b + j * d + k * c == 14:
                    answers.append([i, j, k])
    return sorted(answers)

