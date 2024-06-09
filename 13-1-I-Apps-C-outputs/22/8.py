
def solve(n, m, k, flights):
    # Sort the flights by their departure day
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

            # Find the flight that takes the city to Metropolis and add its cost to the total cost
            for flight in graph[city]:
                if flight[0] == 0:
                    cost += flight[2]
                    break

            # Find the flight that takes Metropolis to the next city and add its cost to the total cost
            for flight in graph[0]:
                if flight[0] == next_city:
                    cost += flight[2]
                    break

        # If the total cost is less than or equal to the minimum cost, update the minimum cost
        if cost <= min_cost:
            min_cost = cost

    # Return the minimum cost
    return min_cost if min_cost != float("inf") else -1

