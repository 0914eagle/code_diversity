
def get_minimum_bags(n, k, a):
    # Initialize the number of bags to 0
    bags = 0
    # Iterate through the list of garbage produced each day
    for i in range(n):
        # If the number of garbage produced on the current day is greater than the bag's capacity, calculate the number of full bags needed
        if a[i] > k:
            bags += a[i] // k
        # If the number of garbage produced on the current day is not a multiple of the bag's capacity, calculate the number of partial bags needed
        if a[i] % k != 0:
            bags += 1
    # Return the total number of bags needed
    return bags

