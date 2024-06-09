
def solve(A, B, Q, shrines, temples, x):
    # Sort the shrines and temples in ascending order
    shrines.sort()
    temples.sort()
    
    # Initialize the minimum distance to visit a shrine and a temple
    min_dist_shrine = float('inf')
    min_dist_temple = float('inf')
    
    # Loop through each query
    for i in range(Q):
        # Find the closest shrine and temple to the current point
        for j in range(A):
            if shrines[j] <= x[i]:
                min_dist_shrine = min(min_dist_shrine, shrines[j] - x[i])
        for j in range(B):
            if temples[j] <= x[i]:
                min_dist_temple = min(min_dist_temple, temples[j] - x[i])
        
        # Print the minimum distance to visit a shrine and a temple
        print(min(min_dist_shrine + temples[0] - x[i], min_dist_temple + shrines[0] - x[i]))
    
    return

