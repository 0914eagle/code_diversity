
def get_max_bottles(n, h, bottle_heights):
    # Initialize a list to store the maximum number of bottles that can be placed on each shelf
    max_bottles_per_shelf = [0] * h
    max_bottles_per_shelf[0] = 1

    # Loop through the bottles and calculate the maximum number of bottles that can be placed on each shelf
    for i in range(1, n):
        for j in range(h-1, -1, -1):
            if bottle_heights[i] <= j:
                max_bottles_per_shelf[j] = max(max_bottles_per_shelf[j], max_bottles_per_shelf[j+1] + 1)
                break

    # Return the maximum number of bottles that can be placed on the top shelf
    return max_bottles_per_shelf[0]

