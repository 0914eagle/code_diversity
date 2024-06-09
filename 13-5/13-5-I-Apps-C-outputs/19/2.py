
def get_maximum_unique_colleagues(n, m, a):
    # Initialize a list to store the number of burgers ordered on each day
    burgers = []
    
    # Loop through each day and add the number of burgers ordered on that day to the list
    for i in range(m):
        burgers.append(a[i])
    
    # Initialize a variable to store the maximum number of unique colleagues identified
    max_unique_colleagues = 0
    
    # Loop through each day and check if the number of burgers ordered is greater than the number of salads ordered
    for i in range(m):
        # If the number of burgers ordered is greater than the number of salads ordered, update the maximum number of unique colleagues identified
        if burgers[i] > (n - burgers[i]):
            max_unique_colleagues = max(max_unique_colleagues, n - burgers[i])
    
    # Return the maximum number of unique colleagues identified
    return max_unique_colleagues

