
def find_min_total_stamina(N, X):
    # Sort the coordinates of the people in ascending order
    X.sort()
    
    # Initialize the minimum total stamina to infinity
    min_total_stamina = float('inf')
    
    # Iterate over all possible meeting coordinates
    for meeting_coord in range(X[0], X[-1] + 1):
        # Initialize the total stamina spent by all people to 0
        total_stamina = 0
        
        # Iterate over all people and calculate their stamina spent for the meeting
        for i in range(N):
            total_stamina += (X[i] - meeting_coord) ** 2
        
        # If the total stamina spent is less than the current minimum, update the minimum
        if total_stamina < min_total_stamina:
            min_total_stamina = total_stamina
    
    # Return the minimum total stamina
    return min_total_stamina

