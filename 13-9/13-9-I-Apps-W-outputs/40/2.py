
def solve(c1, c2, c3, c4, n, m, a, b):
    # Calculate the total cost of using each type of ticket
    cost1 = c1 * sum(a)
    cost2 = c2 * sum(a) + c2 * sum(b)
    cost3 = c3 * n
    cost4 = c4 * n + c4 * m

    # Return the minimum cost
    return min(cost1, cost2, cost3, cost4)

