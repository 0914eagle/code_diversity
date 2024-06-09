
def solve(D, G, *problems):
    total_score = 0
    num_problems = 0
    for p, c in problems:
        total_score += p
        num_problems += 1
        if total_score >= G:
            break
    return num_problems

