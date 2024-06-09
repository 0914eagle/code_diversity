
def max_free_tables(n, k, s):
    # Count the number of occupied tables
    num_occupied = s.count("1")
    
    # Initialize the maximum number of free tables to occupy
    max_free = 0
    
    # Iterate over the string and check if the table at each position can be occupied
    for i in range(n):
        # Check if the table at the current position is occupied
        if s[i] == "0":
            # Count the number of occupied tables between the current position and the previous occupied table
            occupied_between = 0
            for j in range(i-1, -1, -1):
                if s[j] == "1":
                    occupied_between += 1
                    break
            # Check if the number of occupied tables between the current position and the previous occupied table is less than or equal to k
            if occupied_between <= k:
                # Increment the maximum number of free tables that can be occupied
                max_free += 1
    
    # Return the maximum number of free tables that can be occupied
    return max_free

