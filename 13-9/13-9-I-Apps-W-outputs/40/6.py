
def get_min_cost(c_one, c_two, c_three, c_four, n_buses, n_trolleys, bus_rides, trolley_rides):
    # Calculate the cost of each type of ticket
    cost_one = c_one * sum(bus_rides) + c_one * sum(trolley_rides)
    cost_two = c_two * (max(bus_rides) + max(trolley_rides))
    cost_three = c_three * n_buses + c_three * n_trolleys
    cost_four = c_four

    # Return the minimum cost
    return min(cost_one, cost_two, cost_three, cost_four)

