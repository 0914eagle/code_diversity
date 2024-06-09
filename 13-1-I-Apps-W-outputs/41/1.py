
def solve(n, v, m, queries):
    # Sort the stone costs in non-decreasing order
    v.sort()
    
    # Initialize two arrays to store the sums
    sum_v = [0] * (n + 1)
    sum_u = [0] * (n + 1)
    
    # Calculate the sums
    for i in range(1, n + 1):
        sum_v[i] = sum_v[i - 1] + v[i - 1]
        sum_u[i] = sum_u[i - 1] + v[n - i]
    
    # Iterate through the queries and calculate the answers
    answers = []
    for query in queries:
        if query[0] == 1:
            answers.append(sum_v[query[1]:query[2] + 1])
        else:
            answers.append(sum_u[query[1]:query[2] + 1])
    
    return answers

