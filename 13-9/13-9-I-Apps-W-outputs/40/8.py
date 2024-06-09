
def solve(c_1, c_2, c_3, c_4, n, m, buses, trolleys):
    # Calculate the cost of each ticket type
    ticket_1_cost = c_1 * sum(buses)
    ticket_2_cost = c_2 * sum(buses)
    ticket_3_cost = c_3 * (n + m)
    ticket_4_cost = c_4

    # Find the minimum cost
    return min(ticket_1_cost, ticket_2_cost, ticket_3_cost, ticket_4_cost)

