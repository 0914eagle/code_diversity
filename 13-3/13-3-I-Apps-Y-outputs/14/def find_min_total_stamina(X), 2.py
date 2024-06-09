
def find_min_total_stamina(X):
    # Sort the input array in ascending order
    X.sort()
    
    # Initialize the minimum total stamina to 0
    min_total_stamina = 0
    
    # Iterate over the input array
    for i in range(len(X)):
        # Calculate the stamina spent by the current person
        stamina = (X[i] - i) ** 2
        
        # Add the stamina to the minimum total stamina
        min_total_stamina += stamina
    
    # Return the minimum total stamina
    return min_total_stamina

