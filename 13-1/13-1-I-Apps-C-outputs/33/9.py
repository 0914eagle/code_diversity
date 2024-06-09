
def get_minimum_bags(n, k, a):
    # Initialize variables
    bags = 0
    current_bag = 0
    garbage_left = 0

    # Iterate through the input array
    for i in range(n):
        # If the current bag is full, dispose of it and start a new one
        if current_bag == k:
            bags += 1
            current_bag = 0

        # Add the current day's garbage to the current bag
        current_bag += a[i]

        # If there is garbage left over from the previous day, dispose of it
        if garbage_left > 0:
            bags += 1
            current_bag = garbage_left
            garbage_left = 0

        # If there is still garbage left over after disposing of the current bag, save it for the next day
        if current_bag > k:
            garbage_left = current_bag - k
            current_bag = k

    # If there is still garbage left over after disposing of all the bags, dispose of it in a final bag
    if garbage_left > 0:
        bags += 1

    return bags

