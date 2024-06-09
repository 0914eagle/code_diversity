
def get_max_free_tables(n, k, s):
    # Count the number of free tables
    free_tables = s.count("0")
    
    # Iterate over the string and check if the distance between any two "1" is greater than k
    for i in range(n - 1):
        if s[i] == "1" and s[i + 1] == "1" and i - k >= 0 and s[i - k] == "1":
            free_tables -= 1
    
    return free_tables

