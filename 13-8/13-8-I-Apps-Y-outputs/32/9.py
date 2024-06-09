
def solve(n, k, s):
    # Initialize the number of free tables to 0
    free_tables = 0

    # Iterate through the string
    for i in range(n):
        # Check if the current table is free
        if s[i] == "0":
            # Check if the table at position i-k and i+k are both free
            if i-k >= 0 and s[i-k] == "0" and i+k < n and s[i+k] == "0":
                # Increment the number of free tables
                free_tables += 1

    # Return the number of free tables
    return free_tables

