
def f1(n, a):
    # Calculate the sum of all angles
    total_angle = sum(a)
    
    # Initialize the minimum difference between angles
    min_diff = total_angle
    
    # Iterate over all possible combinations of pieces
    for i in range(n):
        for j in range(i+1, n):
            # Calculate the sum of angles for Vasya's sector
            vasya_angle = sum(a[i:j+1])
            
            # Calculate the sum of angles for Petya's sector
            petya_angle = total_angle - vasya_angle
            
            # Calculate the difference between angles
            diff = abs(vasya_angle - petya_angle)
            
            # Update the minimum difference
            min_diff = min(min_diff, diff)
    
    return min_diff

