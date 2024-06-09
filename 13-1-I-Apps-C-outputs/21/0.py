
def solve(n, m, flights):
    # Sort the flights by departure time
    flights.sort(key=lambda x: x[2])

    # Initialize the minimum frustration and itinerary
    min_frustration = 0
    itinerary = []

    # Loop through each flight and calculate the frustration
    for flight in flights:
        frustration = (flight[2] - flight[1]) ** 2
        min_frustration += frustration
        itinerary.append(flight)

    # Return the minimum frustration and itinerary
    return min_frustration, itinerary

