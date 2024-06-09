
def get_max_free_tables(n, k, s):
    # Initialize the number of free tables to 0
    free_tables = 0

    # Iterate through the string
    for i in range(n):
        # Check if the current table is free
        if s[i] == "0":
            # Check if the previous table is occupied
            if i > 0 and s[i-1] == "1":
                # Check if the difference between the current table and the previous table is greater than k
                if i - (i-1) > k:
                    # Increment the number of free tables
                    free_tables += 1

            # Check if the next table is occupied
            if i < n-1 and s[i+1] == "1":
                # Check if the difference between the current table and the next table is greater than k
                if (i+1) - i > k:
                    # Increment the number of free tables
                    free_tables += 1

    # Return the number of free tables
    return free_tables

