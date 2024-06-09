
def get_max_tables(n, k, s):
    # Initialize variables
    max_tables = 0
    current_table = 0
    previous_table = -1

    # Iterate through the string
    for i in range(n):
        # If the current table is occupied
        if s[i] == "1":
            # Check if the minimum distance between the current table and the previous table is greater than k
            if previous_table != -1 and i - previous_table <= k:
                # If not, return 0
                return 0
            # Update the current table and previous table
            current_table = i
            previous_table = i

    # If all tables are occupied, return 0
    if current_table == n - 1:
        return 0

    # Calculate the maximum number of tables that can be occupied
    max_tables = current_table + k + 1

    return max_tables

