
def get_max_birds(ell, d, n):
    # Initialize a list to store the positions of the birds
    positions = []
    
    # Iterate through the input list and add the positions to the list
    for i in range(n):
        positions.append(int(input()))
    
    # Sort the list of positions in ascending order
    positions.sort()
    
    # Initialize a variable to store the maximum number of birds that can sit on the wire
    max_birds = 0
    
    # Iterate through the list of positions and check if the distance between each pair of positions is greater than or equal to d
    for i in range(len(positions) - 1):
        if positions[i + 1] - positions[i] >= d:
            max_birds += 1
    
    # Return the maximum number of birds that can sit on the wire
    return max_birds

def main():
    # Read the input from stdin
    ell, d, n = input().split()
    ell = int(ell)
    d = int(d)
    n = int(n)
    
    # Call the get_max_birds function and print the result
    print(get_max_birds(ell, d, n))

if __name__ == '__main__':
    main()

