
def solve(n, arr):
    # Sort the array in ascending order
    arr.sort()

    # Initialize the minimum distance and quantity of pairs
    min_dist = float('inf')
    quantity = 0

    # Iterate over the array
    for i in range(n - 1):
        # Calculate the distance between the current city and the next city
        dist = abs(arr[i + 1] - arr[i])

        # If the distance is less than the minimum distance, update the minimum distance and quantity of pairs
        if dist < min_dist:
            min_dist = dist
            quantity = 1
        # If the distance is equal to the minimum distance, increment the quantity of pairs
        elif dist == min_dist:
            quantity += 1

    # Return the minimum distance and quantity of pairs
    return min_dist, quantity

