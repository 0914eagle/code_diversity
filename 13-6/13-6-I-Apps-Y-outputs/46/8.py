
def solve(D, G, *problems):
    total_score = 0
    problems_solved = 0

    for i in range(1, D+1):
        p_i, c_i = problems[i-1]
        problems_solved += p_i
        total_score += p_i * 100 * i

    if total_score >= G:
        return problems_solved

    for i in range(D, 0, -1):
        p_i, c_i = problems[i-1]
        if total_score + c_i >= G:
            return problems_solved + p_i
        total_score += c_i

    return problems_solved

