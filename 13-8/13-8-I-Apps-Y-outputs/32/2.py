
def get_maximum_free_tables(s, k):
    # Initialize variables
    n = len(s)
    count = 0
    i = 0
    j = 0

    # Iterate through the string
    while i < n and j < n:
        # If the current character is '0', increment the count
        if s[j] == '0':
            count += 1
        # If the current character is '1', check if it violates the rule
        elif s[j] == '1':
            # If the difference between the current index and the previous index is less than or equal to k, decrement the count
            if j - i <= k:
                count -= 1
            # If the count becomes negative, return 0
            if count < 0:
                return 0
        i = j
        j += 1

    # Return the maximum number of free tables
    return count

