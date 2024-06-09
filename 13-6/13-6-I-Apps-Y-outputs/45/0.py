
def max_tables(n, k, s):
    # Count the number of occupied tables
    occupied_tables = s.count("1")

    # Check if the number of occupied tables is less than or equal to the maximum allowed
    if occupied_tables <= n:
        return 0

    # Initialize the maximum number of tables that can be occupied
    max_tables = 0

    # Iterate over the string and check if the table at each position can be occupied
    for i in range(n):
        # Check if the table at the current position is empty
        if s[i] == "0":
            # Count the number of occupied tables between the current position and the previous occupied table
            occupied_tables_between = 0
            for j in range(i, -1, -1):
                if s[j] == "1":
                    occupied_tables_between += 1
                    break

            # Check if the number of occupied tables between the current position and the previous occupied table is less than or equal to k
            if occupied_tables_between <= k:
                max_tables += 1

    return max_tables

