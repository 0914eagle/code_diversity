
def solve(b, d, c, l):
    answers = []
    for i in range(1, min(b, d, c) + 1):
        for j in range(1, min(b - i, d, c) + 1):
            for k in range(1, min(b - i - j, d - j, c - j) + 1):
                if i + j + k == l:
                    answers.append([i, j, k])
    if not answers:
        return ["impossible"]
    return [" ".join(map(str, answer)) for answer in sorted(answers)]

