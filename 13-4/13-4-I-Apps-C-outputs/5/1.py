
def solve(n, d, schedule, m, fares):
    # Initialize a dictionary to store the minimum cost to reach each city
    min_cost = {city: float('inf') for city in range(1, n + 1)}
    min_cost[schedule[0]] = 0

    # Loop through each city in the schedule
    for i in range(d):
        current_city = schedule[i]
        next_city = schedule[i + 1]

        # Loop through each airfare
        for fare in fares:
            s, d, t, p = fare

            # Check if the airfare is valid for the current city
            if s == current_city and d == next_city:
                # If the airfare is a one-way ticket, add the cost to the minimum cost
                if t == 'O':
                    min_cost[next_city] = min(min_cost[next_city], min_cost[current_city] + p)
                # If the airfare is a round-trip ticket, add the cost to the minimum cost if it's the first segment of the ticket
                elif t == 'R' and min_cost[current_city] + p < min_cost[next_city]:
                    min_cost[next_city] = min_cost[current_city] + p

    # Return the minimum cost to reach the last city in the schedule
    return min_cost[schedule[-1]]

