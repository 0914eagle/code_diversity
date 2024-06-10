
def get_painted_coordinates(k, x):
    # Initialize a set to store the painted coordinates
    painted_coordinates = set()
    
    # Iterate from x-k to x+k
    for i in range(x-k, x+k+1):
        # If the current coordinate is not equal to x, add it to the set of painted coordinates
        if i != x:
            painted_coordinates.add(i)
    
    # Return the set of painted coordinates
    return painted_coordinates

def main():
    # Read the input from stdin
    k, x = map(int, input().split())
    
    # Call the get_painted_coordinates function and store the result in a variable
    painted_coordinates = get_painted_coordinates(k, x)
    
    # Sort the painted coordinates in ascending order
    sorted_coordinates = sorted(painted_coordinates)
    
    # Print the sorted coordinates separated by spaces
    print(*sorted_coordinates, sep=' ')

if __name__ == '__main__':
    main()

