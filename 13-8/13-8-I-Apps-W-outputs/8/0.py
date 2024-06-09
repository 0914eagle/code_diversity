
def solve(n, k, weights):
    # Sort the weights in non-decreasing order
    weights.sort()
    # Initialize the number of days needed to collect all pebbles as 0
    days = 0
    # Loop through each pebble type
    for i in range(n):
        # Calculate the number of pebbles that can be collected on this day
        day_capacity = k * weights[i]
        # If the number of pebbles left to collect is greater than the day capacity,
        # then the number of days needed to collect all pebbles will be at least 1
        if sum(weights[i:]) > day_capacity:
            days += 1
    return days

