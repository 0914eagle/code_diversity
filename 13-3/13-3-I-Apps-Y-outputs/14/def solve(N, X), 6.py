
def solve(N, X):
    # Sort the input array in ascending order
    X.sort()
    
    # Initialize the minimum total stamina to infinity
    min_stamina = float('inf')
    
    # Iterate over all possible meeting coordinates
    for i in range(N):
        # Calculate the total stamina spent by all people to attend the meeting at coordinate X[i]
        total_stamina = sum((x - X[i])**2 for x in X)
        
        # Update the minimum total stamina if necessary
        min_stamina = min(min_stamina, total_stamina)
    
    # Return the minimum total stamina
    return min_stamina

