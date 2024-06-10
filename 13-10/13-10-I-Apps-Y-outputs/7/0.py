
def get_potential_coordinates(k, x):
    # Initialize a list to store the potential coordinates
    potential_coordinates = []
    
    # Iterate from x - k + 1 to x + k - 1
    for i in range(x - k + 1, x + k):
        # If the current coordinate is not equal to x, add it to the list of potential coordinates
        if i != x:
            potential_coordinates.append(i)
    
    # Return the list of potential coordinates
    return potential_coordinates

def main():
    # Read the input k and x from stdin
    k, x = map(int, input().split())
    
    # Call the get_potential_coordinates function and store the result in a list
    potential_coordinates = get_potential_coordinates(k, x)
    
    # Print the list of potential coordinates in ascending order
    print(*potential_coordinates)

if __name__ == '__main__':
    main()

