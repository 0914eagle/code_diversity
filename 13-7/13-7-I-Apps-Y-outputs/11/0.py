
def get_subset(points):
    # Sort the points
    points.sort()
    
    # Initialize the subset with the first point
    subset = [points[0]]
    
    # Iterate over the remaining points
    for i in range(1, len(points)):
        # Check if the current point is a power of two away from the last point in the subset
        if points[i] - subset[-1] == 2**(len(subset) - 1):
            # If it is, add it to the subset
            subset.append(points[i])
        else:
            # If it's not, return the current subset
            return subset
    
    # If we reach the end of the list, return the subset
    return subset

def main():
    # Read the number of points and their coordinates from stdin
    n = int(input())
    points = [int(x) for x in input().split()]
    
    # Get the maximum possible subset
    subset = get_subset(points)
    
    # Print the size of the subset and its coordinates
    print(len(subset))
    print(*subset)

if __name__ == '__main__':
    main()

