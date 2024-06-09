
def get_max_bottles(n, h, bottle_heights):
    # Initialize a list to store the maximum number of bottles that can be placed on each shelf
    max_bottles = [0] * (h + 1)
    max_bottles[0] = 1

    # Loop through each bottle and calculate the maximum number of bottles that can be placed on each shelf
    for i in range(n):
        for j in range(h, 0, -1):
            if bottle_heights[i] <= j:
                max_bottles[j] = max(max_bottles[j], max_bottles[j - bottle_heights[i]] + 1)
                break

    # Return the maximum number of bottles that can be placed on the top shelf
    return max_bottles[h]

