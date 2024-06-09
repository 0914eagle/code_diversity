
def solve(n, m, flights):
    # Sort the flights by departure time
    flights.sort(key=lambda x: x[2])

    # Initialize the minimum frustration and itinerary
    min_frustration = 0
    itinerary = []

    # Loop through each flight
    for flight in flights:
        # If the flight is not the first flight, check if the previous flight has the same departure and arrival country
        if len(itinerary) > 0 and itinerary[-1][1] == flight[1]:
            # If so, remove the previous flight from the itinerary and add the current flight
            itinerary.pop()
            itinerary.append(flight)
        else:
            # If not, add the current flight to the itinerary
            itinerary.append(flight)

        # Calculate the frustration for the current flight
        frustration = (flight[3] - flight[2]) ** 2
        min_frustration += frustration

    # Return the minimum frustration and itinerary
    return min_frustration, itinerary

