
def get_max_tables(n, k, s):
    # Initialize variables
    max_tables = 0
    current_table = 0
    previous_table = -1

    # Iterate through the string
    for i in range(n):
        # If the current table is occupied
        if s[i] == "1":
            # Check if the previous table is occupied and the difference between their indices is less than or equal to k
            if previous_table != -1 and abs(current_table - previous_table) <= k:
                # If so, return 0
                return 0
            # Update the previous table index
            previous_table = current_table
        # If the current table is free
        else:
            # Update the maximum number of tables that can be occupied
            max_tables += 1
        # Update the current table index
        current_table += 1

    # Return the maximum number of tables that can be occupied
    return max_tables

