
def min_cost_to_travel_to_rightmost_gas_station(n, g, distances, costs):
    # Sort the gas stations by distance in ascending order
    sorted_gas_stations = sorted(zip(distances, costs), key=lambda x: x[0])

    # Initialize the current gas station and the total distance traveled
    current_gas_station = 0
    total_distance = 0

    # Initialize the minimum cost to travel to the rightmost gas station
    min_cost = 0

    # Loop through each gas station and calculate the minimum cost to travel to it
    for i in range(n):
        # Calculate the distance from the current gas station to the next gas station
        distance = sorted_gas_stations[i][0] - total_distance

        # Calculate the cost to travel to the next gas station
        cost = sorted_gas_stations[i][1] * (distance // 1000)

        # Check if the total cost plus the cost to travel to the next gas station exceeds the car's fuel tank capacity
        if total_distance + cost > g:
            # If it does, cancel the road trip
            return "cancel road trip"

        # Update the current gas station and the total distance traveled
        current_gas_station = i
        total_distance += distance

        # Update the minimum cost to travel to the rightmost gas station
        min_cost += cost

    # If the loop completes successfully, return the minimum cost to travel to the rightmost gas station
    return min_cost

