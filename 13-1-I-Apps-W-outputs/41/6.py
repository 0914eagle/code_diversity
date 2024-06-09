
def solve(n, v, m, questions):
    # Calculate the cost of the i-th cheapest stone
    u = [0] * (n + 1)
    for i in range(n):
        u[i + 1] = u[i] + v[i]
    
    # Answer the questions
    answers = []
    for type, l, r in questions:
        if type == 1:
            answers.append(u[r] - u[l - 1])
        else:
            answers.append(u[r] - u[l - 1] + v[l - 1])
    
    return answers

