
def get_minimum_bags(n, k, a):
    # Initialize the number of bags to 0
    bags = 0
    # Iterate through the list of garbage produced each day
    for i in range(n):
        # If the number of garbage produced on the current day is greater than the bag's capacity,
        # calculate the number of full bags that can be filled and the remaining garbage
        if a[i] > k:
            full_bags, remaining = divmod(a[i], k)
            bags += full_bags
            a[i+1] += remaining
        # If the number of garbage produced on the current day is less than or equal to the bag's capacity,
        # add the garbage to the current day's total and move on to the next day
        else:
            a[i+1] += a[i]
    # Return the total number of bags needed to dispose of all the garbage
    return bags

