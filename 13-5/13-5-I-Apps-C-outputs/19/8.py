
def solve(n, m, a):
    # Initialize a list to store the number of burgers ordered on each day
    burgers = []
    
    # Iterate over the input list and add the number of burgers ordered on each day to the list
    for i in range(m):
        burgers.append(a[i])
    
    # Initialize a variable to store the maximum number of unique colleagues identified
    max_unique = 0
    
    # Iterate over the list of burgers ordered on each day
    for i in range(m):
        # If the number of burgers ordered on the current day is greater than the maximum number of unique colleagues identified so far, update the maximum number of unique colleagues identified
        if burgers[i] > max_unique:
            max_unique = burgers[i]
    
    # Return the maximum number of unique colleagues identified
    return max_unique

