
def solve(N, boys, A, B):
    # Sort the list of boys in ascending order
    boys.sort()
    
    # Initialize the minimum difference to 0
    min_diff = 0
    
    # Iterate through each boy and calculate the difference between his name and the girl's name
    for boy in boys:
        # Calculate the difference between the boy's name and the girl's name
        diff = abs(boy - (A + B) // 2)
        
        # If the difference is greater than the minimum difference, update the minimum difference
        if diff > min_diff:
            min_diff = diff
    
    # Return the girl's name as the middle value between A and B minus the minimum difference
    return (A + B) // 2 - min_diff

