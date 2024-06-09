
def solve(c_1, c_2, c_3, c_4, n, m, a, b):
    # Calculate the total cost of using each type of ticket
    cost_1 = c_1 * sum(a)
    cost_2 = c_2 * sum(a)
    cost_3 = c_3 * (n + m)
    cost_4 = c_4

    # Return the minimum cost
    return min(cost_1, cost_2, cost_3, cost_4)

