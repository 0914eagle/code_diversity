
def max_tables(n, k, s):
    # Count the number of occupied tables
    occupied_tables = s.count("1")

    # Initialize the maximum number of free tables to occupy
    max_free_tables = 0

    # Iterate over the string
    for i in range(n):
        # Check if the current table is occupied
        if s[i] == "0":
            # Calculate the minimum distance between the current table and the next occupied table
            min_distance = occupied_tables - i

            # Check if the minimum distance is greater than or equal to k
            if min_distance >= k:
                # Increment the maximum number of free tables that can be occupied
                max_free_tables += 1

    return max_free_tables

