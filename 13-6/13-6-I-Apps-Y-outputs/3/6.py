
def get_min_heaters(n, r, arr):
    # Sort the array and find the first and last positions of all 1s
    sorted_arr = sorted(arr)
    first_positions = [i for i, x in enumerate(sorted_arr) if x == 1]
    last_positions = [i for i, x in enumerate(sorted_arr[::-1]) if x == 1]

    # Initialize the minimum number of heaters needed to warm up the whole house
    min_heaters = 0

    # Iterate through the first and last positions of all 1s
    for first, last in zip(first_positions, last_positions):
        # Calculate the range of elements that can be warmed up by the current heater
        range_start = max(first - r, 0)
        range_end = min(last + r, n - 1)

        # If the current heater can warm up all the elements in the range, increase the minimum number of heaters needed
        if range_start <= first and range_end >= last:
            min_heaters += 1

    return min_heaters

