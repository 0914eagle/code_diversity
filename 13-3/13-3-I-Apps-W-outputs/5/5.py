
def get_problems_solved(n, k):
    total_time = 0
    problems_solved = 0
    for i in range(1, n+1):
        if total_time + 5*i <= k:
            total_time += 5*i
            problems_solved += 1
        else:
            break
    return problems_solved

