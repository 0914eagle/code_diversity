
def get_potential_black_coordinates(k, x):
    # Initialize a list to store the potential black coordinates
    potential_coordinates = []
    
    # Iterate through the range of coordinates from -1000000 to 1000000
    for i in range(-1000000, 1000001):
        # If the current coordinate is the target coordinate or is within the range of K consecutive coordinates, add it to the list of potential black coordinates
        if i == x or (i >= x - k + 1 and i <= x + k - 1):
            potential_coordinates.append(i)
    
    # Return the list of potential black coordinates in ascending order
    return sorted(potential_coordinates)

def main():
    # Read the input data from stdin
    k, x = map(int, input().split())
    
    # Call the function to get the potential black coordinates and print them
    print(*get_potential_black_coordinates(k, x))

if __name__ == '__main__':
    main()

