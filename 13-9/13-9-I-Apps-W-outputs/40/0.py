
def solve(c_one, c_two, c_three, c_four, n, m, buses, trolleys):
    # Calculate the cost of each type of ticket
    cost_one = c_one * sum(buses)
    cost_two = c_two * (n + m)
    cost_three = c_three * n * m
    cost_four = c_four * n * m

    # Return the minimum cost
    return min(cost_one, cost_two, cost_three, cost_four)

