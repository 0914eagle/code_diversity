
def solve(n, v, m, questions):
    # Step 1: Sort the stone costs in non-decreasing order
    v_sorted = sorted(v)
    
    # Step 2: Find the cost of the i-th cheapest stone
    u = [0] * (n + 1)
    for i in range(n):
        u[i + 1] = u[i] + v_sorted[i]
    
    # Step 3: Answer the questions
    answers = []
    for question in questions:
        type, l, r = question
        if type == 1:
            answers.append(u[r] - u[l - 1])
        else:
            answers.append(v_sorted[r - 1] - v_sorted[l - 2])
    
    return answers

