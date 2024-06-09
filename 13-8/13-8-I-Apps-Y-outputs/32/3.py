
def max_tables(n, k, s):
    # Count the number of occupied tables
    num_occupied = s.count("1")
    # Initialize the maximum number of free tables to occupy
    max_free = 0
    # Iterate over the string
    for i in range(n):
        # Check if the table is occupied
        if s[i] == "0":
            # Calculate the minimum distance to the next occupied table
            min_dist = k + 1
            # Find the next occupied table to the right
            for j in range(i+1, n):
                if s[j] == "1":
                    min_dist = min(min_dist, j - i)
                    break
            # Find the next occupied table to the left
            for j in range(i-1, -1, -1):
                if s[j] == "1":
                    min_dist = min(min_dist, i - j)
                    break
            # Update the maximum number of free tables
            max_free = max(max_free, min_dist - 1)
    # Return the maximum number of free tables
    return num_occupied + max_free

