
def get_max_locations(distances):
    # Sort the distances in non-decreasing order
    sorted_distances = sorted(distances)
    
    # Initialize the maximum number of locations as 1
    max_locations = 1
    
    # Iterate over the sorted distances
    for i in range(len(sorted_distances)):
        # Check if the current distance is greater than or equal to the previous distance
        if i > 0 and sorted_distances[i] >= sorted_distances[i-1]:
            # If it is, increment the maximum number of locations
            max_locations += 1
    
    return max_locations

def main():
    # Read the number of days from stdin
    n = int(input())
    
    # Read the distances traveled by the shark on each day from stdin
    distances = list(map(int, input().split()))
    
    # Call the get_max_locations function and print the result
    print(get_max_locations(distances))

if __name__ == '__main__':
    main()

