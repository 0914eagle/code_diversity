
def get_maximum_free_tables(n, k, s):
    # Count the number of occupied tables
    occupied_tables = s.count("1")

    # Initialize the maximum number of free tables to occupy
    max_free_tables = 0

    # Iterate over the string and check if the distance between any two occupied tables is greater than k
    for i in range(n - 1):
        if s[i] == "1" and s[i + 1] == "1" and i - k > 0 and i + k < n:
            max_free_tables += 1

    return max_free_tables

