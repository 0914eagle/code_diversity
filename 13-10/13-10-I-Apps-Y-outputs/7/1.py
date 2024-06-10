
def get_potential_black_coordinates(k, x):
    # Find the range of coordinates that potentially contain a black stone
    min_coord = x - k // 2
    max_coord = x + k // 2
    
    # Create a list to store the potential black coordinates
    potential_black_coordinates = []
    
    # Iterate through the range of coordinates and add any black coordinates to the list
    for i in range(min_coord, max_coord + 1):
        if i != x:
            potential_black_coordinates.append(i)
    
    return potential_black_coordinates

def main():
    # Read the input k and x from stdin
    k, x = map(int, input().split())
    
    # Call the get_potential_black_coordinates function and print the result
    print(*get_potential_black_coordinates(k, x))

if __name__ == '__main__':
    main()

