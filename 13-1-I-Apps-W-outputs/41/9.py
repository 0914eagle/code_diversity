
def solve(n, v, m, queries):
    # Sort the stone costs in non-decreasing order
    v.sort()
    
    # Initialize two arrays to store the sum of the costs and the sum of the cheapest costs
    sum_costs = [0] * (n + 1)
    sum_cheapest_costs = [0] * (n + 1)
    
    # Calculate the sum of the costs and the sum of the cheapest costs for each position
    for i in range(1, n + 1):
        sum_costs[i] = sum_costs[i - 1] + v[i - 1]
        sum_cheapest_costs[i] = sum_cheapest_costs[i - 1] + v[i - 1]
    
    # Iterate over the queries and calculate the answers
    answers = []
    for query in queries:
        type, l, r = query
        if type == 1:
            answers.append(sum_costs[r] - sum_costs[l - 1])
        else:
            answers.append(sum_cheapest_costs[r] - sum_cheapest_costs[l - 1])
    
    return answers

