
def solve(n, k, weights):
    # Sort the weights in descending order
    weights.sort(reverse=True)
    # Initialize the number of days needed to collect all pebbles
    days = 0
    # Loop through the weights and calculate the number of days needed for each type of pebble
    for weight in weights:
        # Calculate the number of pebbles that can be collected on this day
        collected = min(k, weight)
        # Add the number of days needed for this type of pebble to the total number of days
        days += (weight // collected) + (1 if weight % collected > 0 else 0)
    # Return the minimum number of days needed to collect all pebbles
    return days

