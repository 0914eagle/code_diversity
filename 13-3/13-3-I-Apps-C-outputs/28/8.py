
def count_sets(points):
    # Initialize a set to store the unique sets
    unique_sets = set()
    
    # Iterate over each point
    for point in points:
        # Initialize a set to store the points in the current set
        current_set = set()
        
        # Iterate over each point again
        for other_point in points:
            # If the current point is not the same as the other point
            if point != other_point:
                # If the current point is in the same column as the other point
                if point[0] == other_point[0]:
                    # Add the other point to the current set
                    current_set.add(other_point)
        
        # Add the current set to the unique sets
        unique_sets.add(frozenset(current_set))
    
    # Return the number of unique sets
    return len(unique_sets)

def main():
    # Read the number of points
    n = int(input())
    
    # Read the points
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    
    # Call the count_sets function
    result = count_sets(points)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

