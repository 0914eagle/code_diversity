
def solve(c_one, c_two, c_three, c_four, n_buses, n_trolleys, bus_rides, trolley_rides):
    # Calculate the total cost of each type of ticket
    cost_one = c_one * sum(bus_rides) + c_one * sum(trolley_rides)
    cost_two = c_two * (sum(bus_rides) + sum(trolley_rides))
    cost_three = c_three * (n_buses + n_trolleys)
    cost_four = c_four

    # Return the minimum cost
    return min(cost_one, cost_two, cost_three, cost_four)

