
def solve(c1, c2, c3, c4, n, m, a, b):
    # Calculate the total cost of using each type of ticket
    cost1 = c1 * sum(a)
    cost2 = c2 * n
    cost3 = c3 * (n + m)
    cost4 = c4

    # Return the minimum of the four costs
    return min(cost1, cost2, cost3, cost4)

