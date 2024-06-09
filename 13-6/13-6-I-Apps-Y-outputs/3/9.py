
def get_minimum_heaters(n, r, arr):
    # Sort the array and find the leftmost and rightmost positions of the heaters
    sorted_arr = sorted(arr)
    leftmost = sorted_arr[0]
    rightmost = sorted_arr[-1]

    # Initialize the minimum number of heaters needed to warm up the whole house
    min_heaters = 0

    # Loop through each position in the array
    for i in range(n):
        # If the current position is within the range of the leftmost heater
        if i >= leftmost - r:
            # Increment the minimum number of heaters needed
            min_heaters += 1
        # If the current position is within the range of the rightmost heater
        if i <= rightmost + r:
            # Increment the minimum number of heaters needed
            min_heaters += 1

    return min_heaters

