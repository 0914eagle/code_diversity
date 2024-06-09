
def solve(n, m, flights):
    # Sort the flights by departure time
    flights.sort(key=lambda x: x[2])

    # Initialize the minimum sum of frustration and the itinerary
    min_frustration = 0
    itinerary = []

    # Loop through each flight and check if it can be added to the itinerary
    for flight in flights:
        # Check if the flight can be added to the itinerary
        if flight[1] == itinerary[-1][0] and flight[2] >= itinerary[-1][1]:
            # Add the flight to the itinerary and calculate the frustration
            itinerary.append(flight)
            min_frustration += (flight[2] - flight[1]) ** 2

    # Return the minimum sum of frustration and the itinerary
    return min_frustration, itinerary

