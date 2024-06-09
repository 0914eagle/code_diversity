
def solve_flight_problem(n, flights):
    # Initialize a graph with the given number of cities
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the given flights
    for flight in flights:
        graph[flight[0] - 1].append(flight[1] - 1)
        graph[flight[1] - 1].append(flight[0] - 1)

    # Find the city with the maximum number of flights
    max_city = 0
    max_flights = 0
    for i in range(n):
        flights_from_i = len(graph[i])
        if flights_from_i > max_flights:
            max_flights = flights_from_i
            max_city = i

    # Cancel the flight from the city with the maximum number of flights
    flight_to_cancel = graph[max_city].pop()

    # Add a new flight from the city with the maximum number of flights to any other city
    new_flight = [max_city, graph[max_city][0]]

    # Return the minimum number of flights needed, the city to cancel the flight from, and the city to add the new flight to
    return len(graph[0]) - 1, flight_to_cancel + 1, new_flight[0] + 1, new_flight[1] + 1

