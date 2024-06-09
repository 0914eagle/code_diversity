
def solve(D, G, *args):
    p_list, c_list = [], []
    for i in range(D):
        p, c = args[i * 2], args[i * 2 + 1]
        p_list.append(p)
        c_list.append(c)
    
    total_score = 0
    num_problems = 0
    for i in range(D):
        while p_list[i] > 0 and total_score + (100 * i + c_list[i]) <= G:
            total_score += 100 * i + c_list[i]
            p_list[i] -= 1
            num_problems += 1
    
    return num_problems

