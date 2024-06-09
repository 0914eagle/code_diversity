
def f1(n, a):
    # Calculate the sum of all angles
    total_angle = sum(a)
    
    # Initialize the minimum difference between angles
    min_diff = total_angle
    
    # Iterate over all possible combinations of pieces
    for i in range(n):
        for j in range(i+1, n):
            # Calculate the angle of the first sector
            angle1 = sum(a[i:j])
            
            # Calculate the angle of the second sector
            angle2 = total_angle - angle1
            
            # Calculate the difference between the angles
            diff = abs(angle1 - angle2)
            
            # Update the minimum difference
            min_diff = min(min_diff, diff)
    
    return min_diff

