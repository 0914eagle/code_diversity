
def solve(n, m, k, flights):
    # Sort the flights by departure day
    flights.sort(key=lambda x: x[0])

    # Create a graph with n + 1 nodes (0 for Metropolis and 1 to n for the cities)
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph based on the flights
    for flight in flights:
        graph[flight[1]].append((flight[2], flight[3], flight[4]))
        graph[flight[2]].append((flight[1], flight[3], flight[4]))

    # Initialize the minimum cost to gather everybody in Metropolis and send them back to their home cities
    min_cost = float("inf")

    # Iterate over all possible subsets of cities to gather everybody in Metropolis
    for cities in itertools.combinations(range(1, n + 1), n):
        # Initialize the cost of the current subset of cities
        cost = 0

        # Iterate over all cities in the current subset
        for i in range(len(cities)):
            # Get the city and the next city in the subset
            city = cities[i]
            next_city = cities[(i + 1) % len(cities)]

            # Find the cheapest flight from the current city to the next city
            cheapest_flight = float("inf")
            for flight in graph[city]:
                if flight[1] == next_city and flight[0] > 0 and flight[0] <= k:
                    cheapest_flight = min(cheapest_flight, flight[2])

            # If there is no flight from the current city to the next city, the subset is not valid
            if cheapest_flight == float("inf"):
                break

            # Add the cost of the cheapest flight to the total cost
            cost += cheapest_flight

        # If the current subset is valid, check if the total cost is the minimum cost so far
        else:
            min_cost = min(min_cost, cost)

    # Return the minimum cost
    return -1 if min_cost == float("inf") else min_cost

