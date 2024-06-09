
def count_ways(parts):
    # Initialize the number of ways to complete the figure as 0
    num_ways = 0

    # Loop through each pair of holes
    for i in range(len(parts)):
        for j in range(i+1, len(parts)):
            # If the holes are not in the same part and the number of holes in the part is greater than 1
            if parts[i] != parts[j] and parts[i] > 1:
                # Increment the number of ways to complete the figure
                num_ways += 1

    # Return the number of ways to complete the figure modulo 998244353
    return num_ways % 998244353

