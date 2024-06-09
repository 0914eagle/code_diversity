
def get_finalists(n, a, b):
    # Sort the results in ascending order
    a.sort()
    b.sort()
    
    # Initialize the finalists array
    finalists = [0] * n
    
    # Identify the winners from each semifinal
    for i in range(n):
        if a[i] == b[i]:
            finalists[i] = 1
    
    # Identify the participants who have any chances to advance to the finals
    for i in range(n):
        if finalists[i] == 0 and a[i] <= b[n-1-i]:
            finalists[i] = 1
    
    return finalists

