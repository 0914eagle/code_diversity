
def get_max_subset(points):
    # Sort the points
    points.sort()
    
    # Initialize the maximum subset with the first point
    max_subset = [points[0]]
    
    # Iterate over the remaining points
    for i in range(1, len(points)):
        # Check if the current point is a power of two away from the last point in the maximum subset
        if points[i] - max_subset[-1] == 2**(len(max_subset) - 1):
            # If it is, add it to the maximum subset
            max_subset.append(points[i])
        # If it is not, start a new subset with the current point
        else:
            max_subset = [points[i]]
    
    return max_subset

def main():
    n = int(input())
    points = list(map(int, input().split()))
    max_subset = get_max_subset(points)
    print(len(max_subset))
    print(" ".join(map(str, max_subset)))

if __name__ == '__main__':
    main()

