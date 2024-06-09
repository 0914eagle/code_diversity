
def solve(n, a, b, k, f, trips):
    # Initialize variables
    total_cost = 0
    travel_cards = 0
    current_stop = "Start"

    # Iterate through the trips
    for i in range(n):
        # Get the start and end stops of the current trip
        start_stop, end_stop = trips[i]

        # Check if the trip is a transshipment
        if start_stop == current_stop:
            # If it is a transshipment, pay the reduced cost
            total_cost += b
        else:
            # If it is not a transshipment, pay the regular cost
            total_cost += a

        # Update the current stop
        current_stop = end_stop

        # Check if a travel card can be purchased
        if travel_cards < k and start_stop != "Start" and end_stop != "Start":
            # If a travel card can be purchased, do so
            travel_cards += 1
            total_cost -= f

    # Return the total cost
    return total_cost
