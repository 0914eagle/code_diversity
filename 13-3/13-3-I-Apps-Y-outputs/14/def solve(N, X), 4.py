
def solve(N, X):
    # Sort the input array in ascending order
    X.sort()
    
    # Initialize the minimum total stamina to infinity
    min_stamina = float('inf')
    
    # Iterate over all possible meeting points
    for meeting_point in X:
        # Calculate the total stamina spent by all people to attend the meeting
        total_stamina = sum((x - meeting_point) ** 2 for x in X)
        
        # Update the minimum total stamina if necessary
        min_stamina = min(min_stamina, total_stamina)
    
    # Return the minimum total stamina
    return min_stamina

