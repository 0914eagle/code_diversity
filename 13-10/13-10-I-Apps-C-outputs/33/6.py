
def solve(points):
    # Convert the points to a set to remove duplicates
    points = set(points)
    
    # Initialize a set to store the unique sets of points
    unique_sets = set()
    
    # Iterate over each point in the set
    for point in points:
        # Initialize a set to store the points in the current set
        current_set = set()
        
        # Add the current point to the current set
        current_set.add(point)
        
        # Iterate over the remaining points in the set
        for other_point in points - current_set:
            # If the other point is in the current set, add it to the current set
            if other_point in current_set:
                current_set.add(other_point)
        
        # Add the current set to the unique sets
        unique_sets.add(frozenset(current_set))
    
    # Return the number of unique sets
    return len(unique_sets)

def main():
    # Read the number of points
    n = int(input())
    
    # Initialize a list to store the points
    points = []
    
    # Iterate over the number of points
    for i in range(n):
        # Read the x and y coordinates of the current point
        x, y = map(int, input().split())
        
        # Add the current point to the list
        points.append((x, y))
    
    # Solve the problem
    result = solve(points)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

