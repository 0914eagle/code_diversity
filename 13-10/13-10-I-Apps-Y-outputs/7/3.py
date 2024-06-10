
def get_painted_black_coordinates(k, x):
    # Find the range of coordinates that potentially contain a painted black stone
    min_coord = x - k // 2
    max_coord = x + k // 2

    # Create a list of all coordinates between min_coord and max_coord, inclusive
    all_coords = list(range(min_coord, max_coord + 1))

    # Return the list of coordinates that are potentially painted black
    return all_coords

def main():
    # Read the input from stdin
    k, x = input().split()

    # Convert the input to integers
    k = int(k)
    x = int(x)

    # Call the get_painted_black_coordinates function and store the result
    painted_black_coords = get_painted_black_coordinates(k, x)

    # Print the painted black coordinates, separated by spaces
    print(*painted_black_coords, sep=' ')

if __name__ == '__main__':
    main()

