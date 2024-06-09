
def get_max_free_tables(n, k, s):
    # Initialize the number of free tables to 0
    free_tables = 0

    # Iterate through the string
    for i in range(n):
        # If the current character is 0, we can occupy the table
        if s[i] == "0":
            # Check if the table is within the allowed distance from any other occupied table
            can_occupy = True
            for j in range(i-k, i+k+1):
                # If the index is within the range of the string and the character is 1, we cannot occupy the table
                if 0 <= j < n and s[j] == "1":
                    can_occupy = False
                    break
            # If we can occupy the table, increment the number of free tables
            if can_occupy:
                free_tables += 1

    # Return the number of free tables
    return free_tables

