
def solve(N, X):
    # Sort the coordinates of the people
    X.sort()
    
    # Initialize the minimum total stamina to infinity
    min_stamina = float('inf')
    
    # Iterate over all possible meeting coordinates
    for i in range(N):
        # Calculate the total stamina spent by all people
        total_stamina = sum((x - i) ** 2 for x in X)
        
        # Update the minimum total stamina if necessary
        min_stamina = min(min_stamina, total_stamina)
    
    # Return the minimum total stamina
    return min_stamina

