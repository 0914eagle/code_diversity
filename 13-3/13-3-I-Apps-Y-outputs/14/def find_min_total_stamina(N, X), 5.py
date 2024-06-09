
def find_min_total_stamina(N, X):
    # Sort the coordinates of the people
    X.sort()
    
    # Initialize the minimum total stamina to infinity
    min_total_stamina = float('inf')
    
    # Iterate over all possible meeting points
    for meeting_point in range(X[0], X[-1] + 1):
        # Initialize the total stamina to 0
        total_stamina = 0
        
        # Iterate over all people
        for i in range(N):
            # Calculate the stamina spent by the ith person
            stamina = (X[i] - meeting_point) ** 2
            
            # Add the stamina to the total stamina
            total_stamina += stamina
        
        # If the total stamina is less than the minimum total stamina, update the minimum total stamina
        if total_stamina < min_total_stamina:
            min_total_stamina = total_stamina
    
    # Return the minimum total stamina
    return min_total_stamina

