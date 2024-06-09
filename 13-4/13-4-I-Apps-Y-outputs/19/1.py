
def solve(n, a):
    # Initialize a dictionary to map each kid to their remembered kids
    remembered_kids = {}
    for i in range(n):
        remembered_kids[i+1] = [a[i][0], a[i][1]]
    
    # Initialize a list to store the final permutation
    permutation = []
    
    # Start from the first kid and follow the remembered kids to construct the permutation
    current_kid = 1
    while len(permutation) < n:
        # If the current kid has not been visited yet, add them to the permutation
        if current_kid not in permutation:
            permutation.append(current_kid)
        # Get the next kid from the remembered kids of the current kid
        current_kid = remembered_kids[current_kid][0]
    
    return permutation

