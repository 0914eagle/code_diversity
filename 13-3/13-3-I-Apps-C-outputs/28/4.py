
def count_sets(points):
    # Initialize a set to store the unique sets
    unique_sets = set()
    
    # Iterate over each point
    for point in points:
        # Initialize a set to store the current set
        current_set = set()
        
        # Iterate over each other point
        for other_point in points:
            # If the other point is not the same as the current point
            if point != other_point:
                # If the other point is in the current set
                if other_point in current_set:
                    # Add the current set to the unique sets
                    unique_sets.add(current_set)
                    break
                # If the other point is not in the current set
                else:
                    # Add the other point to the current set
                    current_set.add(other_point)
        
    # Return the number of unique sets
    return len(unique_sets)

def main():
    # Read the number of points
    n = int(input())
    
    # Initialize a list to store the points
    points = []
    
    # Iterate over each point
    for i in range(n):
        # Read the x and y coordinates of the point
        x, y = map(int, input().split())
        
        # Add the point to the list
        points.append((x, y))
    
    # Call the count_sets function
    result = count_sets(points)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

