
def get_maximum_free_tables(n, k, s):
    # Count the number of occupied tables
    num_occupied_tables = s.count("1")

    # If all tables are occupied, return 0
    if num_occupied_tables == n:
        return 0

    # Initialize the maximum number of free tables to occupy
    max_free_tables = 0

    # Iterate over the tables
    for i in range(n):
        # Check if the table is occupied
        if s[i] == "0":
            # Calculate the minimum distance between the current table and the nearest occupied table
            min_distance = k + 1
            for j in range(i):
                if s[j] == "1":
                    min_distance = min(min_distance, abs(i - j))

            # If the minimum distance is greater than k, we can occupy the current table
            if min_distance > k:
                max_free_tables += 1

    return max_free_tables

