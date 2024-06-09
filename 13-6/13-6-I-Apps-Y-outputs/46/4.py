
def solve(D, G, *args):
    problems = []
    for i in range(D):
        problems.append((args[i*2], args[i*2+1]))
    
    problems.sort(key=lambda x: x[1], reverse=True)
    
    total_score = 0
    num_problems = 0
    for p in problems:
        total_score += p[0]
        num_problems += 1
        if total_score >= G:
            break
    
    return num_problems

